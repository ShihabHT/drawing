import turtle

turtle.Screen().setup(1500, 700)
turtle.Screen().setworldcoordinates(0, 0, 1500, 700)

x = str(turtle.pos())
turtle.goto(350, 350)
print(turtle.pos())
while True:
    turtle.forward(200)
    turtle.right(90)
    print(turtle.pos())
    if str(turtle.pos()) == '(350.00,350.00)':
        break
turtle.done()