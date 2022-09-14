FONT = ("Courier", 24, "normal")
hints = ["New York", "Atlanta", "Seattle", "Denver", "Dallas", "Phoenix", "Breaking Bad", "San Fransisco", "Charlotte", "Milwaukee",
          "Miami", "Cleveland", "Chicago", "St.Louis", "Salt Lake City", "Philly", "New Orleans", "Hawkins", "Polar Bear"]
from turtle import Turtle
import random
import time


class Write(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,290)

    def show_hint(self):
        self.goto(0,290)
        self.color("light blue")
        self.write(arg=random.choice(hints), align="center", font=FONT)
        time.sleep(3)
        self.clear()

    def end_game(self):
        self.goto(0,290)
        self.color("green")
        self.write(arg="Heres What You Missed", align="center", font=FONT)

    def previous_guess(self):
        self.goto(0,290)
        self.color("red")
        self.write(arg="You already guessed this state",align="center", font=FONT)
        time.sleep(2)
        self.clear()



