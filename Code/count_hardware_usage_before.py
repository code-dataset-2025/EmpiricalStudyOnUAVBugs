import os
import re
import pandas as pd

# 指定主文件夹路径和 Excel 文件路径
folder_path = "./分类/使用的硬件"  # 替换为文件夹A的路径
excel_path = "extracted_info.xlsx"  # 替换为指定的Excel文件路径

# 加载 Excel 文件
df = pd.read_excel(excel_path)

# 检查 Excel 文件中是否有足够的列，添加最后一列（如果不存在）
if len(df.columns) < 10:
    df["Extra"] = None  # 添加第10列

# 遍历主文件夹的所有子文件夹
for subfolder_name in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.isdir(subfolder_path):
        continue

    # 收集子文件夹中的 issue 文件编号和路径
    issues = []
    for file_name in os.listdir(subfolder_path):
        if file_name.endswith(".md"):
            match = re.match(r"issue(\d+)\.md", file_name)
            if match:
                issue_number = int(match.group(1))
                issues.append((issue_number, os.path.join(subfolder_path, file_name)))

    # 遍历子文件夹中的每个 .md 文件
    for current_issue, file_path in issues:
        # 在 Excel 中找到对应行
        matching_row = df[df.iloc[:, 0] == current_issue]
        if matching_row.empty:
            print(f"Warning: Issue {current_issue} not found in Excel.")
            continue

        row_index = matching_row.index[0]
        author = matching_row.iloc[0, 8]  # 获取第9列（作者名）

        # 统计当前子文件夹中相同作者但编号小于当前编号的issue
        count = sum(
            1 for issue, _ in issues if issue < current_issue and df[df.iloc[:, 0] == issue].iloc[0, 8] == author)

        # 更新 Excel 文件中的最后一列
        df.at[row_index, "Extra"] = count

# 保存 Excel 文件
df.to_excel(excel_path, index=False)

print("Processing complete. Excel file updated.")
