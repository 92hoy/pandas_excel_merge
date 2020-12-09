import pandas as pd
import openpyxl
import sys

df = pd.read_excel("./location_data/AI_TEST_201104.xlsx", sheet_name='03_자동측정망')
df1 = df['SN'] != 0
# column sort
df1 = df[df1].sort_values('SN')

h_list = []
choice_excel = []
tmp_dict={}
start_year=2016
end_year=2020
for i in df1.values:
    river=[]
    for year in range(start_year, end_year):
        river.append('./excel_data/'+str(i[2]) + '_' + str(year) + '.xlsx')
        if year == end_year-1:
            choice_excel.append(river)

# print(tmp_dict)
for i,k in zip(choice_excel,df1.values):
    excel_names = i
    excels = [pd.ExcelFile(name) for name in excel_names]
    frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
    frames[1:] = [df[1:] for df in frames[2:]]
    combined = pd.concat(frames)

    #파일저장
    combined.to_excel("./result/"+k[2]+"_all.xlsx", header=False, index=False)
