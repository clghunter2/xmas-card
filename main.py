"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

from turtle import *

def star(x,y,size):
  penup()
  goto(x,y)
  pendown()

  fillcolor('gold')
  begin_fill()

  for x in range(5):
    forward(size)
    right(144)
    forward(size)
    left(72)

  end_fill()


speed(0)
star(0,0,50)
star(-100,150,20)