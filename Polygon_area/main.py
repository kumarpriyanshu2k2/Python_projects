class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.picture=""
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.height>50 or self.width>50:
            print("Too big for picture.")
        else:
            for i in range(self.height):
                    self.picture += "*"*self.width+"\n"
        return self.picture
    def get_amount_inside(self,obj):
        rows = self.height//obj.height
        columns= self.width//obj.width
        return int(rows*columns)
class Square(Rectangle):
    def __init__(self,side):
        self.side =side
        super().__init__(self.side,self.side)

    def __str__(self):
        return f"Square(side={self.side})"
    def set_side(self,side):
        self.side=side
        self.width = side
        self.height = side
    def set_height(self,height):
        self.set_side(height)
    def set_width(self,width):
        self.set_side(width)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(51)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())


rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
