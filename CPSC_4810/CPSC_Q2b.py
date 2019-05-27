#!/usr/bin/env python3
import pandas as pd
import numpy as np
df = pd.read_csv("/Users/NT/flightdelay.csv")
print(df.Dest.value_counts().head(n=3))
print("Suzie")

