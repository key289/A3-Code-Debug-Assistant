# HTTP 状态码标准
出处：MDN Web Docs (HTTP Status)

## 404 Not Found
- 症状：资源找不到。
- 原因：前端请求 URL 拼写错误、后端未注册该路由、代理配置错误。
- 排查：在浏览器 F12 Network 面板查看实际请求的 URL。

## 401 Unauthorized
- 症状：未授权 / 认证失败。
- 原因：未携带 Token、Token 过期、API Key 错误。

## 403 Forbidden
- 症状：拒绝访问。
- 原因：已登录但无权限访问该接口，或触发了服务器安全策略。