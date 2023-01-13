import pandas as pd
# from pathlib import Path

filepath = 'csv_input/sample1.csv'
# print(Path(filepath).read_text())

# usecols=[1, 3, 6, 7] は読み込む行の指定[1.項目名 3.桁数 6.物理名 7.型]
# header=0 は0行目から読み込み開始
# names=["item_name","digit","physical_name","type"]はheaderのラベル名指示


df = pd.read_csv(
        filepath,
        usecols=[1, 3, 6, 7],
        header=0,
        names=["item_name","digit","physical_name","type"]
        )

# df_1=df.reindex(columns=["physical_name","type","item_name","digit"])はカラムの順番変更
df_1=df.reindex(columns=["physical_name","type","item_name","digit"])

print(df_1)


# 出力
df_1.to_csv("csv_output/out1.csv")