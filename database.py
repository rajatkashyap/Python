import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PWSADSEXPSTUD03;DATABASE=ExpAnnuity;trusted_connection=yes')
cursor = cnxn.cursor()
sql_comm='''SELECT top 100 [POL_NBR],[COMPANY_ALPHA],[PRODUCT_CD] 
FROM [ExpAnnuity].[ESU].[WNL-FSA]'''
cursor.execute(sql_comm) 
print cursor.fetchall()
#print type(s)

print cursor.fetchall()
#cursor.seek()
for row in cursor.fetchall():
    print row[0]
for POL_NBR in cursor:
	print POL_NBR
 
cursor.execute(sql_comm)
for (POL_NBR,COMPANY_ALPHA,PRODUCT_CD) in cursor:
	print  POL_NBR,PRODUCT_CD
	
cnxn.close()