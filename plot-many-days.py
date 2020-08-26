#!/usr/bin/env python

import os

import pandas as pd
import plotly.express as px

temp_data_path = '/mnt/media/temps'

file_entries = []
for entry in os.scandir(temp_data_path):
    n = entry.name
    if n.startswith("thermo-") and n.endswith(".dat"):
        file_entries.append(entry)

print(f"Files found: {[x.name for x in file_entries]}")
file_entries.sort(key=lambda a: a.name)
print(f"Sorted: {[x.name for x in file_entries]}")


df = None
for e in file_entries:
    f = e.path
    print(f"File: {f}")
    if df is None:
        df = pd.read_csv(f)
    else:
        df = df.append(pd.read_csv(f))

fig = px.line(df, x='Date', y='F')
fig.show()
