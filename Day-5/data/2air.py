import pandas as pd

df = pd.read_csv(
    "data/airqual.csv",
    parse_dates=[["Date", "Time"]],
    na_values=[-200],
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"]
).rename(
    columns={
        "CO(GT)": "co",
        "Date_Time": "tstamp",
        "T": "temp_c",
        "RH": "rel_hum",
        "AH": "abs_hum",
    }
).set_index("tstamp")

print(df.head())
print("minimum value", df.index.min())
print("Maximum value", df.index.max())