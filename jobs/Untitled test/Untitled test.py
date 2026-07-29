import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_1785284763310 = spark.read.format("json") \
    .option("multiLine", "true") \
    .load("s3://amazon-sagemaker-598122632870-us-east-2-967cfa2a2653/dzd-4ly7wie4jqr90p/53fl1drf6u4hih/shared/.libs.json")
