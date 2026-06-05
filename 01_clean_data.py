import pandas as pd

df = pd.read_csv("protocol_measurements.csv")

df = df[df["status"] == "success"].copy()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["rtt_ms"] = pd.to_numeric(df["rtt_ms"], errors="coerce")
df["download_time_sec"] = pd.to_numeric(df["download_time_sec"], errors="coerce")

df = df.dropna(subset=["timestamp", "rtt_ms", "download_time_sec"])

df.to_csv("clean_protocol_measurements.csv", index=False)

print("Clean data saved as clean_protocol_measurements.csv")
print("Rows:", len(df))