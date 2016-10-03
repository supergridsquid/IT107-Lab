import turtle

s = input("How long are the polygon sides?: ")
s = int(s)
#go to start point
turtle.forward(500)
turtle.left(180)
turtle.forward(1000)

#triangle
turtle.right(120)
turtle.forward(s)
turtle.right(120)
turtle.forward(s)
turtle.left(60)
turtle.forward(s)

#square
turtle.left(90)
turtle.forward(s)
turtle.right(90)
turtle.forward(s)
turtle.right(90)
turtle.forward(s)
turtle.left(90)
turtle.forward(s)

#pentagon
turtle.left(108)
turtle.forward(s)
turtle.right(72)
turtle.forward(s)
turtle.right(72)
turtle.forward(s)
turtle.right(72)
turtle.forward(s)
turtle.left(108)
turtle.forward(s)

#hexagon
turtle.left(120)
turtle.forward(s)
turtle.right(60)
turtle.forward(s)
turtle.right(60)
turtle.forward(s)
turtle.right(60)
turtle.forward(s)
turtle.right(60)
turtle.forward(s)
turtle.left(120)
turtle.forward(s+15)

#septagon
turtle.left(128.57)
turtle.forward(s)
turtle.right(51.73)
turtle.forward(s)
turtle.right(51.73)
turtle.forward(s)
turtle.right(51.73)
turtle.forward(s)
turtle.right(51.73)
turtle.forward(s)
turtle.right(51.73)
turtle.forward(s)


turtle.done()
