from pyspark import pipelines as dp
@dp.table(name="workspace.default.shipmentwe47")
def return_df():
    df1=spark.read.table("gcp_mysql_fc_wd361.logistics.shipments1")
    return df1