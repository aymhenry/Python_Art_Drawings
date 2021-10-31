import turtle
import math
t = turtle.Pen()
CONV2_RAD = math.pi / 180
margin = .01
    
def shape01():
    t.clear()
    t.speed(0)
    t.shape("turtle")
    t.pencolor("green")
    t.pensize(2)
    # t.lt(90)

    # input("press enter)")

    for x in range(12):
        for y in range(18):
            t.fd(20)
            t.rt(20)
        t.rt(30)
        t.fd(20)


#----
def shape02(r_outer, r_inner, color = "", is_clear = False):
    if (is_clear): t.clear
    
    angle_part = 1
    num = 150
    t.pensize(1)
    t.penup()
    
    if (color != ""):
        t.pencolor(color)
        
    t.goto(r_outer, 0)
    t.pendown()
    deg_range = (int) (360 * num / angle_part)
    
    for ang_deg in range (deg_range):
        ang = ang_deg * CONV2_RAD
        angle_inner = ang * r_outer / r_inner
        
        x_abs = (r_outer - r_inner) * math.cos(ang) \
                + r_inner * math.cos(angle_inner - ang)
        
        y_abs = r_outer * math.sin(ang) - r_inner * math.sin(angle_inner - ang)
        
        t.goto(x_abs, y_abs)
        
        if ( abs(x_abs - r_outer) < margin and y_abs < margin and ang_deg != 0):
            break
        
#----
def heart ():
    def heart_x (t):
        return math.cos(t) 
        
    def heart_y (t):
        return math.sin(t) - math.sqrt(abs(math.cos(t))) 
    
    num = 6.28 / CONV2_RAD
    angle_part = 1
    deg_range = (int) (360 * num / angle_part)
    arm = 100

    t.pencolor("red")
    t.penup()
    x_org = heart_x(0) * arm
    y_org = - heart_y(0) * arm
    
    t.goto(x_org, y_org)
    t.pendown()
    t.pensize(10)
  
    for ang_deg in range (angle_part, deg_range):
        ang = ang_deg * CONV2_RAD
        x_abs = heart_x (ang) * arm
        y_abs = - heart_y (ang) * arm
        t.goto(x_abs, y_abs)

        if ( abs(x_abs - x_org) < MARGIN and abs(y_abs-y_org) < MARGIN and ang_deg != 0):
            break    


def flower ():
    def heart_x (t):
        return math.cos(t) 
        
    def heart_y (t):
        return math.sin(t)
    
    def arm_len (t):
        return math.sin(t) *  math.cos(t)
        
    NUM = 2
    ANGLE_PART = 2
    DEG_RANGE = (int) (360 * NUM / ANGLE_PART)
    arm = 250

    t.pencolor("red")
    t.penup()
    
    armlen = arm_len(0)
    x_org = heart_x(0) * arm * armlen
    y_org = - heart_y(0) * arm * armlen
    
    t.goto(x_org, y_org)
    t.pendown()
    t.pensize(3)
  
    for ang_deg in range (ANGLE_PART, DEG_RANGE):
        ang = ang_deg * CONV2_RAD
        armlen = arm_len(ang)
        
        x_abs = heart_x (ang) * arm * armlen
        y_abs = - heart_y (ang) * arm * armlen
        t.goto(x_abs, y_abs)

        #if ( abs(x_abs - x_org) < MARGIN and abs(y_abs-y_org) < MARGIN and ang_deg != 0):
        #    break 

# -------------------------------------        
shape01()
# shape02(160, 65, "green", True)
# shape02(65, 160, "red")
# shape02(30, 170, "red")
# shape02(15, 168, "red")  # very good

# heart() # good
# flower() 
input("press enter") 


