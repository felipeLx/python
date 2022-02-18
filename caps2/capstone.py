from simpledbf import Dbf5

placenames = Dbf5('../../../../Downloads/yearly_deforestation_2021_pri.dbf')
df = placenames.to_dataframe()

print(df.info())