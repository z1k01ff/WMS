import getpass
import oracledb
import os
import json


CLIENT_DIR = "/Users/admin/Downloads/instantclient_19_8/"


oracledb.init_oracle_client(lib_dir=CLIENT_DIR, config_dir=None, error_url=None, driver_name=None)


# pw = getpass.getpass("Pass: ")

connection = oracledb.connect(
    user="qguaradm",
    password="quantum",
    dsn="WMSUB1.berta.corp/lc2")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

result = 0
result2 = {}
step = 0
for row in cursor.execute("select * from tr_transports_fast where transport_type_nr = 'SH'"):
    print(row)

    result2.update({step: row})
    step += 1
    result += 1
# with open("test.json", "w") as file:
#     json.dump(result2, file, indent=4, ensure_ascii=False, default=str)

print(result)



cursor.close()
print("Successfully closed Oracle Database")