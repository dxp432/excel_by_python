# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：一些时候PANDAS会把文件中日期格式的字段读取为字符串格式，
# 这里我们先赋值给新增的日期列，
# 然后用to_datetime()函数将字符串类型转换成时间格式
# 计算两个日期差
df_my_books['距离今天天数'] = pd.to_datetime('2020-07-01') - df_my_books['开始日期']

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)