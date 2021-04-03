# 4. 
""""
辞書を作成後、任意のキーを入力させるプログラムを書く。そして入力されたキーを
使って、作成した辞書から、バリューを取得して表示する。
"""

works={"IT":"high","Transportation":"middle","Maker":"low"}

print("IT、Transportation、Maker")

guest=input("上記の中で、気になる業界を１つ入力してください：")
print(works[guest])

print("---------------------------------------------------------------")

# 5. 好きな食べ物のジャンルを辞書のキーに入れ、
#    そのバリューとしてそれらの具体的な食べ物をリストでもたせる

sweets=["choco","snack","cake"]
ices=["cup","corn","bar"]
dishs=["スパゲッティ","まぜそば","チャーハン"]

foods={"sweet":sweets,"ice":ices,"dish":dishs}
print(foods)