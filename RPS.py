from tkinter import *
import random
import csv

class GUI:
    
    def __init__(self, window) -> None:
        '''
        Initializer method creates the elements of the GUI window and declares RPS variables.
        '''
        self.window = window
        self.userScore: int = 0
        self.compScore: int = 0
        self.handsThrown: int = 0
        self.frame_choice = Frame(self.window)
        self.label_choice = Label(self.frame_choice, text='Choice')
        self.entry_choice = Entry(self.frame_choice)
        self.label_choice.pack(padx=5, side='left')
        self.entry_choice.pack(padx=5, side='left')
        self.frame_choice.pack(pady=10)
        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text='')
        self.label_message.pack(padx=5, side='left')
        self.frame_message.pack(pady=10)
        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='Submit', command=self.clicked)
        self.button_submit.pack()
        self.frame_submit.pack(pady=10)
    
    
    def playGame(self, userChoice, compChoice) -> None:
        '''
        RPS simulator method determines the winner of a game of RPS (or a tie) given the user choice and computer
        choice, and keeps track of how many games have been played.
        '''
        if userChoice == 1:
            if compChoice == 2:
                self.compScore += 1
            if compChoice == 3:
                self.userScore += 1
                    
        if userChoice == 2:
            if compChoice == 1:
                self.userScore += 1
            if compChoice == 3:
                self.compScore += 1
            
        if userChoice == 3:
            if compChoice == 1:
                self.compScore += 1
            if compChoice == 2:
                self.userScore += 1
        
        self.handsThrown += 1
        
        
    def checkChoice(self, userChoice) -> int:
        '''
        This method converts a string user input into an int that the rest of the code can use.
        '''
        if userChoice.strip().lower() == "rock":
            return 1
        if userChoice.strip().lower() == "paper":
            return 2
        if userChoice.strip().lower() == "scissors":
            return 3
        return -1


    def clicked(self) -> None:
        '''
        Submit button click method runs a game of RPS and updates the message board
        according to the results.
        '''
        userChoice = self.entry_choice.get()
        compChoice = random.randint(1, 3)
        
        if self.checkChoice(userChoice) == -1:
            self.label_message.config(text="Choice must be Rock, Paper, or Scissors.")
        else:
            self.playGame(self.checkChoice(userChoice), compChoice)
            self.label_message.config(text="Hands Thrown: {}\nUser Score: {}\nComputer Score: {}".format(self.handsThrown, self.userScore, self.compScore))
