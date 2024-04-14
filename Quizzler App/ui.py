from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
CANVAS_BG = "#A8CD9F"
CANVAS_BG_TRUE = "#58A399"
CANVAS_BG_FALSE = "#FF204E"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Self turns into a property which can be accessed anywhere in the class.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg=CANVAS_BG, highlightthickness=0)  # Canvas it allows us to layer lots of things on top of it.

        # LABELS

        self.scoreLabel = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1, columnspan=2)

        """Whenever we add an image or we add something to the canvas, we always have to provide a position 
        as the first two arguments. That is the tuple that represents the X and Y position of the text."""
        self.quizzText = self.canvas.create_text(
            150,
            125,
            width=280, # It allows to provide sufficient space for question and make it fitted inside of canvas
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Adding pady here to adjust the layout for Y coord.

        # BUTTONS
        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, bg=CANVAS_BG,
                                 highlightbackground=CANVAS_BG, command=self.trueButton)
        self.trueButton.grid(row=2, column=0)

        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, bg=CANVAS_BG,
                                 highlightbackground=CANVAS_BG, command=self.falseButton)
        self.falseButton.grid(row=2, column=1)


        """
        this endless loop essentially that's called the main loop.
        And this is a bit like a never ending while loop. It's constantly checking to see 
        if it needs to update something in the graphical user interface, or if the user has interacted 
        with it in some sort of way.
        """
        self.get_next_question() # everything has to go before the main loop because all the code you write after this
        # line is not going to be executed until window gets destroyed.
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_BG)
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            questionText = self.quiz.next_question()
            self.canvas.itemconfig(self.quizzText, text=questionText)
        else:
            self.canvas.itemconfig(self.quizzText, text="You have attained the end of the quiz")
            self.trueButton().config(state="disabled") # This method allows to disable or deactivate buttons.
            self.falseButton().config(state="disabled") # It will prevent from being pressed or activated.
    def trueButton(self):
        isCorrect = self.quiz.check_answer("True")
        self.provideFeedback(isCorrect)

    def falseButton(self):
        isCorrect= self.quiz.check_answer("False")
        self.provideFeedback(isCorrect)

    def provideFeedback(self, isCorrect):
        if isCorrect:
            self.canvas.config(bg=CANVAS_BG_TRUE)
        else:
            self.canvas.config(bg=CANVAS_BG_FALSE)

        self.window.after(1000, self.get_next_question)   # This method is used to calculate the time intervals for the functions in the application parallel

