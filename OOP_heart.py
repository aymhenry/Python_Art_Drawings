import turtle
import math

CONV2_RAD = math.pi / 180
MARGIN = .01

class Heart:
    NUM = 6.28 / CONV2_RAD
    ANGLE_PART = 1
    DEG_RANGE = (int) (360 * NUM / ANGLE_PART)
    obj_turtle = turtle.Pen()
    
    def __init__(this, arm=100):
        this.arm = arm     

    def heart_x (self, t):
        return math.cos(t) 
        
    def heart_y (self, t):
        return math.sin(t) - math.sqrt(abs(math.cos(t)))    
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        x_org = self.heart_x(0) * self.arm
        y_org = - self.heart_y(0) * self.arm
        
        self.obj_turtle.penup()
        self.obj_turtle.goto(x_org, y_org)
        self.obj_turtle.pendown()
        
        for ang_deg in range (self.ANGLE_PART, self.DEG_RANGE):
            ang = ang_deg * CONV2_RAD
            
            x_abs = self.heart_x (ang) * self.arm
            y_abs = - self.heart_y (ang) * self.arm
            self.obj_turtle.goto(x_abs, y_abs)

            if ( abs(x_abs - x_org) < MARGIN and abs(y_abs-y_org) < MARGIN and ang_deg != 0):
                break  

# ------

objHeart = Heart(150)
objHeart.format("yellow", 55)
objHeart.draw()

objHeart.format("green", 40)
objHeart.draw()

objHeart.format("blue", 25)
objHeart.draw()

objHeart.format("red", 10)
objHeart.draw()

input("Wait ...")                