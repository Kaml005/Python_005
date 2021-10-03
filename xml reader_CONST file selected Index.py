from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from datetime import datetime
import os

start = datetime.now()
print(start)
os.chdir("C:/Users/kannamalai/Downloads/DEXIA/")
file_name=('BSFI_US_CONST_20210129.xml')
doc = ET.parse(file_name)
root = doc.getroot()
root2=root.tag
columns=["BENCHMARK_ID","SECURITY_ID","ISIN","FAMILY_ID","DATE","WEIGHT","WEIGHT_ND","QUANTITY","FDS_EXCHANGE_RATE","MCAP","PR_1D","TR_1D_GROSS","TR_1D_NET","MCAP_LOC","PR_1D_LOC","TR_1D_GROSS_LOC","TR_1D_NET_LOC","CTMD","FDS_FIGI_SECURITY","FDS_FIGI_COMPOSITE","FDS_FIGI_LISTING"]
data=[]
df = pd.DataFrame(data,columns=["BENCHMARK_ID","SECURITY_ID","ISIN","FAMILY_ID","DATE","WEIGHT","WEIGHT_ND","QUANTITY","FDS_EXCHANGE_RATE","MCAP","PR_1D","TR_1D_GROSS","TR_1D_NET","MCAP_LOC","PR_1D_LOC","TR_1D_GROSS_LOC","TR_1D_NET_LOC","CTMD","FDS_FIGI_SECURITY","FDS_FIGI_COMPOSITE","FDS_FIGI_LISTING"])

for main in root:#FactSet
    for sub in main:
        if sub.get('BENCHMARK_ID')=="LHMN0038_EUR":
            data=(sub.attrib)
            df=df.append(data,ignore_index=True)
        else:
            pass
        
df.to_csv(file_name+".csv", index=False)
end = datetime.now()
diff = end - start
print('Code executed for ' + str(diff.seconds) + 's')
