import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif" # This is basically the path to reach my image, and it will be the shape
                              # that I am going to load into my screen by using the addshape() method
screen.addshape(image)
turtle.shape(image)




data = pd.read_csv("50_states.csv")
# print(data)
allStates = data["state"].to_list()
guessedStates = []

while len(guessedStates) < 50:
    # This method allows to inquire the user for an answer. It creates one of those popup boxes, I can provide a title and a prompt
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What is the next state's name?").title()
    # print(answerState)

    if answerState == "Exit":
        missedStates = [missState for missState in allStates if missState not in guessedStates]

        newData = pd.DataFrame(missedStates)
        newData.to_csv("missingStates.csv")
        break

    if answerState in allStates:
        # print("It exists")
        guessedStates.append(answerState)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup() # To preclude doing any drawing
        stateData = data[data.state == answerState] # This line allows to get hold an entire row that corresponds the user input
        state.goto(int(stateData.x), int(stateData.y))
        # state.write(answerState)
        state.write(stateData.state.item()) # The alternative way to retrieve a certain state. The method
                                 # series.item() returns the first element of the underlying data as a python scalar
        """ This way allows to get a row of data from a data frame and then get a particular value from that row,
        and get the actual raw value from that."""



screen.exitonclick()
