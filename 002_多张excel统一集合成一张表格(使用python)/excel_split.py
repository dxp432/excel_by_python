import pandas as pd

# 把表里的每一行作为一张表，分离生成。

# 读取表1
df_1 = pd.DataFrame(pd.read_excel('many_excels.xlsx', sheet_name='Sheet1'))
# print(len(df_1))

for my_row_index in range(0, len(df_1), 1):
    df_result = df_1[my_row_index:my_row_index + 1]
    # print(df_1[my_row_index:my_row_index + 1])
    # 结果输出到result.xls
    filepath = 'excels/' + str(my_row_index) + '.xlsx'
    writer = pd.ExcelWriter(filepath)
    df_result.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
    writer.save()
    writer.close()
