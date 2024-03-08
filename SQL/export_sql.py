import pymysql
import pandas as pd

HOST = "localhost"
USER = "root"
PWD = "1234"
CHARSET = "utf8"
DB = "mysqldb"
TABLE = "Weather"

conn = pymysql.connect(host=HOST, user=USER, password=PWD, db=DB, charset=CHARSET)
cur = conn.cursor()


query = f"""
SELECT *
FROM {TABLE}
"""

df = pd.read_sql(query, con=conn)
print(df.to_markdown(index=False))
