FONT = ("Courier", 12, "normal")
import turtle
import pandas
from write import Write
from simple import Simple

simple = Simple()
write = Write()

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)


# Reads CSV file containing every state and its coordinates
# Converts this file into a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

# While the length of the correct guesses is lower than the number of U.S. States
# The code will run
while len(guessed_states) < 50:
    # User inputs their guess
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?\nEnter 'Hint' for a Hint").title()
    # If user types "Hint", a randomly generated Hint will pop up
    if answer_state == "Hint":
        write.show_hint()
    # If user enters "Exit" a list of the states they missed will be created
    if answer_state == "Exit":
        write.end_game()
        missing_states = [state for state in all_states if state not in guessed_states]
        # For every state the user misses, it will show up on the map
        for n in missing_states:
            simple.show_missing_states(n)
        # This new list of missed states is converted to a DataFrame
        # The whiile loop breaks
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    # If the user inputs the same answer multiple times
    # It will tell them they are repeating guesses
    elif answer_state in guessed_states:
        write.previous_guess()
    # if User guesses a valid state
    # The states name will pop up on the map
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        simple.show_state(answer_state)


turtle.mainloop()