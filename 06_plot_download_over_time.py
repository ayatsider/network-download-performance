import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_protocol_measurements.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(10, 5))

for region in df["region"].unique():
    subset = df[df["region"] == region]
    plt.plot(
        subset["timestamp"],
        subset["download_time_sec"],
        marker="o",
        linestyle="-",
        label=region
    )

plt.xlabel("Time")
plt.ylabel("Download Time (seconds)")
plt.title("Download Time Over Time by Region")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figure_download_over_time.png", dpi=300)
plt.show()