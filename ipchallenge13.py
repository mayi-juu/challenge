class Shape:
    def __init__(self,w,l):
        self.width=w
        self.len=l
    
    def size(self):
        print("幅：{} , 長さ：{}".format(self.width,self.len))
