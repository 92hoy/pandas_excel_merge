import pandas as pd
from pandas import DataFrame
import openpyxl
import sys

########### use pandas ################
df = pd.read_excel("./location_data/AI_TEST_201104.xlsx", sheet_name='03_자동측정망')
df1 = df['SN'] != 0
# column sort
df1 = df[df1].sort_values('SN')
h_list = []
equal_name_excel = []
tmp_excel = []
set_excel = []
start_year = 2016
end_year = 2020

for i in df1.values:
    river = []
    tmp_excel.append(i[2])
    for year in range(start_year, end_year):
        river.append('./excel_data/' + str(i[2]) + '_' + str(year) + '.xlsx')
        if year == end_year - 1:
            equal_name_excel.append(river)

for year in range(start_year, end_year):
    tmp = []
    for i in tmp_excel:
        tmp.append('./excel_data/' + i + '_' + str(year) + '.xlsx')
    set_excel.append(tmp)

# g_df = pd.read_excel("./excel_data/가평_2016.xlsx")
# g_df1 = pd.read_excel("./excel_data/가평_2017.xlsx")
# p = pd.concat([g_df, g_df1], axis=1)
# print(p.head())

## 한강 하류-> 상류 excel
cnt = 0
pd_concat = []
for set_excel_list, year in zip(set_excel, range(start_year, end_year)):
    for i in set_excel_list:
        print(i)
        cnt += 1
        d_f = pd.read_excel(i)
        # 변경할 컬럼이름 생성
        new_col_name = []
        for k in d_f.columns.values:
            new_col_name.append(k + '_' + str(cnt))
        # 변경된 컬럼 적용
        # d_f.rename(columns=dict(zip(d_f.columns.values, new_col_name)))
        d_f.columns = new_col_name
        pd_concat.append(d_f)
    kk = pd.concat(pd_concat, axis=1)
    kk.to_excel('./result/'+'한강_' + str(year) + '.xlsx')

# 연도 병합
pd_concat = []
for equal_name_excel_list, year, name in zip(equal_name_excel, range(start_year, end_year), df1.values):
    for i in equal_name_excel_list:
        print(i)
        d_f = pd.read_excel(i)
        pd_concat.append(d_f)
    kk = pd.concat(pd_concat, axis=0)
    kk.to_excel('./result/'+str(name[2]) + '_all.xlsx')

########### use python / openpyxl ################
# df = pd.read_excel("./location_data/AI_TEST_201104.xlsx", sheet_name='03_자동측정망')
# df1 = df['SN'] != 0
# # column sort
# df1 = df[df1].sort_values('SN')
# h_list = []
# equal_name_excel = []
# start_year=2016
# end_year=2020
# for i in df1.values:
#     river=[]
#     for year in range(start_year, end_year):
#         river.append('./excel_data/'+str(i[2]) + '_' + str(year) + '.xlsx')
#         if year == end_year-1:
#             equal_name_excel.append(river)
#
# for i,k in zip(equal_name_excel,df1.values):
#     excel_names = i
#     excels = [pd.ExcelFile(name) for name in excel_names]
#     frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
#     frames[1:] = [df[1:] for df in frames[2:]]
#     combined = pd.concat(frames)
#
#     #파일저장
#     combined.to_excel("./result/"+k[2]+"_all.xlsx", header=False, index=False)
