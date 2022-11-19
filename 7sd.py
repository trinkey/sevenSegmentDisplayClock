from datetime import datetime
from time import sleep, time
from turtle import Screen, Turtle

twelveHour = True

offset = [-310, -190, -60, 60, 190, 310]
connections = [[[-50, 75], [50, 75]], [[-50, 75], [-50, 0]], [[50, 75], [50, 0]], [[-50, 0], [50, 0]], [[-50, 0], [-50, -75]], [[50, 0], [50, -75]], [[-50, -75], [50, -75]]]
numbers = {"0": [0, 1, 2, 4, 5, 6], "1": [2, 5], "2": [0, 2, 3, 4, 6], "3": [0, 2, 3, 5, 6], "4": [1, 2, 3, 5], "5": [0, 1, 3, 5, 6], "6": [0, 1, 3, 4, 5, 6], "7": [0, 2, 5], "8": [0, 1, 2, 3, 4, 5, 6], "9": [0, 1, 2, 3, 5]}

screen = Screen()
turtle = Turtle()

screen.setup(800, 200)
screen.tracer(0)
screen.bgcolor("#222222")

turtle.pu()
turtle.hideturtle()
turtle.color("#ff0000")
turtle.pensize(7)

def updateNumbers(currentTime):
    try:
        for i in [-125, 125]:
            for o in [-50, 50]:
                turtle.goto(i, o)
                turtle.dot(10)
        
        turtle.color("#2a2a2a")
        for o in range(6):
            for i in numbers["8"]:
                turtle.goto(connections[i][0][0] + offset[o], connections[i][0][1])
                turtle.pd()
                turtle.goto(connections[i][1][0] + offset[o], connections[i][1][1])
                turtle.pu()
        
        turtle.color("#ff0000")
        for o in range(6):
            for i in numbers[currentTime[o]]:
                turtle.goto(connections[i][0][0] + offset[o], connections[i][0][1])
                turtle.pd()
                turtle.goto(connections[i][1][0] + offset[o], connections[i][1][1])
                turtle.pu()
        screen.update()
        turtle.clear()
    except: pass

while True:
    if twelveHour:
        updateNumbers([i for i in (str(datetime.fromtimestamp(round(time())))[11:].replace(":", "") if int(str(datetime.fromtimestamp(round(time())))[11:].replace(":", "")) - 12 < 0 else ("0" + str(int(str(datetime.fromtimestamp(round(time())))[11:].replace(":", "")) - 120000) if len(str(int(str(datetime.fromtimestamp(round(time())))[11:].replace(":", "")) - 120000)) == 5 else str(int(str(datetime.fromtimestamp(round(time())))[11:].replace(":", "")) - 120000)))])
    else:
        updateNumbers([i for i in str(datetime.fromtimestamp(round(time())))[11:].replace(":", "")])
    sleep(.05)
