from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF8080"
RED = "#6D2932"
GREEN = "#436850"
YELLOW = "#FFDEAD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# This function is responsible for resetting the timer.
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
# This function is responsible for calling the countDown function to start clocking.
def startTimer():
    global reps
    reps += 1

    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # The case if it is the 8th rep
        countDown(longBreakSec)
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0: # The case if it is the 2nd/4th/6th rep
        countDown(shortBreakSec)
        timerLabel.config(text="Break", fg=PINK)
    else:
        countDown(workSec) # The case if it is the 1st/3rd/5th/7th rep
        timerLabel.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# To be able to create interactive programs, it is essential to provide a timing mechanism
# window.after(1000, saySmt, "Hello", "Yo", "Vodka")  # This method executes a command after a time delay. It takes an amount of time that it should wait.
                      # We first provide the amount of time to wait in milliseconds. Next we pass a function to call,
                      # The final thing might be a list of argumets (unlimited number of positional arguments). These arguments
                      # are going to be passed to the function.
def countDown(count):
    # It is necessary to remain seconds for depicting on a screen
    countMin = math.floor(count / 60)  # Floor() method will return the largest whole number after division
    countSec = count % 60  # This operation allows to depict zero after finding a module

    if countSec < 10:  # It enables to enhance a visualization with displaying time format, It is called a Dynamic typing
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")  # The method itemconfig() allows to configure and assign a new text
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1) # I have encapsulated into the variable because I need it to cancel timer
                                                        # for the Reset button
    else:
        startTimer() # When the count goes to zero, it is a moment where it is necessary to call start time again

        mark = ""
        workSessions = math.floor(reps/2) # To calculate the total number of sessions in order to display the check mark ot not
        for tick in range(workSessions):
            mark += "✔︎"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Mia")
window.config(padx=100, pady=50, bg=YELLOW)  # bg - background

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # Creating a canvas widget. "highlightthickness"
                                                                    # method removes any boarder lines, some kind of frames
tomato_img = PhotoImage(file="tomato.png") # This class comes from tkinter and it's basically a way to read through a file
                              # and to get hold of a particular image at a particular file location.

canvas.create_image(100, 112, image=tomato_img)  # X value: 103, Y value: 112
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # This method is able to accept *args and **kw to display some information
canvas.grid(column=1, row=1)
#countDown(5)

# LABEL "TIMER"
timerLabel = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timerLabel.grid(column=1, row=0)

# Button "Start"
start_button = Button(text="Start", bg=YELLOW, fg="#000000", highlightthickness=0,
                  highlightbackground=YELLOW, highlightcolor=YELLOW, command=startTimer)
start_button.grid(column=0, row=2)

# Button "Reset"
reset_button = Button(text="Reset", bg=YELLOW, fg="#000000", highlightthickness=0,
                highlightbackground=YELLOW, highlightcolor=YELLOW, command=resetTimer)
reset_button.grid(column=2, row=2)

# Check Mark
check_mark = Label(text="", bg=YELLOW, fg=GREEN, highlightthickness=0,
                highlightbackground=YELLOW, highlightcolor=YELLOW)
check_mark.grid(column=1, row=3)



window.mainloop()
