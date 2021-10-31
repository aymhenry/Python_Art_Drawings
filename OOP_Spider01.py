import turtle
import math

CONV2_RAD = math.pi / 180

class Spider:
    obj_turtle = turtle.Pen()
    
    def __init__(this, radius, step_deg, shape = True):
        this.radius = radius     
        this.step_deg = step_deg  
        this.shape = shape  
                
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        

    def right2left (self, step_outer, direc = -1):
        if (self.shape):
            intFrom = 360
            intTo = 0
            intStep = -10
        else:
            intFrom = 0
            intTo = 360
            intStep = 10
            
        for ang_deg in range (intFrom, intTo, intStep):
                
            ang = ang_deg  * CONV2_RAD

            arm_base = ang * self.radius
            ang_extar = ang_deg + (self.step_deg * step_outer) 

            x_abs = direc * arm_base * math.cos(ang_extar * CONV2_RAD) 
            y_abs =  arm_base * math.sin(ang_extar * CONV2_RAD) 
                 
            self.obj_turtle.goto(x_abs, y_abs)
    
    def draw(self):
      
        NUM = (int) (360/ self.step_deg)
    
        for step_outer in range (NUM):
            self.obj_turtle.penup()
            self.obj_turtle.goto(0, 0)
            self.obj_turtle.pendown()
  
            # for ang_deg in range (intFrom, intTo, intStep):
            self.right2left (step_outer, 1)
            self.right2left (step_outer, -1)
    
# ------

# objShape = Spider(50, 20, True)
# objShape.format("yellow", 8)
# objShape.draw()

objShape = Spider(50, 22, True)
objShape.format("red", 1)
objShape.draw()

# objShape = Spider(30, 20, False)
# objShape.format("red", 1)
# objShape.draw()

input("Wait ...")                