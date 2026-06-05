import pandas as pd

# قراءة البيانات
df = pd.read_csv("clean_protocol_measurements.csv")

# حساب الإحصائيات
table = (
    df.groupby("region")["rtt_ms"]
    .agg(
        Mean_RTT="mean",
        Median_RTT="median",
        Std_Dev="std",
        Min_RTT="min",
        Max_RTT="max",
        Measurements="count"
    )
    .round(2)
    .reset_index()
)

# عرض الجدول
print("\nRTT Statistics by Region\n")
print(table)

# حفظ CSV
table.to_csv("rtt_statistics_by_region.csv", index=False)

# إخراج LaTeX جاهز للورقة
latex_table = table.to_latex(
    index=False,
    caption="RTT statistics by geographic region.",
    label="tab:rtt_stats"
)

with open("rtt_statistics_by_region.tex", "w") as f:
    f.write(latex_table)

print("\nLaTeX table saved to rtt_statistics_by_region.tex")