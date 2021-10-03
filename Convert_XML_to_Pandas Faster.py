

#This is an example of how to convert an XML file where nodes have multiple attirbutes into a panda, using D2_CITI_C_CONST_20210301.xml as an example.
#The D2_CITI_C_CONST_20210301.xml was saved to my current working directory (CWD).
#Please note, there are many ways to parse, use and convert XML in python.

import pandas as pd                                       #Import pandas for dataframe
import xml.etree.ElementTree as ET                        #Python library that reads XML files.
root = ET.parse('D2_CITI_C_CONST_20210301.xml').getroot() #Getting root in xml file

test = []                                       #Creating a list to reference in the dataframe

for type_tag in root.findall('data/entry'):     #Retireving tags form the child element containig data i.e. the "entry" element
    idx    = type_tag.get('BENCHMARK_ID')       #Each tag  represents an attribute in the XML file i.e. the Benhcmark_ID tag refers to BENCHAMRK_ID
    sec_id = type_tag.get('SECURITY_ID')        #You can pull out and manipulate each tag indiviudally.
    isin   = type_tag.get('ISIN')
    fam_id = type_tag.get('FAMILY_ID')
    date   = type_tag.get('DATE')
    weight = type_tag.get('WEIGHT')
    w_nd   = type_tag.get('WEIGHT_ND')
    quant  = type_tag.get('QUANTITY')
    fds_fx = type_tag.get('FDS_EXCHANGE_RATE')
    mcap   = type_tag.get('MCAP')
    pr_1d  = type_tag.get('PR_1D')
    gr_1d  = type_tag.get('TR_1D_GROSS')
    nt_1d  = type_tag.get('TR_1D_NET')
    mcap_l = type_tag.get('MCAP_LOC')
    pr_1dl = type_tag.get('PR_1D_LOC')
    tr_1dl = type_tag.get('TR_1D_GROSS_LOC')
    nt_1dl = type_tag.get('TR_1D_NET_LOC')
    ctmd   = type_tag.get('CTMD')
    id_fig = type_tag.get('FDS_FIGI_SECURITY')
    cp_fig = type_tag.get('FDS_FIGI_COMPOSITE')
    li_fig = type_tag.get('FDS_FIGI_LISTING')

    # Creating a list within a list
    test.append([idx,sec_id,isin,fam_id,date,weight,w_nd,quant,fds_fx,mcap,pr_1d,gr_1d,nt_1d,mcap_l,pr_1dl,tr_1dl,nt_1dl,ctmd,id_fig,cp_fig,li_fig])

#Inputting data into dataframe
df=pd.DataFrame(test)
#Namming columns inside the dataframe
df.columns = ('BENCHMARK_ID','SEC_ID','ISIN','FAMILY_ID','DATE','WEIGHT','WEIGHT_ND','QUANTITY','FDS_EXCHANGE_RATE','MCAP','PR_1D','TR_1D_GROSS','TR_1D_NET','MCAP_LOC',
              'PR_1D_LOC','TR_1D_GROSS_LOC','TR_1D_NET_LOC','CTMD','FDS_FIGI_SECURITY','FDS_FIGI_COMPOSITE','FDS_FIGI_LISTING')
print(df)
