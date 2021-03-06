# 1. 数字を入力値として受け取り、その数字を2乗した戻り値を返す関数を書く。
# その後、ドキュメンテーション文字列を追加する。

def power2():
    """
    入力された数値の2乗を計算する。
    ：param number:int
    :return:整数型データ（not 文字列型データ）　入力された数値の2乗
    """
    number=int(input("数値を入力してください："))
    return number**2
print(power2())

print("---------------------------------------------------------------")

# 3. 3つの文字列の必須引数と、２つのオプション引数がある関数を書き出力する。

def calc(a,b,c,d=1,e=2):
    result=a+b+c+d+e
    print(result)
calc(3,4,5)
# A.15

print("---------------------------------------------------------------")

# 4. ２つの関数からなるプログラムを書く。
# １つ目は整数を引数として受け取り、その整数を２で割って求められる整数を出力
# として返す。２つ目の関数は整数を引数として受け取り、4でかけた整数を返す。
# プログラム内で、1つ目の関数を呼び、戻り値を変数として保存し、
# 2つ目の関数の引数として渡す。

def cal1(x):
    return x/2

def cal2(y):
    return y*4

relt_cal1=cal1(8)
print(cal2(relt_cal1))
# A.16

print("---------------------------------------------------------------")

"""
5. 文字列をfloat型に変換して戻り値とする関数を書く。
さらに起こりうる例外をキャッチする例外処理を書く。
"""

def conversion():
    try:
        return float("ネコ")
    except(ValueError):
        return "文字列をfloat型に変換できません"
print(conversion())

def conversion_miss():
    return float("ネコ")
print(conversion_miss())