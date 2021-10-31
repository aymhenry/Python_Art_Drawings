import turtle
import math

CONV2_RAD = math.pi / 180
MARGIN = .01

class Poly:
    NUM = 1
    ang_step = 30
    deg_range = 0
    obj_turtle = turtle.Pen()
    
    def __init__(this, arm=100, ang=15, part=20):
        this.arm = arm     
        this.ang = ang
        this.part = part
        this.deg_range = (int) (360 * this.NUM )   
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        # x_org = self.arm
        # y_org = 0
        self.obj_turtle.degrees()
        # self.obj_turtle.speed(1)
        
        # self.obj_turtle.setpos(x_org, y_org)
        
        for ang_deg in range (0, self.deg_range, self.ang_step):
            ang = ang_deg * CONV2_RAD
            
            self.obj_turtle.penup()
            self.obj_turtle.goto(self.arm * math.sin(ang), self.arm * math.cos(ang))
            self.obj_turtle.pendown()
            
            for count in range(int(360 / self.ang)):
                self.obj_turtle.right(self.ang )
                self.obj_turtle.fd(self.part)
      
            
            # if ( abs(x_abs - x_org) < MARGIN and abs(y_abs-y_org) < MARGIN and ang_deg != 0):
            #    break  

# ------

objPoly = Poly(140, 360/6, 80)
objPoly.format("yellow", 20)
objPoly.draw()

objPoly.format("green", 12)
objPoly.draw()

objPoly.format("blue", 6)
objPoly.draw()

objPoly.format("red", 1)
objPoly.draw()

input("Wait ...")                