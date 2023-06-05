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
       "and pzone_nr not in ('Global Підбір', 'Імпорт Косметика', 'Підбір VICHI', 'Підбір ПАККОР', " \
        "'Підбір Соломія Сервіс', 'Підбір Зовнішні чаї', 'Шторк Імпорт', 'Yarych підбір')" \
       "GROUP by pzone_nr"



def pandas(sql= test1):
    #cursor = connection.cursor()
    df = pd.read_sql(sql, connection)
    dfi.export(df, 'dataframe.png')
    print(df)
    #cursor.close()
    print("Successfully closed Oracle Database")
    return df

# pandas()

def privyazka(product_nr):
    sql = f"select PRODUCT_NR, NAME, SP_NR from QWHV_SPREAD_SP_ASSIGNMENT where product_nr = '{product_nr}' and wh_nr = '1'"
    df = pd.read_sql(sql, connection)
    dfi.export(df, 'privyazka.png')
    print(product_nr)
    print(df)
    return df

privyazka("000024774")