import pandas as pd
from scipy.stats import fisher_exact, chi2_contingency

a_list=[
        # "Assignees"	,"Participants",	"Comments(Include report)",	"Closed Time",
        # "Author Followers",	"Author Repositories","Author Stars",
        # "Author Registration time",		"Total Contributions",	"Total Contributions Before the Issue",
        # "Contributions Within 1 Year Before Submitting the Issue",	"Contributions Before Submitting the Issue In the Repository",
        # "Total Contributions In the Repository"	,"Previous Hardware Usage Frequency",	"Used the Same Hardware?","Steps","Steps Related to Hardware","Steps Including Code"
        "hardware info","text","annotated text","image","annotated image","recording","log"
]
for i in range(len(a_list)):
    # 配置文件路径
    excel_file = r'C:\Users\hty\Desktop\extracted_info.xlsx'  # 替换为你的 Excel 文件路径
    column_a = a_list[i]
    print(column_a+":",end='')
    column_b = "Can the Program Run?"  # B 列名称
    #  "Can the Program Run?"
    #  "Is the Bug Reproduced?"
    #   "Hardware Related?"
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 提取指定列，并清洗数据
    df_filtered = df[[column_a, column_b]].dropna()

    # 获取 A 列的中间值（中位数）
    median_a = df_filtered[column_a].median()
    # 根据中位数划分 high 组和 low 组
    high_group = df_filtered[df_filtered[column_a] > median_a]
    low_group = df_filtered[df_filtered[column_a] <= median_a]

    # 统计 high 组和 low 组中 B 列各值的计数
    high_counts = high_group[column_b].value_counts()
    low_counts = low_group[column_b].value_counts()

    # 打印计数结果
    # print("High 组 B 列值的计数：")
    # print(high_counts)
    # print("\nLow 组 B 列值的计数：")
    # print(low_counts)

    # 构建频数表（列联表）
    unique_b_values = df_filtered[column_b].unique()
    contingency_table = pd.DataFrame(index=["Low", "High"], columns=unique_b_values, data=0)

    for value in unique_b_values:
        contingency_table.loc["Low", value] = low_counts.get(value, 0)
        contingency_table.loc["High", value] = high_counts.get(value, 0)

    # print("\n列联表：")
    # print(contingency_table)

    # Fisher 精确检验和卡方检验
    if contingency_table.shape[1] == 2:
        # Fisher 精确检验（仅支持 2x2 列联表）
        odds_ratio, p_value_fisher = fisher_exact(contingency_table)
        #print("\nFisher 精确检验结果：")
        print(f"Odds Ratio: {odds_ratio}, P-value: {p_value_fisher}")
    else:
        print("\nFisher 精确检验无法应用于非 2x2 列联表。")

