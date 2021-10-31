import turtle
import math

CONV2_RAD = math.pi / 180
MARGIN = .01

class Shape:
    NUM = 6.28 / CONV2_RAD
    ANGLE_PART = 1
    DEG_RANGE = (int) (360 * NUM / ANGLE_PART)
    obj_turtle = turtle.Pen()
    
    def __init__(this, r_outer, r_inner):
        this.r_outer = r_outer     
        this.r_inner = r_inner     

    def heart_x (self, t):
        return math.cos(t) 
        
    def heart_y (self, t):
        return math.sin(t) - math.sqrt(abs(math.cos(t)))    
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        x_org = self.r_outer
        y_org = 0
        
        self.obj_turtle.penup()
        self.obj_turtle.goto(x_org, y_org)
        self.obj_turtle.pendown()
        
        for ang_deg in range (self.ANGLE_PART, self.DEG_RANGE):
            ang = ang_deg * CONV2_RAD
            
            angle_inner = ang * self.r_outer / self.r_inner
            
            x_abs = (self.r_outer - self.r_inner) * math.cos(ang) \
                    + self.r_inner * math.cos(angle_inner - ang)
            
            y_abs = self.r_outer * math.sin(ang) - self.r_inner * math.sin(angle_inner - ang)
            
            self.obj_turtle.goto(x_abs, y_abs)
            
            if ( abs(x_abs - self.r_outer) < MARGIN and y_abs < MARGIN and ang_deg != 0):
                break  
            

# ------

objShape = Shape(160, 65)
objShape.format("yellow", 8)
objShape.draw()

objShape.format("red", 1)
objShape.draw()

input("Wait ...")                