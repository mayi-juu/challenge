# 1. statisticsモジュールの別の関数を呼ぶ。

import statistics
numbers=[2,3,5,6]

mother=statistics.pvariance(numbers)
standard=statistics.variance(numbers)

print(mother)
print(standard)

print("//////////////////////////////////////////////////////////////////")

dunums=[]
ave=sum(numbers)/len(numbers)

for a in numbers:
    du=(a-ave)**2
    dunums.append(du)

dusum=sum(dunums)
var=dusum/ave

print(ave)
print(dunums)
print(dusum)
print(var)
# mother=var　→　標準標本分散とは？？

print("---------------------------------------------------------------")

# 2.
"""
新たなモジュールを作成し、関数を１つ書く。さらに、この関数内にもう１つ関数（メソッド）を書き、
このモジュールをインポートする。そして、１つ目の関数と２つ目の関数を（直接）実行する。
"""
# 関数の中に関数書くのはたぶん意味なし！！(ipchallenge8.pyファイル実行結果より)

import ipchallenge8
for x in numbers:
    print(ipchallenge8.judge(x))