#reads all content of xml file and writes to csv
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from datetime import datetime
import os

start = datetime.now()
os.chdir("C:/Users/kannamalai/Downloads/DEXIA/")
file_name=('BSFI_EU_INDEX_20201105.xml')
doc = ET.parse(file_name)
root = doc.getroot()
root2=root.tag
columns=["BENCHMARK_ID","NAME_IDX","FAMILY_ID","DATE","CURRENCY_IDX","MCAP_IDX","CONST_IDX","PRICE_IDX","TR_GROSS_IDX","TR_NET_IDX","INTEREST_RATE"," MD","DURATION","YTM","MATURITY"]
data=[]
df = pd.DataFrame(data,columns=["BENCHMARK_ID","NAME_IDX","FAMILY_ID","DATE","CURRENCY_IDX","MCAP_IDX","CONST_IDX","PRICE_IDX","TR_GROSS_IDX","TR_NET_IDX","INTEREST_RATE"," MD","DURATION","YTM","MATURITY"])
for main in root:#FactSet
    for sub in main:
        data=((sub.attrib))
        print(data)
        df=df.append(data,ignore_index=True)    

df.to_csv(file_name+".csv", index=False)
end = datetime.now()
diff = end - start
print('Code executed for ' + str(diff.seconds) + 's')
