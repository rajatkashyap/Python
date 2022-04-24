from mysql.connector import (connection)
import datetime
cnx = connection.MySQLConnection(user='root', password='rajat',host='127.0.0.1',database='db')
cursor = cnx.cursor()								
#query=("create table Likes (date_posted DATE,post_id INT, device VARCHAR(20),activity VARCHAR(10))")
query=("delete from likes")
cursor.execute(query)
cnx.commit()
f=open("Likes.txt")
for line in f:
	data=line.strip().split("\t")
	date,post,device,like=data
	d=datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%Y-%m-%d')
	#query1="insert  into likes values(STR_TO_DATE('%s','\%d/\%m/\%Y'),'%s','%s','%s')" %(date,post,device,like)
	query1="insert  into likes values('%s','%s','%s','%s')" %(d,post,device,like)
	cursor.execute(query1)
	cnx.commit()

q2="select date_posted, sum(case when device in ('Nexus','Non-Nexus') then 1 else 0 end )Android,sum(case when device in ('Nexus','Non-Nexus','iOS') then 1 else 0 end)Phone,sum(case when device='Web' then 1 else 0 end )web,count(*)all_d from likes group by date_posted"
cursor.execute(q2)
print 'Date\t\tAndriod\tPhone\tWeb\tAll'
for (d,a,p,w,e) in cursor:
	print d,'\t',a,'\t',p,'\t',w,'\t',e

	