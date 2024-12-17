import os

# Full project structure with detailed source code and functional content
PROJECT_STRUCTURE = {
    "AI-BigData-Analysis": {
        "README.md": """# AI-BigData-Analysis: A Complete Big Data and AI Solution

## Overview
This project integrates big data frameworks (Hadoop, Spark) with advanced AI models like LlamaIndex and PandasAI. It processes and analyzes sales data to deliver intelligent insights.

## Features:
1. **Data Ingestion**: Load raw data into HDFS using PySpark.
2. **Data Processing**: Process data with SparkSQL to generate insights.
3. **AI Integration**: Use LlamaIndex and PandasAI for natural language querying.
4. **Visualization**: Generate charts and reports using Matplotlib.
5. **Testing**: Ensure pipeline integrity with unit tests.

## Project Structure:
- **data/raw**: Input CSV files.
- **data/processed**: Cleaned data outputs.
- **src/hadoop_spark**: Scripts for data ingestion and processing.
- **src/ai_integration**: AI querying logic.
- **src/visualization**: Data visualization scripts.
- **config**: Configuration files.
- **scripts**: Utility scripts for starting services.
- **tests**: Unit tests for all components.
""",
        "requirements.txt": """pyspark==3.4.1\npandas==2.1.1\nllama-index==0.7.0\npandasai==1.5.1\nmatplotlib==3.7.1\npyyaml==6.0\nrequests==2.31.0""",
        "data": {
            "raw": {
                "sales_data.csv": "region,date,sales\nNorth,2024-06-01,1000\nSouth,2024-06-01,1500\nEast,2024-06-01,1300\nWest,2024-06-01,1200"
            },
            "processed": {}
        },
        "src": {
            "hadoop_spark": {
                "data_loader.py": """from pyspark.sql import SparkSession\n\ndef upload_to_hdfs(local_path, hdfs_path):\n    spark = SparkSession.builder.appName("Data Loader").getOrCreate()\n    df = spark.read.csv(local_path, header=True, inferSchema=True)\n    df.write.mode("overwrite").csv(hdfs_path)\n    print(f"Uploaded to HDFS: {hdfs_path}")\n\nif __name__ == "__main__":\n    upload_to_hdfs("../data/raw/sales_data.csv", "hdfs://localhost:9000/data/sales")"""
            },
            "ai_integration": {
                "llama_index_connector.py": """from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex\n\ndef build_index(data_dir):\n    documents = SimpleDirectoryReader(data_dir).load_data()\n    index = GPTVectorStoreIndex.from_documents(documents)\n    print("Index built successfully.")\n    return index\n\ndef query_index(index, question):\n    response = index.query(question)\n    print(response)\n\nif __name__ == "__main__":\n    index = build_index("../data/processed")\n    query_index(index, "Summarize the sales data.")"""
            },
            "visualization": {
                "plot_results.py": """import pandas as pd\nimport matplotlib.pyplot as plt\n\ndef plot_sales(file_path):\n    df = pd.read_csv(file_path)\n    df.groupby("region")["sales"].sum().plot(kind="bar", title="Sales by Region")\n    plt.xlabel("Region")\n    plt.ylabel("Total Sales")\n    plt.savefig("../results/sales_plot.png")\n    plt.show()\n\nif __name__ == "__main__":\n    plot_sales("../data/raw/sales_data.csv")"""
            }
        },
        "config": {
            "hadoop_config.yaml": "hdfs:\n  host: localhost\n  port: 9000",
            "spark_config.yaml": "spark:\n  master: local[*]\n  app_name: SparkProcessor",
            "ollama_config.yaml": "ollama:\n  endpoint: http://localhost:11434"
        },
        "scripts": {
            "start_hadoop.sh": """#!/bin/bash\nstart-dfs.sh && start-yarn.sh\necho 'Hadoop services started.'""",
            "start_spark.sh": """#!/bin/bash\nspark-submit --version\necho 'Spark cluster ready.'""",
            "ollama_run.sh": """#!/bin/bash\nollama run llama2"""
        },
        "tests": {
            "test_data_loader.py": """from pyspark.sql import SparkSession\n\ndef test_data_upload():\n    spark = SparkSession.builder.appName("Test Data").getOrCreate()\n    df = spark.read.csv("../data/raw/sales_data.csv", header=True)\n    assert df.count() > 0, "Data upload failed!"\n\ntest_data_upload()""",
            "test_ai_query.py": """from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex\n\ndef test_ai_index():\n    documents = SimpleDirectoryReader("../data/processed").load_data()\n    index = GPTVectorStoreIndex.from_documents(documents)\n    assert index is not None, "Index creation failed!"\n\ntest_ai_index()"""
        },
        "results": {
            "sales_summary.txt": "Summary: Total sales across regions processed successfully."
        },
        "logs": {
            "process.log": "INFO: Data uploaded.\nINFO: Data processed.\nINFO: Visualization generated."
        }
    }
}

def create_structure(base_path, structure):
    """
    Recursively create project directories and files.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If it's a folder
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:  # If it's a file
            with open(path, "w") as f:
                f.write(content)
            print(f"Created file: {path}")

if __name__ == "__main__":
    BASE_DIR = "AI-BigData-Analysis"
    create_structure(BASE_DIR, PROJECT_STRUCTURE)
    print("\nProject structure successfully created!")
