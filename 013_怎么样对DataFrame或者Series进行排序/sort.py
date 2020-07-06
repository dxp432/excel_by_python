# 第1步：先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# print(df_my_books['价格'].sort_values(ascending = False))

# 第3步：对价格进行排序
df_my_books = df_my_books.sort_values('价格', ascending = False)

# 对多个列进行先后排序
df_my_books = df_my_books.sort_values(['书名', '作者'], ascending = [True, True])

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)