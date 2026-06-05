import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clean_protocol_measurements.csv")

# Ensure numeric values
df["download_time_sec"] = pd.to_numeric(
    df["download_time_sec"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["download_time_sec", "region"])

# Region order in the dataset
regions_order = ["Asia", "Germany", "USA"]

# Display labels for the figure
display_labels = [
    "Asia\n(Azerbaijan)",
    "Europe\n(Germany)",
    "North America\n(USA)"
]

# Prepare data
data = [
    df[df["region"] == region]["download_time_sec"]
    for region in regions_order
]

# Create figure
plt.figure(figsize=(7, 5))

plt.boxplot(
    data,
    labels=display_labels,
    patch_artist=True,
    showfliers=True,
    medianprops=dict(color="black", linewidth=1.5),
    boxprops=dict(facecolor="white", color="black", linewidth=1.5),
    whiskerprops=dict(color="black", linewidth=1.2),
    capprops=dict(color="black", linewidth=1.2),
    flierprops=dict(
        marker="o",
        markerfacecolor="white",
        markeredgecolor="black",
        markersize=4,
        linestyle="none"
    )
)

plt.xlabel("Geographic Region")
plt.ylabel("Download Time (seconds)")
plt.title("Download Time Distribution by Region")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "figure_download_time_boxplot_by_region_bw.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()

print("Saved: figure_download_time_boxplot_by_region_bw.png")