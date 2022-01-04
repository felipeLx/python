import sqlite3
import pandas as pd

from whatstk import WhatsAppChat
filepath = "./chatsettingsbackup.db.crypt14"

# chat = WhatsAppChat.from_source(filepath=filepath)
# print(chat)

con = sqlite3.connect("./chatsettingsbackup.db.crypt14")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con)
con.close()
tables