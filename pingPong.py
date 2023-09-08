import turtle

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor('#000000')
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('#FFFFFF')
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.shapesize(stretch_wid=5, stretch_len=1)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('#FFFFFF')
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(stretch_wid=5, stretch_len=1)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape('square')
Ball.color('#FFFFFF')
Ball.penup()
Ball.goto(0, 0)
Ball.shapesize(stretch_wid=1, stretch_len=1)
Ball.dx = 0.1
Ball.dy = 0.1

#Functions


def PadAUp():
    y = paddleA.ycor()
    if y < 240:
        y += 20
    paddleA.sety(y)


def PadADown():
    y = paddleA.ycor()
    if y > -240:
        y -= 20
    paddleA.sety(y)


def PadBUp():
    y = paddleB.ycor()
    if y < 240:
        y += 20
    paddleB.sety(y)


def PadBDown():
    y = paddleB.ycor()
    if y > -240:
        y -= 20
    paddleB.sety(y)


#key board bind

wn.listen()
wn.onkeypress(PadAUp, "w")
wn.onkeypress(PadADown, "s")
wn.onkeypress(PadBUp, "Up")
wn.onkeypress(PadBDown, "Down")

while True:
    wn.update()


    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    if Ball.xcor() > 390:
        Ball.setx(0)
        Ball.sety(0)
        Ball.dx *= -1

    if Ball.xcor() < -390:
        Ball.setx(0)
        Ball.sety(0)
        Ball.dx *= -1

    if Ball.ycor() > 290:
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.dy *= -1

    if (Ball.xcor() < paddleA.xcor() + 10) and (Ball.xcor() > paddleA.xcor() -10) and (Ball.ycor() < paddleA.ycor() + 50) and (Ball.ycor() > paddleA.ycor() - 50):
        Ball.dx *= -1
    if (Ball.xcor() < paddleB.xcor() + 10) and (Ball.xcor() > paddleB.xcor() -10) and (Ball.ycor() < paddleB.ycor() + 50) and (Ball.ycor() > paddleB.ycor() - 50):
        Ball.dx *= -1
