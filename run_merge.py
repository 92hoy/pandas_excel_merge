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
choice_excel = []
start_year = 2016
end_year = 2020
for i in df1.values:
    river = []
    for year in range(start_year, end_year):
        river.append('./excel_data/' + str(i[2]) + '_' + str(year) + '.xlsx')
        if year == end_year - 1:
            choice_excel.append(river)

print(choice_excel)
# g_df = pd.read_excel("./excel_data/가평_2016.xlsx")
# g_df1 = pd.read_excel("./excel_data/가평_2017.xlsx")
# p = pd.concat([g_df, g_df1], axis=1)
# print(p.head())
cnt = 0
pd_concat = []
for i in choice_excel[0]:
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
print(kk.head())

########### use python / openpyxl ################
# df = pd.read_excel("./location_data/AI_TEST_201104.xlsx", sheet_name='03_자동측정망')
# df1 = df['SN'] != 0
# # column sort
# df1 = df[df1].sort_values('SN')
# h_list = []
# choice_excel = []
# start_year=2016
# end_year=2020
# for i in df1.values:
#     river=[]
#     for year in range(start_year, end_year):
#         river.append('./excel_data/'+str(i[2]) + '_' + str(year) + '.xlsx')
#         if year == end_year-1:
#             choice_excel.append(river)
#
# for i,k in zip(choice_excel,df1.values):
#     excel_names = i
#     excels = [pd.ExcelFile(name) for name in excel_names]
#     frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
#     frames[1:] = [df[1:] for df in frames[2:]]
#     combined = pd.concat(frames)
#
#     #파일저장
#     combined.to_excel("./result/"+k[2]+"_all.xlsx", header=False, index=False)
