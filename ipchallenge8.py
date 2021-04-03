# 2. import_file

def judge(n):
    if n<4:
        print("数値は4未満です")
    else:
        def big(n):
            print("数値は"+str(n)+"です")
        big(n)

if __name__=="__main__":
    print(judge(128))
    print(judge(2))
    print(big(2))