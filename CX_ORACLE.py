# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:06:31 2021

@author: U40MV02
"""

import cx_Oracle
import pandas as pd

import pyodbc

cnx=pyodbc.connect("DRIVER={SQL Server};SERVER=PWSADSEXPSTUD03;DATABASE=ExpAnnuity;Trusted_Connection=yes")
cursor=cnx.cursor()

dsn_tns = cx_Oracle.makedsn('a2ec701c1-scan.us2.ocm.s7130945.oraclecloudatcustomer.com', '1521', service_name='SLRPWH.us2.ocm.s7130945.oraclecloudatcustomer.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'ACTUARY_REPORT', password='C0ldst0ne1', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
EOPP='07/31/2021'
EOP='08/31/2021'
c = conn.cursor()
c.execute('''
SELECT t1.COMPANY_ALPHA, 
          t1.POL_NBR, 
          --t1.ACCUM_VAL, 
          --t1.CASH_SURR_VAL, 
          --t1.PENALTY_FREE_AMT, 
          --t1.COMPOSITE_INT_RATE,
          sum(case when  t1.AS_OF_DT = to_date('07/31/2021','MM/DD/YYYY') then CASH_SURR_VAL else 0 end) as PriorPeriodCashVal,
          sum(case when  t1.AS_OF_DT = to_date('07/31/2021','MM/DD/YYYY') then PENALTY_FREE_AMT else 0 end) as PriorPerPenFreeAmt ,
          sum(case when  t1.AS_OF_DT = to_date('07/31/2021','MM/DD/YYYY') then ACCUM_VAL else 0 end) as PriorPeriodAV  ,
          sum(case when  t1.AS_OF_DT = to_date('07/31/2021','MM/DD/YYYY') then COMPOSITE_INT_RATE else 0 end) as  BOPCreditedRate  ,  
         
          sum(case when  t1.AS_OF_DT = to_date('08/31/2021','MM/DD/YYYY') then CASH_SURR_VAL else 0 end) as CurrPeriodCashVal ,
          sum(case when  t1.AS_OF_DT = to_date('08/31/2021','MM/DD/YYYY') then ACCUM_VAL else 0 end) as CurrPeriodAV   ,
          sum(case when  t1.AS_OF_DT = to_date('08/31/2021','MM/DD/YYYY') then COMPOSITE_INT_RATE else 0 end) as  EOPCreditedRate,
          :1,
          :2
      FROM DW_ADMIN.POLICY_AS_OF t1
     WHERE 
 t1.AS_OF_DT >= to_date(:1,'MM/DD/YYYY') AND
t1.AS_OF_DT <= to_date(:2,'MM/DD/YYYY')  AND  t1.COMPANY_ALPHA ='VAA' 
and POL_NBR in ('FL002790','FL002795')
group by 
    t1.COMPANY_ALPHA, 
          t1.POL_NBR      
'''
,(EOPP,EOP)

) # use triple quotes if you want to spread your query across multiple lines


'''
df=pd.DataFrame(c)
df.columns=[row[0] for row in c.description]

print (df)'''
result=c.fetchall()
print (result)
cnx=pyodbc.connect("DRIVER={SQL Server};SERVER=PWSADSEXPSTUD03;DATABASE=ExpAnnuity;Trusted_Connection=yes")
cursor=cnx.cursor()

cursor.executemany("""
        insert into  [ExpAnnuity].[ESU].POLICY_AS_OF_PWH values(?,?,?,?,?,?,?,?,?,?,?)""", result)

    
'''print (c.description)
for row in c:
     print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
'''
conn.close()
cnx.commit()
cnx.close()