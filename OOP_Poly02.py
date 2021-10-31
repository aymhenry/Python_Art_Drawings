import turtle
import math

CONV2_RAD = math.pi / 180
MARGIN = .01

class Poly02:
    NUM = 1
    ang_step = 30
    deg_range = 0
    obj_turtle = turtle.Pen()
    
    def __init__(this, arm=100, ang=15, count=None):
        this.arm = arm     
        this.ang = ang
        this.part = (int) (360 / this.ang )
        this.count = count
        
        if (count == None):
            this.count = this.part 
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        # x_org = self.arm
        # y_org = 0
        self.obj_turtle.degrees()
        
        for count in range (self.count):
            ang = count * self.ang * CONV2_RAD
            
            x_value = self.arm * math.sin(ang)
            y_value = self.arm * math.cos(ang)
                           
            for dcount in range(count, int(self.part)):
                ang = dcount * self.ang * CONV2_RAD
                x_value2 = self.arm * math.sin(ang)
                y_value2 = self.arm * math.cos(ang)

                self.obj_turtle.penup()
                self.obj_turtle.goto(x_value, y_value)
                self.obj_turtle.pendown()             
                
                self.obj_turtle.goto(x_value2, y_value2)
      
            
            # if ( abs(x_abs - x_org) < MARGIN and abs(y_abs-y_org) < MARGIN and ang_deg != 0):
            #    break  

# ------

objPoly02 = Poly02(200, 360/60, 2)
objPoly02.format("red", 1)
#objPoly02.draw()

objPoly02 = Poly02(200, 360/15)
objPoly02.format("blue", 2)
objPoly02.draw()


input("Wait ...")                