import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_protocol_measurements.csv")

df["rtt_ms"] = pd.to_numeric(df["rtt_ms"], errors="coerce")
df["download_time_sec"] = pd.to_numeric(df["download_time_sec"], errors="coerce")
df = df.dropna(subset=["rtt_ms", "download_time_sec", "region", "protocol"])

configs = {
    "Asia": {
        "bins": [50, 75, 100, 125, 150, 175, 200, 225, 250, 500],
        "labels": ["50-75", "75-100", "100-125", "125-150", "150-175",
                   "175-200", "200-225", "225-250", "250-500"],
        "title": "Average Download Time Across RTT Ranges in Asia",
        "filename": "figure_rtt_bins_download_time_asia_bw.png"
    },
    "Germany": {
        "bins": [60, 70, 80, 90, 100, 115],
        "labels": ["60-70", "70-80", "80-90", "90-100", "100-115"],
        "title": "Average Download Time Across RTT Ranges in Europe",
        "filename": "figure_rtt_bins_download_time_europe_bw.png"
    }
}

linestyles = {
    "FTP": "-",
    "HTTP": "--",
    "HTTPS": ":"
}

markers = {
    "FTP": "o",
    "HTTP": "s",
    "HTTPS": "^"
}

for region, cfg in configs.items():

    region_df = df[df["region"] == region].copy()

    region_df["rtt_bin"] = pd.cut(
        region_df["rtt_ms"],
        bins=cfg["bins"],
        labels=cfg["labels"],
        include_lowest=True
    )

    summary = (
        region_df
        .groupby(["rtt_bin", "protocol"], observed=True)
        .agg(
            mean_download_time=("download_time_sec", "mean"),
            readings=("download_time_sec", "count")
        )
        .reset_index()
    )

    summary.to_csv(
        cfg["filename"].replace(".png", ".csv"),
        index=False
    )

    plt.figure(figsize=(8, 5))

    for protocol in ["FTP", "HTTP", "HTTPS"]:
        subset = summary[summary["protocol"] == protocol]

        if subset.empty:
            continue

        plt.plot(
            subset["rtt_bin"].astype(str),
            subset["mean_download_time"],
            linestyle=linestyles[protocol],
            marker=markers[protocol],
            color="black",
            linewidth=2,
            markersize=6,
            label=protocol
        )

    plt.xlabel("RTT Range (ms)")
    plt.ylabel("Average Download Time (seconds)")
    plt.title(cfg["title"])
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Protocol")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        cfg["filename"],
        dpi=600,
        bbox_inches="tight"
    )

    plt.show()

    print("Saved:", cfg["filename"])