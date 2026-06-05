import pandas as pd
from scipy.stats import pearsonr

# Read data
df = pd.read_csv("clean_protocol_measurements.csv")

df["rtt_ms"] = pd.to_numeric(df["rtt_ms"], errors="coerce")
df["download_time_sec"] = pd.to_numeric(df["download_time_sec"], errors="coerce")

df = df.dropna(subset=["rtt_ms", "download_time_sec"])

results = []

for region in sorted(df["region"].unique()):

    row = {"Region": region}

    for protocol in ["FTP", "HTTP", "HTTPS"]:

        subset = df[
            (df["region"] == region) &
            (df["protocol"] == protocol)
        ]

        if len(subset) > 1:

            r, p = pearsonr(
                subset["rtt_ms"],
                subset["download_time_sec"]
            )

            row[protocol] = round(r, 3)

        else:
            row[protocol] = None

    results.append(row)

corr_table = pd.DataFrame(results)

print("\nCorrelation by Region and Protocol\n")
print(corr_table)

# Save CSV
corr_table.to_csv(
    "grouped_correlation.csv",
    index=False
)

# Generate LaTeX table
latex_table = corr_table.to_latex(
    index=False,
    caption="Pearson correlation coefficients between RTT and download time for each region and protocol.",
    label="tab:grouped_corr"
)

with open(
    "grouped_correlation.tex",
    "w",
    encoding="utf-8"
) as f:
    f.write(latex_table)

print("\nSaved:")
print("grouped_correlation.csv")
print("grouped_correlation.tex")