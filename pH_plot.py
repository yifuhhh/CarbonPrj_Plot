import numpy as np
import pandas as pd

tmp = np.loadtxt("/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData/pH_2.csv", dtype=np.str, delimiter=",")
Ids = tmp[0:, 1].astype(np.float)
Vg = tmp[0:, 0].astype(np.float)
print(Vg)
print(Ids)
