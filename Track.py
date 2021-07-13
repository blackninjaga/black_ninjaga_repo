import turtle, random
from turtle import *

number = int(input("Введи число дорожек: "))
length = []
for i in range(number):
    length.append(int(input("Введи длину дорожки № " + str(i) + ": ")))

colors  = ["red","green","blue","orange","purple","pink"]
speed(6)
right(90)
up()
for n in range(number):
    l = length[n]
    goto((n - 1) * 20 / 2, l / 2)
    color("black")
    pendown()
    write(n)
    color(random.choice(colors))
    fd(l)
    penup()

hideturtle()
turtle.Screen().exitonclick()