import os
import streamlit as st
from openai import OpenAI
from retriever import SimpleRetriever
import prompts

# ========== 页面配置 ==========
st.set_page_config(page_title="A3 代码调试与注释助手", layout="wide")

# ========== 侧边栏 ==========
with st.sidebar:
    st.header("使用必读")
    st.markdown("""
    1. 请粘贴**完整报错原文**。
    2. 说明**语言/版本**和**已尝试操作**。
    3. 不要贴密钥、密码、客户信息。
    4. 修改建议需**本地运行验证**后才算有效。
    """)
    st.divider()
    st.caption("AI声明：本应用使用 智谱 GLM 提供对话能力，知识库检索在本地完成。AI输出不替代专业判断。")
    if st.button("清空对话 / 重新开始"):
        st.session_state.messages = [{"role": "system", "content": prompts.SYSTEM_PROMPT_V1}]
        st.rerun()

# ========== 初始化本地检索资源 ==========
@st.cache_resource
def load_retriever():
    if not os.path.isdir("knowledge"):
        st.error("找不到 knowledge 文件夹！请确保创建了该文件夹及对应的md文件。")
        return None
    return SimpleRetriever("./knowledge")

retriever = load_retriever()

# ========== 主界面 ==========
st.title("🛠️ 代码调试与注释助手 (A3)")
st.caption("解决报错看不懂、定位慢、注释不会写的问题")

# 1. API Key 处理 (优先读取环境变量，其次读取界面输入)
api_key = os.environ.get("ZHIPU_API_KEY", "")
if not api_key:
    api_key = st.text_input("请输入 智谱 API Key 开始对话（或提前设置环境变量 ZHIPU_API_KEY）", type="password")
    if not api_key:
        st.info("免费申请地址：open.bigmodel.cn (注册并实名后，在个人中心创建 API Key)")
        st.stop()

# 2. 配置智谱的客户端 (注意这里是智谱的 Base URL)
client = OpenAI(
    api_key=api_key, 
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

# 3. 会话状态初始化
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": prompts.SYSTEM_PROMPT_V1}]

# 渲染历史记录
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 处理用户输入
if user_input := st.chat_input("粘贴报错原文 + 代码片段 + 语言/版本 + 已尝试操作"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 第一步：检索本地知识库
    hits = retriever.search(user_input) if retriever else []
    context_text = ""
    if hits:
        context_text = "\n\n".join(
            f"【知识库引用：{h['source']}】\n{h['text']}" for h in hits
        )
        # 界面上展示命中的知识库片段
        with st.expander("🔍 本次命中的本地知识库片段（可展开核对）", expanded=False):
            for h in hits:
                st.markdown(f"**{h['source']}**")
                st.code(h["text"][:300] + "...", language="markdown")

    # 第二步：构造发给大模型的消息（插入知识库内容）
    messages_for_llm = list(st.session_state.messages)
    if context_text:
        messages_for_llm.insert(
            1,
            {"role": "system", "content": "以下是检索到的知识库内容，请优先依据这些内容回答，并在输出中注明引用来源：\n\n" + context_text}
        )

    # 第三步：调用 智谱 GLM-4-Flash 模型
    with st.chat_message("assistant"):
        with st.spinner("正在诊断与生成建议..."):
            try:
                response = client.chat.completions.create(
                    model="glm-4-flash", # 智谱的免费模型
                    messages=messages_for_llm,
                    temperature=0.2,
                    stream=False
                )
                answer = response.choices[0].message.content
            except Exception as e:
                answer = f"API 调用失败：{e}\n请检查 API Key 是否正确、网络是否通畅，或账户是否已完成实名认证。"
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})