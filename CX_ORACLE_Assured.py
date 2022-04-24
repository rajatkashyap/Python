# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:13:51 2022

@author: U40MV02
"""

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

dsn_tns = cx_Oracle.makedsn('a2ec701c1-scan.us2.ocm.s7130945.oraclecloudatcustomer.com', '1521', service_name='SLRHOP1B.us2.ocm.s7130945.oraclecloudatcustomer.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'u40mv02', password='jan-2022', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
dsn_tns_PHDB= cx_Oracle.makedsn('a2ec701c1-scan.us2.ocm.s7130945.oraclecloudatcustomer.com', '1521', service_name='SLRPHDB.us2.ocm.s7130945.oraclecloudatcustomer.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn_PHDB = cx_Oracle.connect(user=r'u40mv02', password='jan-2022', dsn=dsn_tns_PHDB) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c_PHDB = conn_PHDB.cursor()
c_PHDB.execute('''
select ltrim(rtrim(p.POLICY_NUM)) POLICY_NUM, nb.ANNT_ZIP_CD,p.SURR_CHRG_DESC,p.PROD_DESC_CD, rf.FEATURE_OPT_NAME,RF.SCHEDULED_YEARS,RF.FEATURE_SCHEDULE,
        RF.SC_Yr_1,RF.SC_Yr_2,RF.SC_Yr_3,RF.SC_Yr_4,RF.SC_Yr_5,RF.SC_Yr_6,RF.SC_Yr_7,RF.SC_Yr_8,
        RF.SC_Yr_9,RF.SC_Yr_10,MVA,SRA_IND,PRODUCT_TYPE
      from POLICY p
left outer join
(select POLICY_NUM,ANNT_ZIP_CD from NEW_BUSINESS nb where ANNT_ZIP_CD is not null) nb
on p.POLICY_NUM=nb.POLICY_NUM
inner join
(select rf.FEATURE_OPT_NAME,STATUS,RF.SCHEDULED_YEARS,RF.FEATURE_SCHEDULE,PROD_CUSIP,
        (REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 1)/100) SC_Yr_1,(REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 2)/100) SC_Yr_2,
        (REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 3)/100) SC_Yr_3,(REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 4)/100) SC_Yr_4,
        (REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 5)/100) SC_Yr_5,(REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 6)/100) SC_Yr_6,
        (REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 7)/100) SC_Yr_7,(REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 8)/100) SC_Yr_8,
        (REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 9)/100) SC_Yr_9,(REGEXP_SUBSTR(Feature_SCH, '[^ ]+', 1, 10)/100) SC_Yr_10
       from
       (select rf.FEATURE_OPT_NAME,STATUS,RF.SCHEDULED_YEARS,RF.FEATURE_SCHEDULE,regexp_replace(FEATURE_SCHEDULE, '[-  %,]|\[|\]', ' ') Feature_SCH,PROD_CUSIP from rider_fee rf
        where  FEE_ID = '1008' AND SPEC_CODE = '10' and STATUS='A'
       )rf
 )
RF
on RF.PROD_CUSIP=P.PROD_DESC_CD
and  lower(ltrim(rtrim(p.SURR_CHRG_DESC)))=lower(ltrim(trim(RF.FEATURE_OPT_NAME)))
inner join PRODUCT pr on P.PROD_DESC_CD=PR.PROD_DESC_CD
where 
plan_cd in  ('133','134','137','138','139','166','167') and
--p.POLICY_NUM=nb.POLICY_NUM
p.SURR_CHRG_DESC!='N/A'
'''
)
df_PHDB=pd.DataFrame(c_PHDB)
df_PHDB.columns=[row[0] for row in c_PHDB.description]

dates=[('07/31/2021','08/31/2021'),('08/31/2021','09/30/2021'),('09/30/2021','10/31/2021')]
for date in dates:
    EOPP=date[0]
    EOP=date[1]
    c = conn.cursor()
    c.execute('''
    Select LTRIM(RTRIM(Nav.PC_CONT)) PC_CONT,Case when Nav.Company_Code = '7' then 'AGL'
                            when Nav.Company_Code = '9' then 'USL'
                            when Nav.Company_Code = '10' then 'VALIC' 
                      else NULL end as COMPANY_ALPHA,
          Nav.PLAN_CD,Nav.DOB,Nav.POL_ISS_DT,Nav.ZIP_CD,Nav.CUR_STATE,Nav.ISS_STATE,Nav.PRIORPERIODCASHVAL,Nav.PRIORPERPENFREEAMT,Nav.PRIORPERIODAV,Nav.CURRPERIODCASHVAL,Nav.CURRPERIODAV,Nav.GROSSFULLSURRAMT,
          Nav.DEATHCLAIMAMT,Nav.SYSWDAMT,Nav.MINDISTRAMT,Nav.ANNUITIZATIONAMT,Nav.PREMAMT,Nav.OTHERTRANSAMT,Nav.NOTTAKENAMT,Nav.TRMTHATSPENFREE,Nav.FULLSURRDATE,Nav.DEATHCLAIMDATE,Nav.SYSWDDATE,Nav.MINDISTRDATE,
          Nav.ANNUITIZATIONDATE,Nav.PREMDATE,Nav.OTHERTRANSDATE,Nav.NOTTAKENDATE,Nav.STATUS1,Nav.PLAN_TITLE,Nav.PRODUCT_DESC,
          Case when Nav.PC_QUALIFIED_FLG in ('1','14','16','-999') then 'NQ' 
               when Nav.PC_QUALIFIED_FLG not in ('1','14','16','-999') then 'Q'
                    else NULL end as QUALIFIED_FLG,
                    Nav.ANNUITANT_SEX, NAV.GrossPWDAmt, Nav.PWDDate,
                    '7' as Guar_Term_Yrs_1,
        '7' as Guar1Yr,
                    '1' as Guar2YR
                    ,Nav.PO_MIN_INT_RATE
                    ,Nav.PO_FXD_INT_RATE
                    ,'SPDA' as product_type,
                     Nav.PC_BROKER_DEALER_NAME_ID as Agengy_ID,
                    Nav.Company_Name as Agency_name,
                   
                   BOPCreditedRate, EOPCreditedRate,
                                  Nav.DEATHCLAIMAMT as CorrectedDeathClaim,
                    NAV.GrossPWDAmt as CorrectedPWDAmt,
                    Nav.Company_Name as CorrectedAgencyName ,
                   PO_GLB_BENEFIT_START_DATE as Income_Activation_Date,
                   GLIA.Initial_GLIA_Base as Initial_Eligible_Premium,
                   GLIA.Current_GLIA_Amount as CURRENT_GLIA_AMOUNT,
                   GLIA.Initial_GLIA_Percent as Initial_Income_Percentage,
                     GLIA.Current_GLIA_Percent as CURRENT_Income_Percentage,
                     GLIA.Roll_Up_Percent as ROLL_UP_PERCENTAGE
                    
                   
    from
    (                 
    Select PC_POL_NUM POL_NBR,PC_CONT,PC_STATUS STATUS1,SA_LIFECAD_DESC Pol_Status,PC_PLN_CODE PLAN_CD,PC_DOB_PRIM DOB,PC_ISSUE_DATE POL_ISS_DT,PC_TERM_DATE,PC_FLOOK_DATE,PC_RES_ZIP ZIP_CD,
    PC_CONT_STATE_CODE CUR_STATE,PC_STATE_CODE ISS_STATE,PC_POL_DATE,PC_SEX_PRIM ANNUITANT_SEX,PC_QUALIFIED_FLG,QU_QUAL_DESC,PC_CO_ID Company_Code,PC_BROKER_DEALER_NAME_ID,T_LINC_NAME_COMPANY.NC_COMPANY_NAME Company_Name,PL_FORM PLAN_TITLE,PL_PRD_DESC PRODUCT_DESC,Val.PriorPeriodAV,Val.PriorPeriodCashVal,Val.PriorPerPenFreeAmt,Val.CurrPeriodAV,Val.CurrPeriodCashVal,Val.CurrPerPenFreeAmt,
          
           PO_MIN_INT_RATE,PO_FXD_INT_RATE,
           Trans.GrossFullSurrAmt,Trans.PremAmt,Trans.SysWDAmt,Trans.MinDistrAmt,Trans.DeathClaimAmt,Trans.AnnuitizationAmt,Trans.NotTakenAmt,Trans.TRMThatsPenFree,Trans.OtherTransAmt,
           Trans.FullSurrDate,Trans.PremDate,Trans.SysWDDate,Trans.MinDistrDate,Trans.DeathClaimDate,Trans.AnnuitizationDate,Trans.NotTakenDate,Trans.OtherTransDate, Trans.GrossPWDAmt, Trans.PWDDate --RF_EXTERNAL_ID,AG_AGENCY,
           ,BOPCreditedRate, EOPCreditedRate,PL_MKTG_NUM,PO_GLB_BENEFIT_START_DATE
    from T_LIPC_POLICY_COMMON 
    left outer join T_LIPL_PLAN on T_LIPC_POLICY_COMMON.PC_PLN_CODE = T_LIPL_PLAN.PL_PLN_CODE
    --left outer join T_CRRF_RIDER_FEE on RF_PROD_CUSIP = PL_MKTG_NUM
    left outer join T_LIQU_QUALIFIED on T_LIPC_POLICY_COMMON.PC_QUALIFIED_FLG = T_LIQU_QUALIFIED.QU_QUAL_CODE
    left outer join T_LINC_NAME_COMPANY on T_LIPC_POLICY_COMMON.PC_BROKER_DEALER_NAME_ID = T_LINC_NAME_COMPANY.NC_NAME_ID
    Left outer join T_LISA_STATUS on T_LIPC_POLICY_COMMON.PC_STATUS = T_LISA_STATUS.sa_status
    --left outer join T_ANLH_LOAN_HEADER  on T_ANLH_LOAN_HEADER.LH_POL_NUM= T_LIPC_POLICY_COMMON.PC_POL_NUM --Current credited interest rates
    inner join T_ANPO_POLICY  on T_ANPO_POLICY.PO_POL_NUM= T_LIPC_POLICY_COMMON.PC_POL_NUM --GMIR
    
    left outer join
    (
    select FV_POL_NUM,
    max(case when FV_VALUATION_DATE = to_date(:1,'MM/DD/YYYY') then FV_INT_RATE/100 end) as BOPCreditedRate,
                    max(case when FV_VALUATION_DATE = to_date(:2,'MM/DD/YYYY') then FV_INT_RATE/100 end) as EOPCreditedRate
    
                    
    from  T_LIFV_SUN_FIX_DPST_VALUATION 
    --on T_LIPC_POLICY_COMMON.PC_POL_NUM=T_LIFV_SUN_FIX_DPST_VALUATION.FV_POL_NUM
    where FV_VALUATION_DATE >= to_date(:1,'MM/DD/YYYY') AND FV_VALUATION_DATE <=to_date(:2,'MM/DD/YYYY')--and FV_POL_NUM='3313213'
    
    group by FV_POL_NUM
    )CreditedRate
    on T_LIPC_POLICY_COMMON.PC_POL_NUM=CreditedRate.FV_POL_NUM
    
    left outer join
    (Select TC_POL_NUM,
           Max(Case when TC_TXN_TYPE in ('59')then TC_TXN_DATE else NULL end) as AnnuitizationDate,
           Max(Case when TC_TXN_TYPE in ('22','66','1017','194','195')then TC_TXN_DATE else NULL end) as DeathClaimDate,
           Max(Case when TC_TXN_TYPE in ('21')then TC_TXN_DATE else NULL end) as FullSurrDate,
           Max(Case when TC_TXN_TYPE in ('1','6','7','1001')then TC_TXN_DATE else NULL end) as PremDate,
    
           Max(Case when TC_TXN_TYPE in ('1006','1009') or (TC_TXN_TYPE = '5' and T_LIPC_POLICY_COMMON.PC_FLOOK_DATE <= T_LIPC_POLICY_COMMON.PC_TERM_DATE) then TC_TXN_DATE else NULL end) as NotTakenDate,
           Max(Case when TC_TXN_TYPE in ('11')then TC_TXN_DATE else NULL end) as SysWDDate,
           Max(Case when TC_TXN_TYPE in ('44')then TC_TXN_DATE else NULL end) as MinDistrDate,
           Max(Case when TC_TXN_TYPE not in ('18','44','59','22','66','1017','21','1','6','7','1001','1006','11','5','1009','194','195','170')then TC_TXN_DATE else NULL end) as OtherTransDate,
           Max(Case when TC_TXN_TYPE in ('18','170')then TC_TXN_DATE else NULL end) as PWDDate,
    
           Sum(Case when TC_TXN_TYPE in ('18','170')then TC_TOTAL else NULL end)*-1 as GrossPWDAmt,
           Sum(Case when TC_TXN_TYPE in ('59')then TC_TOTAL else NULL end) as AnnuitizationAmt,
           Sum(Case when TC_TXN_TYPE in ('22','66','1017','194','195')then TC_TOTAL else NULL end)*-1 as DeathClaimAmt,
           Sum(Case when TC_TXN_TYPE in ('21')then TC_TOTAL else NULL end)*-1 as GrossFullSurrAmt,
           Sum(Case when TC_TXN_TYPE in ('1','6','7','1001')then TC_TOTAL else NULL end) as PremAmt,
           Sum(Case when TC_TXN_TYPE in ('1006','1009' ) or (TC_TXN_TYPE = '5' and T_LIPC_POLICY_COMMON.PC_FLOOK_DATE <= T_LIPC_POLICY_COMMON.PC_TERM_DATE) then TC_TOTAL else NULL end) as NotTakenAmt,
           Sum(Case when TC_TXN_TYPE in ('11')then TC_TOTAL else NULL end)*-1 as SysWDAmt,
           Sum(Case when TC_TXN_TYPE in ('44')then TC_TOTAL else NULL end)*-1 as MinDistrAmt,
                Sum(Case when TC_TXN_TYPE in ('5') and T_LIPC_POLICY_COMMON.PC_FLOOK_DATE > T_LIPC_POLICY_COMMON.PC_TERM_DATE then TC_TOTAL else NULL end)*-1 as TRMThatsPenFree,
           Sum(Case when TC_TXN_TYPE not in ('18','44','59','22','66','1017','21','1','6','7','1001','1006','11','5','1009','194','195','170')then TC_TOTAL else NULL end)*-1 as OtherTransAmt
    from T_LITC_TRANSACTION_COMMON
    left outer join T_LIPC_POLICY_COMMON
    on T_LITC_TRANSACTION_COMMON.TC_POL_NUM = T_LIPC_POLICY_COMMON.PC_POL_NUM
    where TC_TXN_STATUS='D' and TC_TXN_DATE > to_date(:1,'MM/DD/YYYY') AND TC_TXN_DATE <=to_date(:2,'MM/DD/YYYY')
    group by TC_POL_NUM
    ) Trans
    on T_LIPC_POLICY_COMMON.PC_POL_NUM = Trans.TC_POL_NUM                                                      
    left outer join
    (
    Select PV_POL_NUM,
           Sum(case when PV_VALUATION_DATE = to_date(:1,'MM/DD/YYYY')then (PV_FIX_ACCT_VALUE+PV_VAR_ACCT_VALUE) else 0 end) as PriorPeriodAV,
           Sum(case when PV_VALUATION_DATE = to_date(:1,'MM/DD/YYYY')then (PV_FIX_CASH_VALUE + PV_VAR_CASH_VALUE) else 0 end) as PriorPeriodCashVal,
           Sum(case when PV_VALUATION_DATE = to_date(:1,'MM/DD/YYYY')then ((PV_FIX_ACCT_VALUE+PV_VAR_ACCT_VALUE)-(PV_FIX_CASH_VALUE+PV_VAR_CASH_VALUE)+PV_MVA) else 0 end) as PriorPerPenFreeAmt,
           Sum(case when PV_VALUATION_DATE = to_date(:2,'MM/DD/YYYY')then (PV_FIX_ACCT_VALUE+PV_VAR_ACCT_VALUE) else 0 end) as CurrPeriodAV,
           Sum(case when PV_VALUATION_DATE = to_date(:2,'MM/DD/YYYY')then (PV_FIX_CASH_VALUE + PV_VAR_CASH_VALUE) else 0 end) as CurrPeriodCashVal,
           Sum(case when PV_VALUATION_DATE = to_date(:2,'MM/DD/YYYY')then ((PV_FIX_ACCT_VALUE+PV_VAR_ACCT_VALUE)-(PV_FIX_CASH_VALUE+PV_VAR_CASH_VALUE)+PV_MVA) else 0 end) as CurrPerPenFreeAmt
           from T_LIPV_SUN_POLICY_VALUATION
    where PV_VALUATION_DATE >= to_date(:1,'MM/DD/YYYY')  AND  PV_VALUATION_DATE <=to_date(:2,'MM/DD/YYYY')
    group by PV_POL_NUM
    )Val
    on T_LIPC_POLICY_COMMON.PC_POL_NUM = Val.PV_POL_NUM
    where PC_STATUS in ('#') and pc_pln_code in ('133','134','137','138','139','166','167') 
    and PC_ISSUE_DATE <=to_date(:2,'MM/DD/YYYY')
    
    
    order by T_LIPC_POLICY_COMMON.PC_POL_NUM
    )Nav
    left outer join
    (select distinct 
      pc.pc_cont as Policy_Number,
      pl.pl_prd_desc as Product_Name,
      pc.pc_pol_date as Issue_Date,
      po_glb_benefit_start_date as Income_Activation_Date,
      i_tl.tl_glia_base as Initial_GLIA_Base,
      i_tl.tl_glwb_glia_amount as Initial_GLIA_Amount,
      i_tl.tl_glwb_glia_percent as Initial_GLIA_Percent,
      case when pl_prd_desc not like '%NY%' then i_tl.tl_glwb_income_growth_percent
      else 
     -- l_tl.tl_glwb_glia_percent end as Roll_Up_Percent,
     NULL end as Roll_Up_Percent,
      l_tl.tl_glwb_glia_amount as Current_GLIA_Amount,
      l_tl.tl_glwb_glia_percent as Current_GLIA_Percent,
      l_tl.tl_glia_base as Current_GLIA_Base
     -- tc3.tc_txn_date as Withdrawal_Date
     -- tc3.tc_total as Withdrawal_Amount
      
    from 
      t_lipc_policy_common pc join (
      select max(tc_txn_num) as i_tc_txn_num, tc_pol_num as i_tc_pol_num
      from t_litc_transaction_common tc 
      where tc.tc_txn_type in (1, 7, 63) and
      tc.tc_txn_status = 'D'
      group by tc.tc_pol_num
      ) on i_tc_pol_num = pc_pol_num join t_antl_transaction_log i_tl
      on i_tl.tl_txn_num = i_tc_txn_num join (
      select max(tc_txn_num) as l_tc_txn_num, tc_pol_num as l_tc_pol_num
      from t_litc_transaction_common tc2
      where 
      tc2.tc_txn_status = 'D'
      group by tc2.tc_pol_num
      ) on l_tc_pol_num = pc_pol_num join t_antl_transaction_log l_tl
      on l_tl.tl_txn_num = l_tc_txn_num,
      t_lipl_plan pl,
      t_anpo_policy po left join t_litc_transaction_common tc3 on
      tc3.tc_pol_num = po_pol_num and tc3.tc_txn_status = 'D' and 
      tc3.tc_txn_type in (11, 18, 44, 155, 166, 170, 178)
    
    where 
      pc_status not in ('D','C','G','W', 'P','t','S','=') and 
      pl_prd_desc like 'Assured%' and
      pc_pln_code = pl_pln_code and 
      po.po_pol_num = pc_pol_num 
        )GLIA
      on
      NAV.PC_CONT=GLIA.Policy_Number
    
    '''
    ,(EOPP,EOP)
    
    ) # use triple quotes if you want to spread your query across multiple lines
    
    
    
    df=pd.DataFrame(c)
    df.columns=[row[0] for row in c.description]
    
    assured_all=pd.merge(df,df_PHDB,left_on='PC_CONT',right_on='POLICY_NUM',how='left')
    #print(type(assured_all['PC_CONT'].tolist()))
    print (len(assured_all))
    #print (assured_all['PC_CONT'].tolist())
    cnx=pyodbc.connect("DRIVER={SQL Server};SERVER=PWSADSEXPSTUD03;DATABASE=ExpAnnuity;Trusted_Connection=yes")
    cursor=cnx.cursor()
    for i in range(len(assured_all)):
        cursor.execute('''INSERT INTO [ExpAnnuity].[ESU].[WNL-FSA_Temp] ([POL_NBR]) values(?)''',[assured_all['PC_CONT']])
    

#print (c.description)
for row in c:
     print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.


#print (df_PHDB)

conn.close()
conn_PHDB.close()
#cnx.commit()
#cnx.close()