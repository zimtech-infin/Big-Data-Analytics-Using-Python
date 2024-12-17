import os

# Define the project tree structure as a nested dictionary
project_tree = {
    "AI-BigData-Analysis": {
        "README.md": "# AI-Powered Big Data Analysis\n\nProject documentation placeholder.",
        "requirements.txt": "pandas\npandasai\nllama-index\npyspark\nmatplotlib\nrequests",
        "data": {
            "raw": {"sales_data.csv": "id,region,sales\n1,North,100\n2,South,200"},
            "processed": {}
        },
        "notebooks": {
            "01_data_ingestion.ipynb": "",
            "02_spark_processing.ipynb": "",
            "03_llama_index_integration.ipynb": "",
            "04_pandasai_queries.ipynb": ""
        },
        "src": {
            "hadoop_spark": {
                "data_loader.py": "# Script to upload data to HDFS",
                "spark_processing.py": "# PySpark script for data processing"
            },
            "ai_integration": {
                "llama_index_connector.py": "# Integration script for LlamaIndex",
                "pandasai_query.py": "# Script to run queries using PandasAI",
                "ollama_client.py": "# Ollama API interaction script"
            },
            "visualization": {
                "plot_results.py": "# Script to generate charts and graphs"
            }
        },
        "config": {
            "hadoop_config.yaml": "dfs.replication: 1\n# Hadoop configuration placeholder",
            "spark_config.yaml": "spark.master: local\n# Spark configuration placeholder",
            "ollama_config.yaml": "api_url: http://localhost:11434\n# Ollama config placeholder"
        },
        "logs": {
            "process.log": ""
        },
        "results": {
            "insights_summary.txt": "Summary of AI-generated insights.",
            "region_sales_plot.png": "",
            "spark_output": {}
        },
        "scripts": {
            "start_hadoop.sh": "#!/bin/bash\necho 'Starting Hadoop services...'",
            "start_spark.sh": "#!/bin/bash\necho 'Starting Spark services...'",
            "ollama_run.sh": "#!/bin/bash\necho 'Running Llama2 with Ollama...'"
        },
        "tests": {
            "test_spark_processing.py": "# Unit test for Spark processing script",
            "test_llama_index.py": "# Unit test for LlamaIndex integration",
            "test_pandasai.py": "# Unit test for PandasAI query script"
        }
    }
}

def create_project_structure(base_path, tree):
    """
    Recursively create the project directory structure with files.

    Args:
        base_path (str): The root directory where the project will be created.
        tree (dict): A nested dictionary representing the directory structure.
    """
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # If the value is a dictionary, create a directory and recurse
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            # If the value is not a dictionary, create a file with placeholder content
            with open(path, "w") as f:
                f.write(content)
            print(f"Created file: {path}")

if __name__ == "__main__":
    root_dir = "AI-BigData-Analysis"
    create_project_structure(".", project_tree)
    print("Project tree creation complete!")
