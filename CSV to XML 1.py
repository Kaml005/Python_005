import csv
import os

os.chdir("C:/Users/kannamalai/Downloads/DEXIA/")
csvFile = 'BSFI_EU_INDEX_20201104.xml.csv'
xmlFile = 'T_BSFI_EU_INDEX_20201104.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<FactSet>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            print(tags[i])
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<data>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</data>' + "\n")
            
    rowNum +=1

xmlData.write('</FactSet>' + "\n")
xmlData.close()
