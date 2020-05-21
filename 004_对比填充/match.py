# ---------------------------------------方法1------------------------------------------------
# import pandas as pd
# import os


# # 读取表
# df_my_books = pd.DataFrame(pd.read_excel('excels/作品信息表.xlsx', sheet_name='Sheet1'))

# df_my_author = pd.DataFrame(pd.read_excel('excels/作者表.xlsx', sheet_name='Sheet1'))

# # 左关联
# df_same_df = pd.merge(df_my_author, df_my_books, how='left', on=['Author'])

# # 结果输出到result.xls  
# filepath = 'result.xls'
# writer = pd.ExcelWriter(filepath)
# df_same_df.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
# writer.save()
# writer.close()














# # ---------------------------------------方法2------------------------------------------------

import pandas as pd
import os


# 读取表
df_my_books = pd.DataFrame(pd.read_excel('excels/作品信息表.xlsx', sheet_name='Sheet1'))

df_my_author = pd.DataFrame(pd.read_excel('excels/作者表.xlsx', sheet_name='Sheet1'))

# 新建空列表，把想要的那一些行放进去列表里。
my_list = []

for i in range(len(df_my_author)):
    for j in range(len(df_my_books)):
        if str(df_my_books.iloc[j]['Author']) == str(df_my_author.iloc[i]['Author']):
            # 把想要的那一行放进去列表里：这行的数据就是df_my_books.iloc[j]
            my_list.append(df_my_books.iloc[j])

# 把列表转成dataframe
df_same_df = pd.DataFrame(my_list)

# 结果输出到result.xls
filepath = 'result.xls'
writer = pd.ExcelWriter(filepath)
df_same_df.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
writer.save()
writer.close()