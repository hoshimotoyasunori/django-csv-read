import pandas as pd
# from pathlib import Path

filepath = 'sample.csv'
# print(Path(filepath).read_text())

# header=1 は1行目から読み込み開始
# usecols=[1, 3, 6, 7] は読み込む行の指定[1.項目名 3.桁数 6.物理名 7.型]
# index_col=0 行ラベルとなる列の指定


df = pd.read_csv(filepath,header=1,usecols=[1, 3, 6, 7],index_col=0)
print(df)

# 出力
# df.to_csv("out.csv")