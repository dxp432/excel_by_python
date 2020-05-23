import pandas as pd
import os
import numpy as np


# up 你好 我想咨询下 如何提取一个文件夹所有表格名字 然后赋值到各个表格中，单独弄一列显示

# # 生成大量示例excel
# df_my_books = pd.DataFrame(np.random.randn(3,3))

# for i in range(1,101):
#     # 结果输出到result.xls  
#     filepath = '好多excel/打死不改版' + str(i) + '.xls'
#     writer = pd.ExcelWriter(filepath)
#     df_my_books.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
#     writer.save()
#     writer.close()

# 新建空列表，把想要的放进去列表里。
my_list = []
for root, dirs, files in os.walk("好多excel/"):

    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list

    # 遍历文件
    for f in files:
        # 去掉后缀
        name = f.replace('.xls','')
        print(name)
        # 把每张表的名字追加
        my_list.append(name)

# 把列表转成dataframe
df_result = pd.DataFrame(my_list)

# 结果输出到result.xls
filepath = 'all_in_one.xlsx'
writer = pd.ExcelWriter(filepath)
df_result.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
writer.save()
writer.close()
