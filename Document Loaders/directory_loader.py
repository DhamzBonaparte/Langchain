from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(path="Books", glob="*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()
print(len(docs))

print(docs[326].page_content)
print(docs[326].metadata)

docs2 = loader.lazy_load()
for i in docs:
    print(i.metadata)

for i in docs2:
    print(i.metadata)
