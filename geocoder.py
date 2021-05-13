import requests
import codecs
import pandas as pd
import geocoder

dir_wk = r"DIR"

df = pd.read_stata(dir_wk + r"\DATA_WITH_ADDRESSES.dta")
t = len(df.index)
df["lat"] = r""
df["lon"] = r""

for k in range(0,t):
    address2 = ""
    for i, char in enumerate(df.loc[k,'address']):
        if char == " ":
            address2 += "+"
        else:
            address2 += char
    g = geocoder.arcgis(address2)
    df.loc[k,"lat"] = str(g.x)
    df.loc[k,"lon"] = str(g.y)
    out_pre = dir_wk + r"\PRELIMINAR_OUTPUT.dta"
    df.to_stata(out_pre)

out = dir_wk + r"\OUTPUT.dta"
df.to_stata(out)
