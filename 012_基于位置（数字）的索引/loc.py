# 第1步：一定是先导入我们的库
import pandas as pd

# 第2步：读取表
df_my_books = pd.read_excel('books.xlsx', sheet_name='Sheet1')

# 第3步：基于位置（数字）的索引
# 场景一（行选取）把第2行数据赋值为0
df_my_books.iloc[1, :] = 0

# 场景二（列选取）在第3列中的数据赋值为1
df_my_books.iloc[:, 2] = 1

# 场景三（行列交叉选取）
# 在第1到2列中，把第10行和第15行的数据赋值为2(索引含首不含尾)
df_my_books.iloc[9:15, 0:2] = 2
# 把第22行和24行同时列是第1列和第4列的数字赋值为3
df_my_books.iloc[[21, 23], [0, 3]] = 3

# 第4步，导出
df_my_books.to_excel('newbooks.xlsx',index = False)