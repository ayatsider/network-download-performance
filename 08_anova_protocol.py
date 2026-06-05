import pandas as pd
from scipy.stats import f_oneway

df = pd.read_csv("clean_protocol_measurements.csv")

groups = [
    df[df["protocol"] == protocol]["download_time_sec"]
    for protocol in df["protocol"].unique()
]

f_stat, p_value = f_oneway(*groups)

with open("anova_protocol_results.txt", "w") as f:
    f.write("ANOVA Test: Download Time by Protocol\n")
    f.write("------------------------------------\n")
    f.write(f"F-statistic: {f_stat:.4f}\n")
    f.write(f"p-value: {p_value:.4f}\n")

print("ANOVA protocol results saved in anova_protocol_results.txt")