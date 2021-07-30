import turtle

turtle.Screen().setup(1500, 700)
turtle.Screen().setworldcoordinates(0, 0, 1500, 700)
print("f -- For going 150 units forward")
print("b -- For going backward maintaining same direction")
print("r -- For turning 165 degree to the  right and moving 150 units")
print("l -- For turning 165 degree to the left and moving 150 units")

while True:
    control = input().upper()
    if control == 'F':
        turtle.forward(150)
    elif control == 'B':
        turtle.backward(150)
    elif control == 'R':
        turtle.right(165)
        turtle.forward(150)
    elif control == 'L':
        turtle.left(165)
        turtle.forward(150)
    else:
        pass
