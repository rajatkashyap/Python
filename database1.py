import pyodbc

cnx=pyodbc.connect("DRIVER={SQL Server};SERVER=PWSADSEXPSTUD03;DATABASE=ExpAnnuity;Trusted_Connection=yes")
cursor=cnx.cursor()
sql_comm='''SELECT top 100 [POL_NBR],[COMPANY_ALPHA],[PRODUCT_CD] 
FROM [ExpAnnuity].[ESU].[WNL-FSA]'''
cursor.execute(sql_comm) 
#print (cursor.fetchall())
print (len(cursor.fetchall()))
#or pol_nbr,c,a in cursor:
        #print (a,c)
        
cnx.close()