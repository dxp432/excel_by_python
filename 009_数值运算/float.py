# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：数值型数据，常见的操作是计算，
# 分为与单个值的运算，长度相等列的运算。
# 现在想把所有价格都加上10000
df_my_books['价格'] = df_my_books['价格'] + 1000

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)