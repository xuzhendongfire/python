import turtle

#设置回执日期长度和间隔
le = 50
itv = 20

#定义数字，传入（x,y）和number
def drowDate(x,y,n):
    d = turtle.Turtle()
    d.speed(5)
    d.pensize(10)
    
    d.color("red")
    d.hideturtle()
    d.penup()
    d.goto(x,y)#画笔移动到起点
    d.pendown()
    #绘制 从上到下，从左到右
    #第一横
    if n==0 or n==2 or n==3 or n==5 or n==6 or n==7 or n==8 or n==9:
        d.forward(le)
    
    #第一竖
    if n==0 or n==4 or n==5 or n==6 or n==8 or n==9:
        xx = x
        yy = y
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.right(90)
        d.forward(le)
        d.left(90)
        
    #第二竖
    if n==0 or n==1 or n==2 or n==3 or n==4 or n==7 or n==8 or n==9:
        xx = x+le
        yy = y
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.right(90)
        d.forward(le)
        d.left(90)
        

    #第二横
    if n==2 or n==3 or n==4 or n==5 or n==6 or n==8 or n==9:
        xx = x
        yy = y - le
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.forward(le)

    #第三竖
    if n==0 or n==2 or n==6 or n==8:
        xx = x
        yy = y - le
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.right(90)
        d.forward(le)
        d.left(90)
        
    #第四竖
    if n==0 or n==1 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
        xx = x + le
        yy = y - le
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.right(90)
        d.forward(le)
        d.left(90)
        
    #第三横
    if n==0 or n==2 or n==3 or n==5 or n==6 or n==8:
        xx = x
        yy = y - le*2
        d.penup()
        d.goto(xx,yy)#画笔移动
        d.pendown()
        d.forward(le)


#接收日期（暂不做判断）
date = str(input("麻利点，快输入日期（如20171123）:"))
turtle.setup(1000,800,0,0)#定义画布大小
x = -4*(le+itv)
y = le
for i in date:
    drowDate(x,y,int(i))
    x = x+le+itv


