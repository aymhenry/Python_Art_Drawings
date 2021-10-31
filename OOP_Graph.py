import turtle
import math
import time

MARGIN = .01
CONV2_RAD = math.pi / 180

class Base:
    obj_turtle = turtle.Pen()
    m_status = True
    
    def __init__(this, x_org=0, y_org=0):
        this.obj_turtle.penup()
        this.obj_turtle.goto(x_org, y_org)
        this.obj_turtle.pendown()
        
        turtle.onkey(this.reset, 'space')
        
        # to listen by the turtle
        turtle.listen()

    def setflag(self):
        self.m_status = True
    
    def reset(self):
        self.clearScr()
        self.m_status = False
    
    def clearScr(self):
        self.obj_turtle.clear()
        
    def pause(self):
        if (not (self.m_status)): 
            return
        time.sleep(5)
        print (self.m_status)
        self.reset()

class Poly02(Base):
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
        self.setflag()
        self.obj_turtle.degrees()
        
        for count in range (self.count):
            ang = count * self.ang * CONV2_RAD
            
            x_value = self.arm * math.sin(ang)
            y_value = self.arm * math.cos(ang)
                           
            for dcount in range(count, int(self.part)):
                if (not (self.m_status)): 
                    return
                    
                ang = dcount * self.ang * CONV2_RAD
                x_value2 = self.arm * math.sin(ang)
                y_value2 = self.arm * math.cos(ang)

                self.obj_turtle.penup()
                self.obj_turtle.goto(x_value, y_value)
                self.obj_turtle.pendown()             
                
                self.obj_turtle.goto(x_value2, y_value2)
        
    
class Shape(Base):

    def __init__(this, step=20, rot=30, num =1, x_org=0, y_org=0):
        super().__init__(x_org, y_org)
        
        this.step = step     
        this.rot = rot        
        this.num = num        
    
    def format(self, color, size):
        self.obj_turtle.pencolor(color)
        self.obj_turtle.pensize(size)
        
    def draw(self):
        if (not (self.m_status)): 
            return
        self.setflag()
        x_steps = (int) (360/self.rot)
        y_steps = (int) (360/self.step)
        
        for x in range(x_steps * self.num ):
            for y in range(y_steps):
                if (not (self.m_status)): 
                    return
                    
                self.obj_turtle.fd(self.step)
                self.obj_turtle.rt(self.step)
            self.obj_turtle.rt(self.rot)
            self.obj_turtle.fd(self.step)
                     

# ------
objShape = Shape(80, 120, 3)
objShape.format("red", 2)
objShape.draw()
objShape.pause()

objShape = Shape(50, 30, 2)
objShape.format("blue", 2)
objShape.draw()
objShape.pause()

objShape = Shape(50, 75, 8)
objShape.format("green", 2)
objShape.draw() 
objShape.pause() 

# --------------------------
objPoly02 = Poly02(200, 360/60, 2)
objPoly02.format("red", 1)
objPoly02.draw()
objShape.pause()

objPoly02 = Poly02(200, 360/15)
objPoly02.format("blue", 2)
objPoly02.draw()
objShape.pause()

input("Wait ...")
         