import pandas as pd

sorter = ['South Africa', 'Australia', 'Columbia']
read_file = pd.read_excel('/home/felipelx/Downloads/data.xlsx', sheet_name='solution', engine='openpyxl')
final_df = read_file.sort_values(by=['COMMODITY SOURCE LOCATION'], ascending=False)

final_df.to_csv('/home/felipelx/Downloads/data.csv', index = None, header=True)


