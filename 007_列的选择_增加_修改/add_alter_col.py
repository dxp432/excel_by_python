# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：
# 对列进行操作：选择两列
print(df_my_books[['书名','作者']])

# # 对列进行操作：增加列
df_my_books['我是新的列名'] = 'hello'

# # 对列进行操作：修改列
df_my_books['我是新的列名'] = df_my_books['书名'] + df_my_books['作者'] 

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)