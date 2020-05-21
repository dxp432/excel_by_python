import pandas as pd

# 读取表
# 返回的结果是dataframe
df_mybooks = pd.DataFrame(pd.read_excel('books.xlsx', sheet_name='Sheet1'))

print(df_mybooks)