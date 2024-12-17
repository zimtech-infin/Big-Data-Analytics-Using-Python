from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

def test_ai_index():
    documents = SimpleDirectoryReader("../data/processed").load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    assert index is not None, "Index creation failed!"

test_ai_index()