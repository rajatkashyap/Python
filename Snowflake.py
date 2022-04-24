# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:56:25 2021

@author: U40MV02
"""

import snowflake.connector
import pandas as pd
conn = snowflake.connector.connect(
                user='Rajat.Kashyap@aig.com',
                #password='',
                account='aig.us-east-1',
                warehouse='WH_IM_GP_XS',
                database='IM_DEV',
                schema='UK_PENSIONS_CUR',
                role='RL_IM_DEV_UK_PENSIONS_CUR_RO',
                authenticator='externalbrowser'#'https://aigtech.okta.com'
                                )
cur = conn.cursor()
cur.execute('select * from EXPERIENCE_STUDY_TEST_TABLE')
result=cur.fetchall()
df=pd.DataFrame(cur)
'''df.columns=[row[0] for row in cur.description]'''
print (df)