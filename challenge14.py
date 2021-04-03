# 1. and 2.
"""
正方形の一辺の長さをインスタンス変数に持つSquareクラスを定義し、Square_listクラス変数を追加する。
そして、Squareクラスのオブジェクトが作られるたびに、そのオブジェクトをリストに追加する。
さらに、Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さが出力されるようにする。
"""

class Square:
    square_list=[]

    def __init__(self,side):
        self.side=side
        self.square_list.append([self.side])

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side,self.side,self.side,self.side)

square1=Square(1)
square2=Square(2)
square3=Square(3)
square4=Square(4)

print(Square.square_list)
print(square1.square_list)
print(square3)

print("......................................................")

# 3. 2つのパラメーターを受け取る関数を書く。
# この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseを返す。

def kakunin():
    p1=input("1つ目のパラメーターを入力してください：")
    p2=input("2つ目のパラメーターを入力してください：")

    if p1 is p2:
        return True
    elif p1 == p2:
        return "同一オブジェクトではない"
    else:
        return p1+p2

print(kakunin())

# =「=（イコール）」と「同じオブジェクト」は意味が全然違う！！