# 2. 円を表すCircleクラスを定義し。計算して面積を返すareaメソッドを持たせる。
# 面積の計算にはmathモジュールを使い（π）、Circleオブジェクトを作ってareaメソッドで結果を出力する。

class Circle:
    def __init__(self,r):
        self.radius=r

    def area(self):
        import math
        return self.radius*self.radius*math.pi

guest=int(input("円の半径を入力してください："))
circle1=Circle(guest)
print(circle1.area())

print("---------------------------------------------------------------------------------")

# 4. 六角形を表すHexagonクラスを定義し、その中に外周の長さを計算して返すメソッドculを定義する。
# そしてHexagonオブジェクトを作り、culメソッドで結果を出力する。

class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.s6=s6
        # 左辺の「self.s1~s6」と右辺の「s1~s6」は違うデータ！！

    def side(self):
        return self.s6+self.s5+self.s4+self.s3+self.s2+self.s1

total1=Hexagon(1,2,3,4,5,6)
print(total1.s3)
print(total1.side())

print("/////////////////////////////////////////////////////////")

class Hexagon2:
       
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.ss=[s1,s2,s3,s4,s5,s6]
        
    def side2(self):
        result=0
        for e in self.ss:
            result=result+e
        return result
    
    def sidesum2(self):
        return sum(self.ss)

total2=Hexagon2(1,2,3,4,5,6)
print(total2.ss)
print(total2.side2())
print(total2.sidesum2())

print("/////////////////////////////////////////////////////////")

# エラー（self.s=sではs1~s6変数を作れない）
# [先にs1~s6に数値1~6代入処理が優先される] and [s=1,s=2・・・s=6が更新されているだけ！]
"""
class Hexagon2:
    
    def __init__(self,s1,s2,s3,s4,s5,s6):
        ss=[s1,s2,s3,s4,s5,s6]
        for s in ss:
            self.s=s
            print(s)

    def side2(self):
        result=0
        for e in ss:
            result=result+e
            return result

total2=Hexagon2(1,2,3,4,5,6)
print(total2.s)
print(total2.s6)
print(total2.side2())
"""