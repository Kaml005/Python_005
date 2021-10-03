import os
from statistics import mean
import pandas as pd
#from os import listdir
from os.path import isfile, join
import numpy as np

#directories for base file, new file, and output summary

bdfpath = 'C:\\Users\\kannamalai\\Downloads\\asi_conv\\BDF\\'
legacypath = 'C:\\Users\\kannamalai\\Downloads\\asi_conv\\legacy\\'
summarypath = 'C:\\Users\\kannamalai\\Downloads\\ASI_CONV\\Results\\'
wd="C:/Users/kannamalai/Downloads/ASI_CONV/BDF/"
var = 'emucp.dat'
filename_1 = os.path.join(bdfpath,var)
filename_2 = os.path.join(legacypath,var)
summary_path = os.path.join(summarypath,var) #must already exist
summary_name = 'diff_test_summary.txt' #does not need to already exist

file_1 = pd.read_csv(filename_1,sep='|')

file_2 = pd.read_csv(filename_2,sep='|')

#columns that don't match
col_list = []
join_files = file_1.set_index('c').join(file_2.set_index('c'),lsuffix='_1',rsuffix='_2')
for col in file_1.columns:
    if col=='c':
        pass
    else:  
        try:
            column_compare = join_files[[col+'_1',col+'_2']]
            X=((abs(mean(column_compare[col+'_1'])-mean(column_compare[col+'_2'])))<0.05)
            Y=mean(column_compare[col+'_1'])
            #print(Y)
        except TypeError:
            X='False'
            Y=0
    print(Y)
    if X:
        pass
    elif column_compare[col+'_1'].equals(column_compare[col+'_2']):
        pass
    else:
        col_list.append(col)
    
#writes diffs to a text file for each field - warning given below is fine, ignore
for col in col_list:
            col_data = join_files[[col+'_1',col+'_2']]
            col_data['match'] = col_data[col+'_1']==col_data[col+'_2']
            col_data['BDF_populated'] = pd.notna(col_data[col+'_1'])
            col_data['Legacy_populated'] = pd.notna(col_data[col+'_2'])    
            try:
                col_data['num_diff'] = abs(col_data[col+'_1']-col_data[col+'_2'])
                col_data['match'] = abs(col_data[col+'_1']-col_data[col+'_2'])<0.05
            except TypeError: col_data['num_diff'] = "string/Na"
            col_data[col_data['match']==False].to_csv(summary_path+'\\'+col+'.txt',sep='|')
