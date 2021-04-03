from ipchallenge13 import Shape

class Square(Shape):
    def area(self):
        return self.width*self.len

    def size(self):
        print("変更後　幅：{} , 長さ：{}".format(self.width,self.len))
"""
square=Square(15,25)
square.size()
"""