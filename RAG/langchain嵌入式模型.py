from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()

print(model.embed_query("吃苹果"))
print(model.embed_documents(["你喜欢吃苹果吗","我不喜欢吃苹果"]))