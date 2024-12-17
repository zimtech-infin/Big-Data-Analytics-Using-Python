from pyspark.sql import SparkSession

def test_data_upload():
    spark = SparkSession.builder.appName("Test Data").getOrCreate()
    df = spark.read.csv("../data/raw/sales_data.csv", header=True)
    assert df.count() > 0, "Data upload failed!"

test_data_upload()