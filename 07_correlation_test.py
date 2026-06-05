import pandas as pd
from scipy.stats import pearsonr, spearmanr

df = pd.read_csv("clean_protocol_measurements.csv")

pearson_corr, pearson_p = pearsonr(df["rtt_ms"], df["download_time_sec"])
spearman_corr, spearman_p = spearmanr(df["rtt_ms"], df["download_time_sec"])

with open("correlation_results.txt", "w") as f:
    f.write("Correlation between RTT and Download Time\n")
    f.write("-----------------------------------------\n")
    f.write(f"Pearson correlation: {pearson_corr:.4f}\n")
    f.write(f"Pearson p-value: {pearson_p:.4f}\n\n")
    f.write(f"Spearman correlation: {spearman_corr:.4f}\n")
    f.write(f"Spearman p-value: {spearman_p:.4f}\n")

print("Correlation results saved in correlation_results.txt")