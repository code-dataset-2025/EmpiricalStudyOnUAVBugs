import pandas as pd
from scipy import stats
from cliffs_delta import cliffs_delta

def perform_wilcoxon_test(file_path, group_column, value_column):
    """
    根据指定列将数据分组并进行 Wilcoxon 秩和检验（Mann-Whitney U）并计算 Cliff's Delta。

    参数:
        file_path (str): Excel 文件路径
        group_column (str): 用于分组的列名（值只能为 0 或 1）
        value_column (str): 需要检验的数值列名

    返回:
        dict: 包含统计量、p 值、Cliff's Delta 和两组样本量的结果字典
    """
    df = pd.read_excel(file_path)

    if group_column not in df.columns:
        raise ValueError(f"分组列 '{group_column}' 不存在")
    if value_column not in df.columns:
        raise ValueError(f"数值列 '{value_column}' 不存在")

    if not set(df[group_column].unique()).issubset({0, 1}):
        raise ValueError("分组列包含非0/1值")

    group0 = df[df[group_column] == 0][value_column].dropna()
    group1 = df[df[group_column] == 1][value_column].dropna()

    print(f"0 类中位数: {group0.median()}")
    print(f"1 类中位数: {group1.median()}")

    # Mann-Whitney U 检验
    stat, p_value = stats.mannwhitneyu( group1,group0, alternative='two-sided')

    delta,magnitude = cliffs_delta( group1.values,group0.values)

    return {
        'statistic': stat,
        'p_value': p_value,
        'cliffs_delta': delta,
        'cliffs_magnitude': magnitude,
        'group0_size': len(group0),
        'group1_size': len(group1)
    }


if __name__ == "__main__":
    excel_path = r'..\..\Result\RQ4\RQ4.xlsx'
    group_col = 'Hardware Related?'
    test_cs = [
        "Author Followers", "Author Repositories", "Author Stars",
        "Author Registration time",
        "Total Contributions", "Total Contributions Before the Issue",
        "Contributions Within 1 Year Before Submitting the Issue",
        "Contributions Before Submitting the Issue In the Repository", "Total Contributions In the Repository",
        "Previous Frequency(all)",
        "Steps"
    ]
    for test_col in test_cs:
        print(f'{test_col}:')
        try:
            result = perform_wilcoxon_test(excel_path, group_col, test_col)
            print(f"    0 组样本数: {result['group0_size']}")
            print(f"    1 组样本数: {result['group1_size']}")
            print(f"    Mann-Whitney U 统计量: {result['statistic']:.4f}")
            print(f"    P 值: {result['p_value']:}")
            print(f"    Cliff's Delta: {result['cliffs_delta']:.4f} ({result['cliffs_magnitude']})")
            print("")
        except Exception as e:
            print(f"发生错误: {e}")
