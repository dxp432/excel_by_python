# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：替换
# Pandas中字符串的操作和原生字符串操作几乎一毛一样，
# 唯一不同的是需要在操作前加上".str"
# 下面这行代码作用是：把作者这一列空格替换成下划线
df_my_books['作者'] = df_my_books['作者'].str.replace(' ', '_')

# 把所有列名的空格替换成下划线
df_my_books.columns = df_my_books.columns.str.replace(' ', '_')

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)