import turtle
import random
import math

turtle.Screen().bgcolor("black")

solar_system = {"Sun": 30, "Mercury": 4.87, "Venus": 12.10,
                "Earth": 12.72, "Mars": 10.77, "Jupiter": 139.82,
                "Saturn": 60, "Uranus": 50.72, "Neptune": 49.24}

solar_system_distance = [0, 20, 36, 50, 76, 210, 325, 400, 500, 0]
solar_system_colors = ["#ffcc00", "#8585ad", "#ff6600", "#6699ff",
                       "#804000", "#ff9966", "#ff9933", "#ff8000",
                       "#1a53ff"]
for x in solar_system:
    print("{0} - {1}".format(x, solar_system[x]))

turtle.pencolor("yellow")
turtle.speed(10)

i = 0

for x in solar_system:
    r = solar_system_distance[i + 1] / 2
    rand = random.randrange(0, 360)
    kek1 = int(r * math.cos(rand))
    kek2 = int(r * math.sin(rand))
    print(kek1, kek2)

    turtle.dot(solar_system[x], str(solar_system_colors[i]))

    # Saturn circles
    if (x == 'Saturn'):
        turtle.goto(turtle.xcor(), turtle.ycor()-55)
        turtle.down()
        turtle.pensize(8)
        turtle.pencolor('#545559')
        turtle.circle(55)
        turtle.up()
        turtle.goto(turtle.xcor(), turtle.ycor() - 12)
        turtle.down()
        turtle.pencolor('#2a292b')
        turtle.circle(67)
        turtle.up()
        turtle.pensize(1)
        turtle.color('yellow')

    i += 1
    turtle.up()
    turtle.goto(0, (solar_system_distance[i] * (-1)))
    turtle.down()
    turtle.circle(solar_system_distance[i])
    turtle.up()
    turtle.goto(kek1 * 2, kek2 * 2)

turtle.mainloop()
