from tkinter import *
from tkinter import messagebox  # This is another module of code, not a class
import random
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #

LIGHT_GREEN_SHADOW = '#FBFADA'    # Background
LIGHT_GREEN = '#ADBC9F'
GREEN = '#436850'
DARK_GREEN = '#12372A'  # Font
FONT_NAME = "Garret"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generationPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    randomChoiceLetter = [random.choice(letters) for i in range(0, 9)]
    #print(randomChoiceLetter)
    randomChoiceSymbol = [random.choice(symbols) for i in range(2, 4)]
    #print(randomChoiceSymbol)
    randomChoiceNumber = [random.choice(numbers) for i in range(2, 4)]
    #print(randomChoiceNumber)
    result = randomChoiceLetter + randomChoiceSymbol + randomChoiceNumber
    random.shuffle(result)
    password = "".join(result)
    #print(f'Your password is: {"".join(result)}')
    passwordInput.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = websiteInput.get() # get() allows to fetch the current entry text
    email = emailUsernameInput.get()
    password = passwordInput.get()
    newData = {
        website: {
            "email": email,
            "password": password
        }
    }
    # messagebox module allows to create a pop-up window with a title and essential message
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(message='Please fill out the essential fields')
    else:
        try:
            with open("passwordData.json", "r") as dataFile:

                passwordData = json.load(dataFile)  # json.load() allows to read the data

        except FileNotFoundError:
            with open("passwordData.json", "w") as dataFile:
                json.dump(newData, dataFile, indent=4)

        else:
            passwordData.update(newData)  # Updating old data with new data. The update() method inserts the specified items to the dictionary.
            messagebox.showinfo(title=website, message=f"The data has been saved for {website} website")

            with open("passwordData.json", "w") as dataFile:
                json.dump(passwordData, dataFile, indent=4)  # Saving updated data

        finally:
            websiteInput.delete(0, END)
            #emailUsernameInput.delete(0, END)
            passwordInput.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def findPassword():
    website = websiteInput.get()
    try:
        with open("passwordData.json") as dataFile:
            passwordData = json.load(dataFile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="The file has not been found")
    else:
        if website in passwordData:
            email = passwordData[website]["email"]
            password = passwordData[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"The data has not been saved for {website} website")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=LIGHT_GREEN_SHADOW)  # bg - background

# The layout is going to be 3-columns and 5-rows
canvas = Canvas(width=250, height=250, bg=LIGHT_GREEN_SHADOW, highlightthickness=0)   # Creating a canvas widget. "highlightthickness"
                                                                    # method removes any boarder lines, some kind of frames
password_img = PhotoImage(file="Green Lock.png")

canvas.create_image(90, 125, image=password_img)  # X value: 103, Y value: 112
canvas.grid(column=1, row=0,columnspan=2) # Enabling some sort of layout dimension.

# LABEL "Website"
websiteLabel = Label(text="Website:", font=(FONT_NAME, 15), fg=DARK_GREEN, bg=LIGHT_GREEN_SHADOW)
websiteLabel.grid(column=0, row=1)

# LABEL "Email/Username"
emailUsernameLabel = Label(text="Email/Username:", font=(FONT_NAME, 15), fg=DARK_GREEN, bg=LIGHT_GREEN_SHADOW)
emailUsernameLabel.grid(column=0, row=2)

# LABEL "Password"
passwordLabel = Label(text="Password:", font=(FONT_NAME, 15), fg=DARK_GREEN, bg=LIGHT_GREEN_SHADOW)
passwordLabel.grid(column=0, row=3)

# ENTRY "Website"
websiteInput = Entry(width=18, bg=LIGHT_GREEN_SHADOW, highlightthickness=0.5, fg=DARK_GREEN)
websiteInput.grid(column=1, row=1) #, columnspan=2) # columnspan() method that allows to specify how many columns in a
                                      # particular widget (for instance label) will be spanned
websiteInput.focus() # This will place a cursor into that particular entry

# ENTRY "Email/Username"
emailUsernameInput = Entry(width=37, bg=LIGHT_GREEN_SHADOW, highlightthickness=0.5, fg=DARK_GREEN)
emailUsernameInput.grid(column=1, row=2, columnspan=2)
emailUsernameInput.insert(0, "mkhomutinnikov@gmail.com") # This method allows to ingest data at on a certain position.
                                                     # 0 - index where a text is going to be hold
# ENTRY "Password"
passwordInput = Entry(width=18, bg=LIGHT_GREEN_SHADOW, highlightthickness=0.5, fg=DARK_GREEN)
passwordInput.grid(column=1, row=3) #, columnspan=2)


# BUTTON "Search"
searchButton = Button(width=14, text="Search", bg=LIGHT_GREEN_SHADOW, fg=DARK_GREEN, highlightthickness=1,
                                highlightbackground=LIGHT_GREEN_SHADOW, command=findPassword)
searchButton.grid(column=2, row=1) #, columnspan=2)

# BUTTON "Generate Password"
generatePasswordButton = Button(width=14, text="Generate Password", bg=LIGHT_GREEN_SHADOW, fg=DARK_GREEN, highlightthickness=0,
                                highlightbackground=LIGHT_GREEN_SHADOW, command=generationPass)
generatePasswordButton.grid(column=2, row=3) #, columnspan=2)

# BUTTON "Save Password"
savePasswordButton = Button(width=35, text="Save Password", bg=LIGHT_GREEN_SHADOW, fg=DARK_GREEN, highlightthickness=0,
                            highlightbackground=LIGHT_GREEN_SHADOW, command=save)
savePasswordButton.grid(column=1, row=4, columnspan=2)

# highlightbackground=DARK_BLUE, highlightcolor=DARK_BLUE)


window.mainloop()
