#Doubt Checking

class bye():
    def __init__(self):
        self.x="x"
        self.y='y'
    def __display(self):
        print self.x
    def __str__(self):
        return self.y #Private Function
class aloha(bye):
    def __init__(self):
        bye.__init__(self)


a=bye()
print a
b=aloha()
print b
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return (x,y)
a=Point(0,1)
b=Point(5,3)
print a+b
