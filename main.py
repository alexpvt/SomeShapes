import turtle as t

tim = t.Turtle()
win = t.Screen()

tim.speed(0.1)
tim.penup()
tim.goto(-70, 250)
tim.pendown()
win.bgcolor("pale green")
win.title("SomeShapes")

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for ranges in range(3, 17):
    draw_shapes(ranges)

win.exitonclick()