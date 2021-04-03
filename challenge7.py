# 2. 25から50までの数値をそれぞれ出力する。

for number in range(25,51):
    print(number)

print("---------------------------------------------------------------")

# 3. 次のリストの要素をそれぞれ、インデックス値と一緒に出力する。
# ["engineer","specialist","generalist"]

works=["engineer","specialist","generalist"]
i=0
for work in works:
    print(str(i)+":"+work)
    i += 1

print("---------------------------------------------------------------")

# 4. p116参照

print("qを入力すると終了します。")

kirisute=[0,1,2,3,4]

while True:
    user=input("四捨五入で切り捨てとなる数値をどれか入力してください：")
    try:
        if user=="q":
            print("数字当てクイズを終了します。")
            break
        elif int(user) in kirisute:
            print("正解")
        else:
            print("不正解")
    except(ValueError):
        print("qか数値を入力してください")

# int(user)をqの条件より先に入力してしまうと、エラー発生（qはint(整数)ではない）
# 数値（整数）かどうかの判断→intを使う

print("---------------------------------------------------------------")

# 5. 2つのリストに含まれる全ての数字の組み合わせで掛け算する。
# そしてその結果を新しいリストに格納し、出力する。

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result=[]

for i in list1:
    for j in list2:
        result.append(i*j)

print(len(result))
print(result)