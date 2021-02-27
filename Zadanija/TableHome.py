import pandas as pd

df = pd.read_csv("TableHome.csv", header=1)

ent = input("'Score'" + "\n" + "'GDP per capita'" + "\n" + "'Social support'" + "\n" + "'Healthy life expectancy'" + "\n" + "'Freedom to make life choices'" + "\n" + "'Generosity'" + "\n" + "'Perceptions of corruption'" + "\n" + "Enter one of the suggested values: ")
a = "Score"
b = "GDP per capita"
c = "Social support"
d = "Healthy life expectancy"
e = "Freedom to make life choices"
f = "Generosity"
g = "Perceptions of corruption"

try:
    if ent == a:
        a1 = df.sort_values("Score").tail(16)
        a1.to_csv("TableHome1.csv", columns=["Country or region", "Score"])
    elif ent == b:
        b1 = df.sort_values("GDP per capita").tail(16)
        b1.to_csv("TableHome1.csv", columns=["Country or region", "GDP per capita"])
    elif ent == c:
        c1 = df.sort_values("Social support").tail(16)
        c1.to_csv("TableHome1.csv", columns=["Country or region", "Social support"])
    elif ent == d:
        d1 = df.sort_values("Healthy life expectancy").tail(16)
        d1.to_csv("TableHome1.csv", columns=["Country or region", "Healthy life expectancy"])
    elif ent == e:
        e1 = df.sort_values("Freedom to make life choices").tail(16)
        e1.to_csv("TableHome1.csv", columns=["Country or region", "Freedom to make life choices"])
    elif ent == f:
        f1 = df.sort_values("Generosity").tail(16)
        f1.to_csv("TableHome1.csv", columns=["Country or region", "Generosity"])
    elif ent == g:
        g1 = df.sort_values("Perceptions of corruption").tail(16)
        g1.to_csv("TableHome1.csv", columns=["Country or region", "Perceptions of corruption"])
    else:
        print("Invalid request")
except:
    print("Invalid request")





