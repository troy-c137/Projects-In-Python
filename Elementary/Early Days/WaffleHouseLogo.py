import turtle

myWorld = turtle.Screen()
waffleHouse = turtle.Turtle()
myWorld.bgcolor('gray')
waffleHouse.color('black')
waffleHouse.fillcolor('gold')
waffleHouse.speed(0)
waffleHouse.hideturtle()

waffleHouse.penup()
waffleHouse.goto(-100,0)

waffleHouse.begin_fill()
for i in range (6):
  waffleHouse.pendown()
  waffleHouse.forward(30)
  waffleHouse.left(90)
  waffleHouse.forward(30)
  waffleHouse.left(90)
  waffleHouse.forward(30)
  waffleHouse.left(90)
  waffleHouse.forward(30)
  waffleHouse.left(90)
  waffleHouse.forward(30)
  waffleHouse.penup()
  waffleHouse.forward(10)
waffleHouse.penup()
waffleHouse.end_fill()

waffleHouse.penup()
waffleHouse.goto(-94,2)
waffleHouse.color('black')
waffleHouse.write('W', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(-50,2)
waffleHouse.color('black')  
waffleHouse.write('A', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(-10,2)
waffleHouse.color('black')
waffleHouse.write('F', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(30,2)
waffleHouse.color('black')
waffleHouse.write('F', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(70,2)
waffleHouse.color('black')
waffleHouse.write('L', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(108,2)
waffleHouse.color('black')
waffleHouse.write('E', font=('Arial',15,"bold"))

waffleHouse.penup()
waffleHouse.goto(-80,-10)
waffleHouse.pendown()

waffleHouse.fillcolor('gold')
waffleHouse.begin_fill()
for i in range (5):
  waffleHouse.forward(30)
  waffleHouse.right(90)
  waffleHouse.forward(30)
  waffleHouse.right(90)
  waffleHouse.forward(30)
  waffleHouse.right(90)
  waffleHouse.forward(30)
  waffleHouse.right(90)
  waffleHouse.forward(30)
  waffleHouse.penup()
  waffleHouse.forward(10)
  waffleHouse.pendown()
waffleHouse.end_fill()

waffleHouse.penup()
waffleHouse.goto(-70,-37)
waffleHouse.color('black')
waffleHouse.write('H', font=('Arial',15,"bold"))

waffleHouse.goto(-31,-37)
waffleHouse.color('black')
waffleHouse.write('O', font=('Arial',15,"bold"))

waffleHouse.goto(10,-37)
waffleHouse.color('black')
waffleHouse.write('U', font=('Arial',15,"bold"))

waffleHouse.goto(50,-37)
waffleHouse.color('black')
waffleHouse.write('S', font=('Arial',15,"bold"))

waffleHouse.goto(90,-37)
waffleHouse.color('black')
waffleHouse.write('E', font=('Arial',15,"bold"))

myWorld.exitonclick()
