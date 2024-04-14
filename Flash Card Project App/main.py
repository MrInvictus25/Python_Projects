from tkinter import *
import pandas
import random


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Garret"
FONT_COLOR_RUSSIAN = "#12372A"    # "#436850"
FONT_COLOR_ENGLISH = "#FEFBF6" #"#FBFADA"
currentCard = {}
toLearn = []
# ---------------------------- READING FILES ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_comprehend.csv")  # The file with unknown words
    toLearn = data.to_dict(orient="records")
    print(toLearn)
except FileNotFoundError:  # If we cannot find a file, we are going to open the original one
    originalData = pandas.read_csv("data/russian_words.csv")
    toLearn = originalData.to_dict(orient="records")
    print(toLearn)
#else:
    #toLearn = data.to_dict(orient="records")
    # print(toLearn)

# ---------------------------- NEXT CARD ------------------------------- #
def nextCard():
    global currentCard, flipTimer
    window.after_cancel(flipTimer) # When we click to have access to a new card, we are going to invalidate this timer
    currentCard = random.choice(toLearn) # Picking up a random item from a consolidated list with dictionaries
    #print(currentCard["Russian"])  # Extracting a word from "Russian" column
    canvas.itemconfig(cardTitle, text="Russian", fill=FONT_COLOR_RUSSIAN)
    canvas.itemconfig(cardWord, text=currentCard["Russian"], fill=FONT_COLOR_RUSSIAN)
    canvas.itemconfig(cardBackground, image=cardFrontImage)  # Changing a background to front image
    flipTimer = window.after(3000, func=flipCard) # This method allows to flip a card after termination of 3 seconds

# ---------------------------- FLIP CARD ------------------------------- #
# This function is going to take care of changing the card to show the English word for the current card and
# alternate an image from card front to card back
def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill=FONT_COLOR_ENGLISH)
    canvas.itemconfig(cardWord, text=currentCard["English"], fill=FONT_COLOR_ENGLISH)
    canvas.itemconfig(cardBackground, image=cardBackImage)  # Changing a front to background image

# ---------------------------- IS COMPREHENDED ------------------------------- #
# This function is going to remove the current card from the cards that are in the list of words to learn
def isComprehended():
    toLearn.remove(currentCard)
    print(len(toLearn))
    data = pandas.DataFrame(toLearn)
    data.to_csv("data/words_to_comprehend.csv", index=False)  # This does not add the index number to our newly created list

    """In order to keep hold of the words that I still need to learn, I have to save this list to a new permanent file
        each time the user clicks on this isComprehended button."""
    nextCard()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # bg - background
flipTimer = window.after(3000, func=flipCard)  # this method is used to calculate the time intervals for the functions in the application parallel


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) # Canvas object allows us to lay out
                                                                                # a lot of things on top of each other

cardFrontImage = PhotoImage(file="images/card_front.png")
cardBackImage = PhotoImage(file="images/card_back.png")
cardBackground = canvas.create_image(400, 263, image=cardFrontImage)
cardTitle = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill=FONT_COLOR_RUSSIAN)  # Creating a variable to embed words into pieces of text in the canvas
cardWord = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill=FONT_COLOR_RUSSIAN)  # Creating a variable to embed words into pieces of text in the canvas
canvas.grid(column=0, row=0, columnspan=2)


# BUTTON "Green Right"
rightButton = PhotoImage(file="images/right.png")  # Visible depression
greenButton = Button(image=rightButton, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=isComprehended)
greenButton.grid(column=1, row=1)

# BUTTON "Red Wrong"
wrongButton = PhotoImage(file="images/wrong.png")
redButton = Button(image=wrongButton, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=nextCard)
redButton.grid(column=0, row=1)




# ---------------------------- CALLING THE FUNCTION TO DEPICT THE PROPER OUTPUTS ------------------------------- #
nextCard()

window.mainloop()
