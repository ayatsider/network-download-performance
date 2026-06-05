import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
df = pd.read_csv("clean_protocol_measurements.csv")

# Convert columns
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["rtt_ms"] = pd.to_numeric(df["rtt_ms"], errors="coerce")

df = df.dropna(subset=["timestamp", "rtt_ms"])

# Keep one RTT reading per region per measurement time
# لأن RTT يتكرر مع كل protocol في نفس الجولة
df_rtt = df.drop_duplicates(subset=["timestamp", "region"])

# Aggregate every 3 hours
rtt_3h = (
    df_rtt
    .set_index("timestamp")
    .groupby("region")
    .resample("3H")["rtt_ms"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(9, 5))

linestyles = {
    "Germany": "-",
    "Asia": "--",
    "USA": ":"
}

for region in rtt_3h["region"].unique():
    subset = rtt_3h[rtt_3h["region"] == region]

    plt.plot(
        subset["timestamp"],
        subset["rtt_ms"],
        linestyle=linestyles.get(region, "-"),
        linewidth=2,
        color="black",
        label=region
    )

plt.xlabel("Time")
plt.ylabel("Average RTT (ms)")
plt.title("RTT Variation Over Time by Region")

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.legend(title="Region")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "figure_rtt_over_time_3h_bw.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()

print("Saved: figure_rtt_over_time_3h_bw.png")