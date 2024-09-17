import turtle

angles = int(input("How many angles for the shape? "))

angle = 360/angles
for i in range(angles):
    turtle.forward(30)
    turtle.left(angle)

turtle.done()