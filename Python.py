import pandas as pd
import csv

df = pd.read_csv("final_Scaper.csv")

del df["luminosity"]
df.to_csv("main.csv")