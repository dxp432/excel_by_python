import pandas as pd

# 读取表1
df_1 = pd.DataFrame(pd.read_excel('1.xlsx', sheet_name='Sheet1'))

# 读取表2
df_2 = pd.DataFrame(pd.read_excel('2.xlsx', sheet_name='Sheet1'))

# 左关联
df_result = pd.merge(df_2, df_1, how='left', on=['设备'])

# 结果输出到result.xls
filepath = 'result.xls'
writer = pd.ExcelWriter(filepath)
df_result.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
writer.save()
writer.close()

