import os
import re
from collections import Counter

class SimpleRetriever:
    def __init__(self, folder_path):
        self.docs = []
        if os.path.isdir(folder_path):
            for fname in os.listdir(folder_path):
                if fname.endswith(".md") or fname.endswith(".txt"):
                    path = os.path.join(folder_path, fname)
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        self.docs.append({"source": fname, "text": content})

    def search(self, query, top_k=3):
        query_words = set(re.findall(r'[a-zA-Z0-9_]+', query.lower()))
        scored = []
        for doc in self.docs:
            doc_words = Counter(re.findall(r'[a-zA-Z0-9_]+', doc["text"].lower()))
            score = sum(min(doc_words[w], 3) for w in query_words if w in doc_words)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{"text": item[1]["text"], "source": item[1]["source"]} for item in scored[:top_k]]