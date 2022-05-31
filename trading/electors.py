#import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("electors").getOrCreate()
df = spark.read.csv("/home/felipelx/Downloads/perfil_eleitorado_ATUAL.csv", header=True, sep=";")
df = df.cache()
df.show()

spark.stop()
# df = pd.read_csv("/home/felipelx/Downloads/perfil_eleitorado_ATUAL.csv", encoding="latin1", sep=";")
# print(df.info())
# df["Number"] = 1
# print(df.columns)
#df_group = df.groupby(["SG_UF", "DS_GENERO", "DS_FAIXA_ETARIA"], as_index=False)["Number"].count()
# print(df_group.head())