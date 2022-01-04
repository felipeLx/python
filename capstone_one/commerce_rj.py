import pandas as pd

rj_com = pd.ExcelFile('./comercio_rj.xls')
sheet_names = rj_com.sheet_names

# print(rj_com.op)

area = 10.0

if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")
