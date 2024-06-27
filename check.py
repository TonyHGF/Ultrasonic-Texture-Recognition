# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:07:45 2023

@author: Tony
"""

import pandas as pd

# 读取第一个CSV文件，没有列名
file1_path = 'test.csv'
df1 = pd.read_csv(file1_path, header=None)

# 读取第二个CSV文件，没有列名
file2_path = 'res.csv'
df2 = pd.read_csv(file2_path, header=None)

# 要对比的列索引
column_index_to_compare_df1 = 2  # 假设要对比第三列数据
column_index_to_compare_df2 = 2  # 假设要对比第二列数据

# print(df1[2][0])
# print("###")
# print(df2[2])


# 对比两个DataFrame中指定列数据，计算相同数据的数量
common_data_count = df1[column_index_to_compare_df1].isin(df2[column_index_to_compare_df2]).sum()
total_rows = len(df1)
cnt = 0
for i in range(1, total_rows):
    # print(df1[)
    if df1[2][i] == df2[2][i]:
        cnt += 1

# 计算相同数据的占比

common_data_percentage = (cnt / total_rows) * 100

print(f"相同数据的占比为: {common_data_percentage:.2f}%")
