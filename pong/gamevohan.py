import turtle
import time
import random

wn= turtle.Screen()
wn.title("pong")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)



#paddle A
pd_A=turtle.Turtle()
pd_A.speed(0)
pd_A.shape('square')
pd_A.color('white')
pd_A.shapesize(stretch_wid=5,stretch_len=1)
pd_A.penup()
pd_A.goto(-350,0)
#paddle B
pd_B=turtle.Turtle()
pd_B.speed(0)
pd_B.shape('square')
pd_B.color('white')
pd_B.shapesize(stretch_wid=5,stretch_len=1)
pd_B.penup()
pd_B.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 2 #d= delta= change =speed
ball.dy = 2

#Function
def pad_A_up():
    y = pd_A.ycor()
    y += 20
    pd_A.sety(y)
def pad_A_down():
    y = pd_A.ycor()
    y -= 20
    pd_A.sety(y)
def pad_B_up():
    y = pd_B.ycor()
    y += 20
    pd_B.sety(y)
def pad_B_down():
    y = pd_B.ycor()
    y -= 20
    pd_B.sety(y)
#keyboard binding(nhap tu ban phim)
wn.listen()
wn.onkeypress(pad_A_up,"w")
wn.onkeypress(pad_A_down,"s")
wn.onkeypress(pad_B_up,"Up")
wn.onkeypress(pad_B_down,"Down")

#main game loop
while True:
    time.sleep(0.01)
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ydegree = random.choice([-1, 1])
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= ydegree
    if ball.xcor() < -390:
        ydegree = random.choice([-1, 1])
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= ydegree
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350 and (ball.ycor() < pd_B.ycor()+35 and ball.ycor() > pd_B.ycor() -35)):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() >-350 and (ball.ycor() < pd_A.ycor()+35 and ball.ycor() > pd_A.ycor() -35)):
        ball.setx(-340)
        ball.dx *= -1 
