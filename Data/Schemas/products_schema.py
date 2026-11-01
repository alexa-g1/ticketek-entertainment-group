from pyspark.sql.types import (
    StructType, StructField,
    IntegerType, DoubleType, StringType, BooleanType,
)

products_details_schema = StructType([
    StructField("brand", StringType()),
    StructField("warranty", StringType()),
    StructField("material", StringType()),
    StructField("wireless", BooleanType()),
])

products_read_schema = StructType([
    StructField("product_id", StringType()),
    StructField("name", StringType()),
    StructField("category", StringType()),
    StructField("details", products_details_schema),
])