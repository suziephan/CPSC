#!/usr/bin/env python3

import pandas as pd
import numpy as np
df = pd.read_csv("/Users/NT/flightdelay.csv")
df1=df[df.Origin=="SFO"][['ArrDelay','Origin']].head(n=3)
df1.to_csv('first3sfo.csv',index=False)
df2=pd.read_csv('first3sfo.csv')
df2
print(df2)

