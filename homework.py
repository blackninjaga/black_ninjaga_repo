import turtle


def draw_orbit(orbit):
    t.goto(0, orbit * (-1))
    t.down()
    t.circle(orbit)
    t.up()

solar_system = [30,4.87,12.10,12.72,6.77 ,139.82, 116.46, 50.72, 49.24]
solar_system_distance = [0, 20, 36, 50, 76, 260, 475, 600, 750, 0]
solar_system_colors = ['#ffcc00','#8585ad', '#ff6600', '#6699ff', '#804000', '#ff9933', '#ff9966', '#1a53ff',
                       '#1a53ff']

t = turtle.Pen()
t.speed(10)
turtle.Screen().bgcolor("black")

t.pencolor("yellow")

for x in range(9):
    draw_orbit(solar_system_distance[x])
    t.up
    t.goto(solar_system_distance[x], 0)
    t.dot(solar_system[x], solar_system_colors[x])
    t.down

turtle.mainloop()