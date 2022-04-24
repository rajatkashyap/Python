from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='rajat',host='127.0.0.1',database='db')
cursor = cnx.cursor()								
query=("select * from jobs")
cursor.execute(query)
for (city_id,city_name,country_id,x) in cursor:
	print  city_id,city_name,country_id
cnx.close()
