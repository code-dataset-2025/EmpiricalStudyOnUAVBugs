import os
import re
import pandas as pd

# 参数设置
folder_path = "./answer4/CANREPRODUCE"  # 文件夹路径
excel_path = "extracted_info.xlsx"  # Excel 文件路径
output_path = "extracted_info.xlsx"  # 修改后保存的 Excel 文件路径
w_column = 18  # 第 w 列 (从1开始计数)

# 步骤1：提取文件夹中所有 issue 的标号 x
issue_files = os.listdir(folder_path)
issue_numbers = set()
for file in issue_files:
    match = re.match(r'issue(\d+)\.md$', file)
    if match:
        issue_numbers.add(match.group(1))

# 步骤2：读取 Excel 文件
df = pd.read_excel(excel_path, engine='openpyxl')

# 确保第 w 列存在，若不存在则填充为 0
if w_column > len(df.columns):
    for _ in range(w_column - len(df.columns)):
        df[f"Unnamed: {len(df.columns) + 1}"] = 0

# 步骤3：根据第一列值检查文件是否存在，修改第 w 列
for index, row in df.iterrows():
    if index == 0:
        continue  # 跳过第一行（标题行）
    issue_number = str(row.iloc[0])
    if issue_number in issue_numbers:
        df.iloc[index, w_column - 1] = 1
    else:
        df.iloc[index, w_column - 1] = 0

# 步骤4：保存修改后的 Excel 文件
df.to_excel(output_path, index=False, engine='openpyxl')
print(f"修改后的文件已保存到 {output_path}")