import getpass
import oracledb
import os
import json
import pandas as pd
import dataframe_image as dfi

CLIENT_DIR = "/Users/admin/Downloads/instantclient_19_8/"
oracledb.init_oracle_client(lib_dir=CLIENT_DIR, config_dir=None, error_url=None, driver_name=None)
connection = oracledb.connect(
    user="qguaradm",
    password="quantum",
    dsn="WMSUB1.berta.corp/lc2")
print("Successfully connected to Oracle Database")

test1 = "select pzone_nr, COUNT(pzone_nr) as KILKIST " \
       "FROM TRV_SPREAD_TRANS_ORDERS_FAST " \
       "where transport_type_id = 'SH' " \
       "and pzone_nr not in ('Global Підбір', 'Імпорт Косметика', 'Підбір VICHI', 'Підбір ПАККОР', 'Підбір Соломія Сервіс', 'Підбір Зовнішні чаї', 'Шторк Імпорт')" \
       "GROUP by pzone_nr"



def pandas(sql):
    #cursor = connection.cursor()
    df = pd.read_sql(sql, connection)
    dfi.export(df, 'dataframe.png')
    print(df)
    #cursor.close()
    print("Successfully closed Oracle Database")

pandas(test1)
