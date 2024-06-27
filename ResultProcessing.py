import os
import csv
import pandas as pd
# 指定目标文件夹
target_folder = 'test'

# 创建一个空列表来存储文件名信息
file_info_list = []

# 遍历目标文件夹中的所有文件
for filename in os.listdir(target_folder):
    # 检查文件是否为普通文件
    if os.path.isfile(os.path.join(target_folder, filename)):
        # 以'#'为分隔符拆分文件名，并去除空格
        # file_info = filename.split('#')
        # # file_info = [info.strip() for info in file_info]
        # # 去除文件扩展名
        # file_info[0] = os.path.splitext(file_info[0])[0]
        # # 将文件名信息添加到列表中
        # file_info_list.append(file_info)
        name = filename.split('.')[0]
        file_info = filename.split('#')
        info = []
        info.append(int(file_info[1]))
        info.append(file_info[0])
        if file_info[0] == 1:
            info.append("unhealthy")
        else:
            info.append("healthy")
        file_info_list.append(info)
        



# 指定要导出的CSV文件名
output_csv = 'res.csv'

# 将文件名信息写入CSV文件
df = pd.DataFrame(file_info_list, columns=['id', 'label', 'result'])
sorted_df = df.sort_values(by='id')
sorted_df.to_csv(output_csv, index=False, encoding='utf-8')

print(f'文件名信息已导出到{output_csv}')
