from turtle import *
# speed(10)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# for i in range(500):
#     forward(i)
#     left(91)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    # width(x / 100 + 1)
    forward(x)
    left(59)
done()
