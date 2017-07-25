import pymysql

#databse credentials
host='localhost'
port=3306
user='root'
passwd=''
db='plantdb'

class main:

	conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
	cur = conn.cursor()
	print("database ready")

	def getdescription(self,plantname):
		command = "SELECT other_names from plantdetails WHERE id="+str(plantname)
		try:
			main.cur.execute(command)
			data=main.cur.fetchone()
			data=data[0]
			return data
		except:
			return "Error2" #invalid SQL command

	def getname(self,plantname):
		command = "SELECT name from plantdetails WHERE id="+str(plantname)
		try:
			main.cur.execute(command)
			data=main.cur.fetchone()
			data=data[0]
			return data
		except:
			return "Error2" #invalid SQL command

	def closedatabase(self):
		main.cur.close()
		main.conn.close()
		print("database closed")
		return True

	def getall(self,position):
		command ="SELECT * FROM plantdetails WHERE id ="+str(position)
		main.cur.execute(command)
		data=main.cur.fetchone()
		return data

