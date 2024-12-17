from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

def build_index(data_dir):
    documents = SimpleDirectoryReader(data_dir).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    print("Index built successfully.")
    return index

def query_index(index, question):
    response = index.query(question)
    print(response)

if __name__ == "__main__":
    index = build_index("../data/processed")
    query_index(index, "Summarize the sales data.")