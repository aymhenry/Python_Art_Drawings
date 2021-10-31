import turtle
import math
MARGIN = .01

class Shape:
    obj_turtle = turtle.Pen()
    
    def __init__(this, step=20, rot=30, num =1):
        this.step = step     
        this.rot = rot        
        this.num = num        
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        x_steps = (int) (360/self.rot)
        y_steps = (int) (360/self.step)
        
        for x in range(x_steps * self.num ):
            for y in range(y_steps):
                self.obj_turtle.fd(self.step)
                self.obj_turtle.rt(self.step)
            self.obj_turtle.rt(self.rot)
            self.obj_turtle.fd(self.step)
                     

# ------

objShape = Shape()
objShape.format("blue", 2)
# objShape.draw()

objShape = Shape(80, 120, 3)
objShape.format("red", 2)
# objShape.draw()

objShape = Shape(120, 80, 3)
objShape.format("red", 2)
objShape.draw()  
input("Wait ...")
         