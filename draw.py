import turtle

# turtle.Screen().setup(1500, 700)
# turtle.Screen().setworldcoordinates(0, 0, 1500, 700)
print("f -- For going 150 units forward")
print("b -- For going backward maintaining same direction")
print("r -- For turning 165 degree to the  right and moving 150 units")
print("l -- For turning 165 degree to the left and moving 150 units")

t = turtle.Turtle()
turtle.Screen().setup(1000, 700)
# turtle.tracer()

while True:
    control = input().upper()
    if control == 'F':
        t.forward(150)
    elif control == 'B':
        t.backward(150)
    elif control == 'R':
        t.right(165)
        t.forward(150)
    elif control == 'L':
        t.left(165)
        t.forward(150)
    elif control == 'X':
        break
    else:
        pass
turtle.update()
turtle.mainloop()

