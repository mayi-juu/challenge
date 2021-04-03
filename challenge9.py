# 1. csv変換したエクセルファイル（自作）を読み込み、出力する。

# C:\Users\bsk-k\OneDrive\デスクトップ\python_lesson\独学プログラマー\9.file\練習用csv.csv

import csv
with open("..\9.file\練習用csv.csv","r",encoding="utf-8") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))


# ファイルパス＝コードを書き込んでいる「.pyファイル」があるフォルダを起点にする！！
# （そのファイルのフォルダ名は記述しなくてよい）
# 「..\」：一つ上の階層に移動する、「.\」：ファイルと同じディレクトリ場所

print("---------------------------------------------------------------")

# 2. 何か質問するプログラムを書く。そしてその入力された回答をtxtファイルに書き出した後、読み込む。

print("質問に回答してください")

guest1=input("どんな時に幸せを感じますか？：")
guest2=input("あなたは運がいい方ですか？：")
guest3=input("一番感謝したい人は誰ですか？：")

with open("ques.txt","w",encoding="utf-8") as q:
    q.write(guest1+"\n"+guest2+"\n"+guest3)

with open("ques.txt","r",encoding="utf-8") as q:
    print(q.read())

print("---------------------------------------------------------------")

# 4. リストのリストに含まれている要素をCSVファイルに書き出した後、読み込む。データは下記を使う。
# 書き出すとき、データの各要素はCSVの1行となり、その1行に含まれる各要素がカンマで区切られるようにする。
"""
[["トップガン","リスキービジネス","マイナリティーレポート"],
["タイタニック","リブナント","インセプション"],
["トレーニングデー","マンオンファイア","フライト"]]
"""

import csv

with open("enshu.csv","w",encoding="utf-8") as c:
    l=csv.writer(c,delimiter=",")
    l.writerow(["トップガン","リスキービジネス","マイナリティーレポート"])
    l.writerow(["タイタニック","リブナント","インセプション"])
    l.writerow(["トレーニングデー","マンオンファイア","フライト"])

with open("enshu.csv","r",encoding="utf-8") as c:
    l=csv.reader(c,delimiter=",")
    for youso in l:
        print(",".join(youso))

print("..........................................................................")

with open("enshu.csv","w",newline="",encoding="utf-8") as c:
    l=csv.writer(c,delimiter=",")
    l.writerow(["トップガン","リスキービジネス","マイナリティーレポート"])
    l.writerow(["タイタニック","リブナント","インセプション"])
    l.writerow(["トレーニングデー","マンオンファイア","フライト"])

with open("enshu.csv","r",encoding="utf-8") as c:
    l=csv.reader(c,delimiter=",")
    for youso in l:
        print(",".join(youso))

# Exeleファイルで読み込むにはライブラリを使う必要ありかも