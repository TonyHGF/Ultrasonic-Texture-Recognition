# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:14:07 2023

@author: Tony
"""

import os

# 指定要重命名的根文件夹路径
root_folder_path = "test"  # 将此路径替换为你的根文件夹路径

label = 1
index = 1
# 遍历根文件夹及其子文件夹
for folder_path, _, file_list in os.walk(root_folder_path):
    # 获取最近的父文件夹名
    parent_folder_name = os.path.basename(folder_path)

    # 遍历文件列表并重命名文件
    for file_name in file_list:
        # 构建新文件名
        # name = file_name.split('.')[0]
        # name += ".tif"
        # new_file_name = f"{name}{".tif"}"
        # new_file_name = f"{file_name}_{'#'}_{index}"
        
        lst = file_name.split('_')[1:]
        fst = file_name.split('_')[0]
        fst = fst + '#' + str(index) + '#'
        new_lst = '_'.join(lst[1:])
        # 构建完整的旧路径和新路径
        name = fst + new_lst
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, name)

        # 重命名文件
        os.rename(old_path, new_path)
        index += 1

print("文件重命名完成")
