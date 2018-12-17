# -*- Python -*-

import pymysql

import datetime

connection = pymysql.connect(host='10.66.180.15',
                             port=3306,
                             user='ares',
                             password='$$ares$$',                             
                             db='ARES_DB',
                             cursorclass=pymysql.cursors.DictCursor)

print("Connection to ARES_DB successful")

try:
    with connection.cursor() as cursor:
        query = ("SELECT * FROM DATA_DEFS_TBL")

        #hire_start = datetime.datetime.date(1999, 1, 1)
        #hire_end = datetime.datetime.date(1999, 12, 31)

        cursor.execute(query)

        print("cursor.description: ", cursor.description)

        for row in cursor:
            print(row)
            
        #for (pid, name, desc, engvalunit, datacateg,
        #     raw_datacateg, active, system_element) in cursor:
        #    print("{} - {} - {} ({})".format(pid, name, desc, datacateg))
    
finally:
    connection.close()

    


