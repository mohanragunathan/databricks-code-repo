from pyspark import pipelines as dp

@dp.table()
def myrangetable():
    df=spark.range(10)
    return df
