# -*- Python -*-

import mysql.connector
from mysql.connector import errorcode

dbconfig = {
  'user': 'ares',
  'password': '$$ares$$',
  'host': '10.66.180.15:3306',
  'database': 'ARES_DB',
  'raise_on_warnings': True,
}

try:
    cnx = mysql.connector.connect(**dbconfig)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database {} does not exist".format(dbconfig['database']))
    else:
        print(err)
else:
    cnx.close()


cursor = cnx.cursor()

query = ("SELECT * FROM DATA_DEFS_TBL")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for (pid, name, desc, engvalunit, datacateg,
     raw_datacateg, active, system_element) in cursor:
    print("{} - {} - {} ({})".format(pid, name, desc, datacateg))
    
cursor.close()


