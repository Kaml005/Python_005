import csv
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from datetime import datetime
import os
start = datetime.now()
os.chdir("C:/Users/kannamalai/Downloads/DEXIA/")
csvFile = 'T_BSFI_EU_INDEX_20201104.csv'
xmlFile = 'BSFI_US1_CONST_20201103.xml'

tree = ET.parse(xmlFile)
root = tree.getroot()
columns=["BENCHMARK_ID","ISIN","WEIGHT"]
data=[]
for tag in root:
    for sub in tag:
##Selcet Index
        if sub.get('BENCHMARK_ID')=="LHMN31890_EUR":
            for key,value in sub.attrib.items():
                for col in columns:
                    if col==key:
                        data.append(value)
                        #print(data)
                    else:
                        pass
        else:
            pass

print(data)
df = pd.DataFrame(data,columns)
df=df.transpose()
print(df)
df.to_csv("test.csv",index=False)
end = datetime.now()
diff = end - start
print('Code executed for ' + str(diff.seconds) + 's')

##        x=((subtag.attrib.keys()))
##        y=((subtag.attrib.values()))
##        print(x,y)
##        
##csvData = csv.reader(open(csvFile))
##xmlData = open(xmlFile, 'w')
##xmlData.write('<?xml version="1.0"?>' + "\n")
### there must be only one top-level tag
##xmlData.write('<FactSet>' + "\n")
##
##rowNum = 0
##for row in csvData:
##    if rowNum == 0:
##        tags = row
##        # replace spaces w/ underscores in tag names
##        for i in range(len(tags)):
##            tags[i] = tags[i].replace(' ', '_')
##    else: 
##        xmlData.write('<entry>' + " ")
##        for i in range(len(tags)):
##            xmlData.write('    ' + tags[i] +'="'\
##                          +row[i]+'" ' +"\n")
##        xmlData.write('</entry>' + "\n")
##            
##    rowNum +=1
##
##xmlData.write('</FactSet>' + "\n")
##xmlData.close()
