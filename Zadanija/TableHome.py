import pandas as pd

df = pd.read_csv("TableHome.csv", header=1)
socsup = df.sort_values("Social support").head(11)

socsup.to_csv("TableHome1.csv", columns=["Country or region", "Social support"])
