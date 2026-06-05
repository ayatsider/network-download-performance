import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("clean_protocol_measurements.csv")

model = smf.ols(
    "download_time_sec ~ rtt_ms + C(region) + C(protocol)",
    data=df
).fit()

with open("regression_results.txt", "w") as f:
    f.write(model.summary().as_text())

print("Regression results saved in regression_results.txt")