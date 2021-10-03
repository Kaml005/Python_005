import csv
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from datetime import datetime
import os
from ftplib import FTP

start = datetime.now()
date=20210331
FAM='citi'
B_id="SBEXEU_EUR"
z_date=str(date)
prev_date=str(date-1)

ftp = FTP('fts-adminftp.factset.com')
ftp.login('cand_bdf_qnt','2X$_9TE_38L$')
ftp.cwd('/datafeeds/benchmarks/')
#assigning file names to variables
confile_0 =FAM+'_const_'+z_date+'.txt'
confile_p =FAM+'_const_'+prev_date+'.txt'
idxfile_0=FAM+'_index_'+z_date+'.txt'
idxfile_p=FAM+'_index_'+prev_date+'.txt'

files=[confile_0,confile_p,idxfile_0,idxfile_p]

#files = ftp.nlst('k1_'+FAM+'_*20210211*.txt')
os.chdir("C:/Users/kannamalai/Downloads/DEXIA/CAND_BDF")
#download from ftp to cwd
for file in files:
        if not os.path.exists(file):
                print("Downloading..." + file)
                ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
        else:
                print("file exist")
ftp.quit()

#reading downloaded files to dataframes
df_0 = pd.read_csv(confile_0,delimiter="|")
df_p = pd.read_csv(confile_p,delimiter="|")
df_idx_0=pd.read_csv(idxfile_0,delimiter="|")
df_idx_p=pd.read_csv(idxfile_p,delimiter="|")
#Filtering 1 Index
PERF_0=df_0[df_0['BENCHMARK_ID']==B_id]
PERF_p=df_p[df_p['BENCHMARK_ID']==B_id]
PERF_I_0=df_idx_0[df_idx_0['BENCHMARK_ID']==B_id]
PERF_I_p=df_idx_p[df_idx_p['BENCHMARK_ID']==B_id]
#Merging Const on securityId without overwriting weight,NDs, Tr_net_1ds
PERF_0['TR_1D_GROSS_0']=PERF_0['TR_1D_GROSS']
PERF_p['W_nd']=PERF_p['WEIGHT_ND']
iloc=(PERF_I_0.index[0])
C_LEVEL=pd.DataFrame()
C_LEVEL=pd.merge(PERF_0,PERF_p,on='SECURITY_ID')
C_LEVEL['Wsum']=(C_LEVEL['W_nd']*C_LEVEL['TR_1D_GROSS_0']).fillna(0)
#C_LEVEL.to_excel('clevel.xlsx')
TOP_LEVEL=((PERF_I_0['TR_GROSS_IDX']/PERF_I_p['TR_GROSS_IDX']-1)*100)[iloc]
CONST_LEVEL=sum(C_LEVEL['Wsum'])/100
print('TOP_LEVEL:',TOP_LEVEL)
print('CONST_LEVEL:',CONST_LEVEL)
diff=(abs(TOP_LEVEL-CONST_LEVEL))
if diff<0.005:
    print("~*~*~ Rolls up ~*~*~")
    print(diff)
else:
    print(" Roll up Mismatch !!")
    print(diff)
