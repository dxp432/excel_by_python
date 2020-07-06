# 第1步：先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：删除价格这一列
df_my_books = df_my_books.drop('价格', axis = 1)

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)