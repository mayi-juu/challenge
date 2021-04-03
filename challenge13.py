# 2. Squareクラスにchange_sizeメソッドを定義し、そこに渡した数値の分だけSquareオブジェクトの
# 横幅を増やしたり、減らしたり（マイナス値の場合）する。

class Ssquare:
    def __init__(self,w,l):
        self.wid=w
        self.len=l
        print("width:"+str(self.wid)+"、length:"+str(self.len))

    def change_size(self,n):
        self.wid=self.wid+n
        print("横幅に{}を加えました".format(n))

ssquare=Ssquare(10,15)
ssquare.change_size(3)
print(ssquare.wid)
ssquare.change_size(-2)
print(ssquare.wid)

print("......................................................")

# 3. Sikakuクラスを定義し、ip2challenge13.pyからSquareクラスを継承する。そしてSikakuクラスの
# オブジェクトを生成し、メソッドareaとメソッドsizeを呼び出す。

from ip2challenge13 import Square

class Sikaku(Square):
    pass

sikaku=Sikaku(20,30)
sikaku.size()
print(sikaku.area())

# 継承したクラスをさらに継承することができる！
# import、from importするときは、インポート元のモジュールがインポート先のモジュールと
# 同じディレクトリ内に存在しないといけない？！

print("......................................................")

#4.HorseクラスとRiderクラスを定義する。コンポジションを使って、馬(Horse)に騎手(Rider)を持たせる。

class Horse:
    def __init__(self,name,ozz,owner):
        self.name=name
        self.ozz=ozz
        self.owner=owner

class Rider:
    def __init__(self,name):
        self.name=name

rider=Rider("仮面")
horse=Horse("バイク","HIGH",rider)
print(horse.name)
print(horse.ozz)
print(horse.owner)
print(horse.owner.name)