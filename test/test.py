import pandas as pd

# 第2步：读取表
# movies = pd.read_csv('http://bit.ly/imdbratings')
ufo = pd.read_csv('http://bit.ly/uforeports')

# print(movies.head())
print(ufo.head())

print(ufo.columns)
