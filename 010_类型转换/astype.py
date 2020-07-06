# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：astype转换为字符串或者数字
df_my_books['ISBN'] = df_my_books['ISBN'].astype(str)

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)