import turtle
import math

CONV2_RAD = math.pi / 180
MARGIN = .01

class Flower:
    NUM = 2
    ANGLE_PART = 1
    DEG_RANGE = (int) (360 * NUM / ANGLE_PART)
    obj_turtle = turtle.Pen()
    
    def __init__(this, arm=100):
        this.arm = arm     

    def heart_x (self, t):
        return math.cos(t) 
        
    def heart_y (self, t):
        return math.sin(t)
    
    def arm_len (self, t):
        return math.sin(t) *  math.cos(t)    
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
       
        for ang_deg in range (self.ANGLE_PART, self.DEG_RANGE):
            ang = ang_deg * CONV2_RAD
            armlen = self.arm_len(ang)
            
            x_abs = self.heart_x (ang) * self.arm * armlen
            y_abs = - self.heart_y (ang) * self.arm * armlen
            self.obj_turtle.goto(x_abs, y_abs) 

# ------

objFlower = Flower(500)

objFlower.format("yellow", 60)
objFlower.draw()

objFlower.format("blue", 45)
objFlower.draw()

objFlower.format("green", 30)
objFlower.draw()

objFlower.format("red", 10)
objFlower.draw()

input("Wait ...")                