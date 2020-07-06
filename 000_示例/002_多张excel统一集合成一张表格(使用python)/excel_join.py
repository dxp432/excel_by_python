import pandas as pd
import os

# 把作为分离生成的每一张表，合并到表里作为每一行。


if __name__ == '__main__':
    # result = df1.append(df2)
    result = pd.DataFrame()
    for root, dirs, files in os.walk("excels/"):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            # 路径+文件名
            print(os.path.join(root, f))
            # 读取表1
            df_1 = pd.DataFrame(pd.read_excel(os.path.join(root, f), sheet_name='Sheet1'))
            # 把每张表的数据追加成一张表的内容
            result = result.append(df_1)
    # 结果输出到result.xls
    filepath = 'all_in_one.xlsx'
    writer = pd.ExcelWriter(filepath)
    result.to_excel(excel_writer=writer, index=False, sheet_name='Sheet1')
    writer.save()
    writer.close()
