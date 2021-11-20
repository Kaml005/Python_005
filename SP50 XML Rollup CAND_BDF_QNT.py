import csv
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from datetime import datetime
import os
from ftplib import FTP

start = datetime.now()
date=str(20210211)
prev_date=str(20210210)
FAM='spus'
ftp = FTP('****.com')
ftp.login('*****','****')
ftp.cwd('/datafeeds/benchmarks/')
files=[FAM+'_index_'+date+'.xml',
       FAM+'_index_'+prev_date+'.xml',
       FAM+'_const_'+date+'.xml',
       FAM+'_const_'+prev_date+'.xml']

#files = ftp.nlst('k1_'+FAM+'_*20210211*.xml')
os.chdir("C:/Users/kannamalai/Downloads/DEXIA/CAND_BDF")

for file in files:
        if not os.path.exists(file):
                print("Downloading..." + file)
                ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
        else:
                print("file exist")
ftp.quit()

confile_0 =FAM+'_CONST_'+date+'.xml'
confile_p =FAM+'_CONST_'+prev_date+'.xml'
idxfile_0=FAM+'_INDEX_'+date+'.xml'
idxfile_p=FAM+'_INDEX_'+prev_date+'.xml'

rollup=[confile_0,confile_p,idxfile_0,idxfile_p]
df_r = pd.DataFrame()
df_w = pd.DataFrame()
PERF=pd.DataFrame()
for file in rollup:
    tree = ET.parse(file)
    root = tree.getroot()
    for tag in root:#data
        for sub in tag:#each entry
##Selcet Index in below line:
            if sub.get('BENCHMARK_ID')=="SP50_USD":
                if file==confile_0:
                    df_r=df_r.append({'ISIN':sub.get('ISIN'),'TR_1D_NET':sub.get('TR_1D_NET')},ignore_index=True)
                elif file==confile_p:
                    df_w=df_w.append({'ISIN':sub.get('ISIN'),'WEIGHT_ND':sub.get('WEIGHT_ND')},ignore_index=True)
                elif file==idxfile_0:
                    tr_0=float(sub.get('TR_NET_IDX'))
                else:
                    tr_p=float(sub.get('TR_NET_IDX'))
            else:
                pass
PERF=pd.merge(left=df_w, right=df_r, left_on='ISIN', right_on='ISIN')
PERF['WEIGHT_ND']=PERF['WEIGHT_ND'].astype(float)
PERF['TR_1D_NET']=PERF['TR_1D_NET'].astype(float)
CONST_LEVEL=sum(PERF['TR_1D_NET']*PERF['WEIGHT_ND'])/100
##print('tr_0:',tr_0)
##print('tr_p:',tr_p)
print('TOP_LEVEL:',(tr_0/tr_p-1)*100)
print('CONST_LEVEL:',CONST_LEVEL)
diff=(abs((tr_0/tr_p-1)*100-CONST_LEVEL))
if diff<0.005:
    print("~*~*~ Rolls up ~*~*~")
    print(diff)
else:
    print(" Roll up Mismatch !!")
    print(diff)
##PERF.to_csv("SP_PERF2.csv",index=False)
##end = datetime.now()
##diff = end - start
##print('Code executed for ' + str(diff.seconds) + 's')
