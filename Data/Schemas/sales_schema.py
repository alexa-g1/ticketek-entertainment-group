from pyspark.sql.types import (
    StructType, StructField,
    IntegerType, DoubleType, StringType,
)

sales_read_schema = StructType([
    StructField("sale_id", StringType()),
    StructField("product_id", StringType()),
    StructField("sale_date", StringType()),  
    StructField("quantity", IntegerType()),
    StructField("price", DoubleType()),
])