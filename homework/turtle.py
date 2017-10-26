import turtle
t = turtle.Pen()

def star(n):
    for i in range(n):
        t.up()
        t.goto(0,0)
        t.right(360/n)
        t.forward(100)
        for j in range (5):
            t.down()
            t.right(144)
            t.forward(30)
star(10)
