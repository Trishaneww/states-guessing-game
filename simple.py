FONT = ("Courier", 12, "normal")
from turtle import Turtle
import pandas
data = pandas.read_csv("50_states.csv")

class Simple(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,290)

    def show_missing_states(self, banana):
        self.hideturtle()
        self.penup()
        state_data = data[data.state == banana]
        self.goto(int(state_data.x), int(state_data.y))
        self.color("red")
        self.write(banana)

    def show_state(self, minion):
        self.hideturtle()
        self.penup()
        state_data = data[data.state == minion]
        self.goto(int(state_data.x), int(state_data.y))
        self.write(minion)