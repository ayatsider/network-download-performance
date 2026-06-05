import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("clean_protocol_measurements.csv")

# Calculate average RTT by region
summary = (
    df.groupby("region")["rtt_ms"]
    .mean()
    .reindex(["Germany", "Asia", "USA"])
)

# Plot
plt.figure(figsize=(6,4))

bars = plt.bar(
    summary.index,
    summary.values,
    color="white",
    edgecolor="black",
    linewidth=1.5
)

# Add patterns for IEEE black & white printing
patterns = ["///", "...", "xxx"]

for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 2,
        f"{height:.1f}",
        ha="center"
    )

plt.xlabel("Geographic Region")
plt.ylabel("Average RTT (ms)")
plt.title("Average RTT by Geographic Region")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "figure_avg_rtt_by_region_bw.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()

print("Saved: figure_avg_rtt_by_region_bw.png")