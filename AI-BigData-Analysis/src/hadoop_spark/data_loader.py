from pyspark.sql import SparkSession

def upload_to_hdfs(local_path, hdfs_path):
    spark = SparkSession.builder.appName("Data Loader").getOrCreate()
    df = spark.read.csv(local_path, header=True, inferSchema=True)
    df.write.mode("overwrite").csv(hdfs_path)
    print(f"Uploaded to HDFS: {hdfs_path}")

if __name__ == "__main__":
    upload_to_hdfs("../data/raw/sales_data.csv", "hdfs://localhost:9000/data/sales")