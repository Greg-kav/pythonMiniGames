import turtle
import time
clicks=0
timeLeft=10
gameStart = False
def clickCount(x,y):
    global clicks,gameStart
    if gameStart==True:
       clicks +=1
       clickScore.clear()
       clickScore.write(f"clicks:{clicks}", align="center", font=("Arial", 24, "normal"))
    else:
        return
def timeCountdown(timeLeft):
    gameStart=True
    while timeLeft>0:
        time.sleep(1)
        timeLeft-=1
        Timer.clear()
        Timer.write(f"{timeLeft}", align="center", font=("Arial", 24, "normal"))
    Timer.clear()
    Timer.write(f"Time Stoped", align="center", font=("Arial", 24, "normal"))
Timer=turtle.Turtle()
clickScore=turtle.Turtle()
instractions=turtle.Turtle()
window = turtle.Screen()
window.register_shape(r"C:\Users\info\OneDrive\Desktop\project\SecondPythonApp\clickMe.gif")
window.title("Clicker Game")
window.bgcolor("black")
clickMe=turtle.Turtle()
clickMe.shape(r"C:\Users\info\OneDrive\Desktop\project\SecondPythonApp\clickMe.gif")
clickMe.speed(0)
instractions.hideturtle()
instractions.color("grey")
instractions.penup()
instractions.goto(0,300)
instractions.write(f"the aim of the game is to get the most clicks in the next 10 seconds", align="center", font=("Arial", 24, "normal"))
instractions.goto(0,270)
instractions.write(f"Click on the core and click as many clicks as you can?", align="center", font=("Arial", 24, "normal"))
Timer.hideturtle()
Timer.color("grey")
Timer.penup()
Timer.goto(0,200)
Timer.write(f"Timer", align="center", font=("Arial", 24, "normal"))
clickScore.hideturtle()
clickScore.color("grey")
clickScore.penup()
clickScore.goto(0,-200)
clickScore.write(f"score", align="center", font=("Arial", 24, "normal"))
clickMe.onclick(clickCount)
if (gameStart==False):
    gameStart=True
    timeCountdown(10)
    gameStart=False
window.mainloop()