import random
import copy


class Hat:
    def __init__(self,**colours):
        self.colours = colours
        self.x =[]
        for colour, value in colours.items():
            for i in range(value):
                self.x+=[colour]
        self.contents =copy.copy(self.x)

    def draw(self,num):
        if num >len(self.x):
            return self.x
        out=[]
        self.contents = copy.copy(self.x)


        for i in range(num):
            j= random.randint(0,len(self.contents)-1)
            out+=[self.contents[j]]
            self.contents.pop(j)
        return out
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m=0
    for exp in range(num_experiments):
        k=hat.draw(num_balls_drawn)
        present=False
        for key,value in expected_balls.items():
            if k.count(key) >= value:
                present=True
            else:
                present=False
                break
        if present:
            m+=1
    return m/num_experiments




hat1 = Hat(red=3,blue=2,green=7)
print(experiment(hat1,{"red":1,"blue":1,"green":3},5,2000))