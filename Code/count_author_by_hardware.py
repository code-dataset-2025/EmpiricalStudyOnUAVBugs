import os
import re
import pandas as pd
from collections import defaultdict


def extract_issue_numbers(folder_path):
    """从文件夹中读取issue编号并按子文件夹分类"""
    issue_numbers_by_folder = defaultdict(list)

    for subdir, _, files in os.walk(folder_path):
        folder_name = os.path.basename(subdir)
        for file in files:
            if file.endswith(".md"):
                match = re.match(r"issue(\d+)\.md", file)
                if match:
                    issue_number = int(match.group(1))
                    issue_numbers_by_folder[folder_name].append(issue_number)

    return issue_numbers_by_folder


def count_authors_by_folder(issue_numbers_by_folder, excel_file):
    """根据issue编号统计各作者在每个文件夹中的出现次数"""
    # 读取Excel文件
    df = pd.read_excel(excel_file, header=None)

    # 假设第1列为issue编号，第9列为作者
    issue_to_author = dict(zip(df[0], df[8]))

    # 统计各文件夹中每个作者的出现次数
    author_count_by_folder = defaultdict(lambda: defaultdict(int))

    for folder, issue_numbers in issue_numbers_by_folder.items():
        for issue_number in issue_numbers:
            author = issue_to_author.get(str(issue_number))
            if author:
                author_count_by_folder[folder][author] += 1

    return author_count_by_folder


def output_author_counts_to_excel(author_count_by_folder, output_file):
    """将统计结果输出到Excel文件"""
    rows = []
    for folder, author_counts in author_count_by_folder.items():
        for author, count in author_counts.items():
            rows.append([folder, author, count])

    output_df = pd.DataFrame(rows, columns=["Folder", "Author", "Count"])
    output_df.to_excel(output_file, index=False)


if __name__ == "__main__":
    # 设置文件夹路径和Excel文件路径
    folder_path = "../answer4"
    excel_file = "extracted_info.xlsx"
    output_file = "count_author_by_hardware.xlsx"

    # 提取issue编号
    issue_numbers_by_folder = extract_issue_numbers(folder_path)

    # 统计作者出现次数
    author_count_by_folder = count_authors_by_folder(issue_numbers_by_folder, excel_file)
    print(author_count_by_folder)
    # 输出结果到Excel
    output_author_counts_to_excel(author_count_by_folder, output_file)
    print(f"统计结果已保存到 {output_file}")
