import turtle
import random
tao = turtle.Pen()
def square(n) :
    color = ["red", "blue", "green", "purple", "orange","pink", "black"]
    tao.pencolor(random.choice(color))
    tao.pensize(5)
    tao.forward(n)
    tao.left(90)
    tao.forward(n)
    tao.left(90)
    tao.forward(n)
    tao.left(90)
    tao.forward(n)
    tao.left(100)

def draw():
    t = 50
    while t<=300 :
        square(t)
        t = t+10

draw()       
