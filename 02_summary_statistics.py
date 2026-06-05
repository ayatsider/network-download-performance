import pandas as pd

df = pd.read_csv("clean_protocol_measurements.csv")

summary = df.groupby(["region", "protocol"]).agg(
    avg_rtt_ms=("rtt_ms", "mean"),
    std_rtt_ms=("rtt_ms", "std"),
    avg_download_time_sec=("download_time_sec", "mean"),
    std_download_time_sec=("download_time_sec", "std"),
    min_download_time_sec=("download_time_sec", "min"),
    max_download_time_sec=("download_time_sec", "max"),
    count=("download_time_sec", "count")
).reset_index()

summary.to_csv("summary_statistics.csv", index=False)

print(summary)