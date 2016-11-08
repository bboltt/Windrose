from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd


df = pd.read_csv("data.csv", names=["ws", "wd"], sep=",")
ws = df["ws"].values
wd = df["wd"].values


print "WD is ",wd
print "WS is ",ws
ax = WindroseAxes.from_ax()
ax.bar(wd,ws, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.show()

