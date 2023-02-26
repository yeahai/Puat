# 2023/2/7 14:28
# 你好，夜嗨大帅比

import pandas as pd

dic_file = pd.read_csv("utils/dic1.txt",header=None).values

for i in  dic_file:
    print(i[0])