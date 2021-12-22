import sqlite3
import pandas as pd
from sqlalchemy import create_engine

conn = sqlite3.connect('chinook.db')
cur = conn.cursor()
cur.execute('SELECT * FROM employees LIMIT=5;')

results = cur.fetchall()
results

df = pd.DataFrame(results)
df.head()

cur.close()
conn.close()

conn2 = sqlite3.connect('chinook.db')
df2 = pd.read_sql('SELECT * FROM employees', conn)
df2.head()

df3 = pd.read_sql('SELECT * FROM employees', conn,index_col='EmployeeId', parse_dates=['BirthDate', 'HireDate'])
df3.head()


engine = create_engine('sqlite:///chinook.db')
connection = engine.connect()
df = pd.read_sql_table('employees', con=connection)
df.head()

# reading HTML tables
# !pip install lxml
from IPython.core.display import display, HTML
display(HTML(html_string))

dfs = pd.read_html(html_string)
len(dfs)
df4 = dfs[0]