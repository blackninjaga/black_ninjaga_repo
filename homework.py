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

Sun = 30
Mercury = 4.87
Venus = 12.10
Earth = 12.72
Mars = 6.77
Jupiter = 139.82
Saturn = 116.46
Uranus = 50.72
Neptune = 49.24

Sun_color = "#ffcc00"
Mercury_color = "#8585ad"
Venus_color = "#ff6600"
Earth_color = "#6699ff"
Mars_color = "#804000"
Jupiter_color = "#ff9966s"
Saturn_color = "#ff9933"
Uranus_color = "#ff8000"
Neptune_color = "#1a53ff"

t = turtle.Pen()
t.speed(0)
turtle.Screen().bgcolor("black")

Sun_orb = 0
Mercury_orb = 20
Venus_orb = 36
Earth_orb = 50
Mars_orb = 76
Jupiter_orb = 260
Saturn_orb = 475
Uranus_orb = 600
Neptune_orb = 750

t.pencolor("yellow")
draw_orbit(Sun_orb)
draw_orbit(Mercury_orb)
draw_orbit(Venus_orb)
draw_orbit(Earth_orb)
draw_orbit(Mars_orb)
draw_orbit(Jupiter_orb)
draw_orbit(Saturn_orb)
draw_orbit(Uranus_orb)
draw_orbit(Neptune_orb)

for x in range(9):
    t.up
    t.goto(solar_system_distance[x], 0)
    t.dot(solar_system[x], solar_system_colors[x])
    t.down

turtle.mainloop()