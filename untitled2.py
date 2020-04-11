import numpy as np
import pandas as pd


#Open HLA PLT daily report
def report_read():
    HLA_report = 'C:\\Users\\rodri\\OneDrive\\Desktop\\Py Stuff\\RID 17-00441 Apheresis Platelet Collections with HLA.xlsx'
    df = pd.read_excel(HLA_report, usecols = [0,1,3,6,7,8,9], skiprows = 3)
    df = df.dropna
    print(df.columns)
    
report_read()