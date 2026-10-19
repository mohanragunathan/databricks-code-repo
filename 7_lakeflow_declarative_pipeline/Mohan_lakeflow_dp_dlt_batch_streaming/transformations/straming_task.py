from pyspark import pipelines
@pipelines.table(name="catalog1_we47.schema1_we47.shipment1_bronze3")#Since I used readStream function, this pipelines.table will create a streaming table (incremental table SCDType2 (only inserts are engaged))
def load_data_bronze_imp_dp():
    df1 = spark.readStream.table("catalog1_we47.schema1_we47.silver_staff")  # only work in the delta tables only inserts, skip updates/deletes
    return df1