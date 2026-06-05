import pandas as pd

# قراءة البيانات
df = pd.read_csv("clean_protocol_measurements.csv")

# حساب الإحصائيات
table = (
    df.groupby(["region", "protocol"])["download_time_sec"]
    .agg(
        Mean="mean",
        Median="median",
        Std_Dev="std",
        Min="min",
        Max="max",
        Readings="count"
    )
    .round(2)
    .reset_index()
)

print("\nDownload Time Statistics\n")
print(table)

# حفظ CSV
table.to_csv(
    "download_time_statistics.csv",
    index=False
)

# توليد جدول LaTeX
latex_table = table.to_latex(
    index=False,
    caption="Download time statistics by geographic region and transfer protocol.",
    label="tab:download_stats"
)

with open(
    "download_time_statistics.tex",
    "w",
    encoding="utf-8"
) as f:
    f.write(latex_table)

print("\nLaTeX table saved to download_time_statistics.tex")