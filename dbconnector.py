import pymysql

#databse credentials
host='localhost'
port=3306
user='root'
passwd=''
db='plantdb'


conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)

cur = conn.cursor()

cur.execute("SELECT * FROM plantdetails")

print(cur.description)


cur.close()
conn.close()