import pandas as pd
from scipy.stats import spearmanr


def compute_correlations(file_path, colA_name):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 提取指定的列 A
    A = df[colA_name]

    # 需要计算相关性的列
    target_cols = [
        "Assignees"	,"Participants",	"Comments(Include report)",	"Closed Time",
        "Author Followers",	"Author Repositories","Author Stars",
        "Author Registration time",
        "Total Contributions",	"Total Contributions Before the Issue","Contributions Within 1 Year Before Submitting the Issue",
        "Contributions Before Submitting the Issue In the Repository","Total Contributions In the Repository",
        "Previous Frequency(all)","Previous Frequency(Same Hardware)",

    ]

    # 存储结果的字典
    results = {}

    for col in target_cols:
        B = df[col]
        # 在计算之前，去除任何缺失值
        valid_idx = A.notna() & B.notna()
        A_valid = A[valid_idx]
        B_valid = B[valid_idx]

        # 计算 Spearman 相关性及其 p 值
        spearman_corr, spearman_p = spearmanr(A_valid, B_valid)
        results[col] = {
            "spearman_p": spearman_p,
            "s_c":spearman_corr
        }

    return results


if __name__ == "__main__":
    # 请将下面路径和列名替换为实际值
    file_path = r'..\..\Result\RQ7\RQ7.xlsx'
    colA_name ="Is the Bug Reproduced?"
# Can the Program Run?
# Is the Bug Reproduced?
    res = compute_correlations(file_path, colA_name)
    print(colA_name)
    # 输出 p 值
    for col, pvals in res.items():
        print(f"{col}")
        print(f"  Spearman p-value: {pvals['spearman_p']:}")
        print(f"  Spearman corr: {pvals['s_c']:}")