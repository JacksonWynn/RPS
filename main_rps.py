from RPS import *


def main():
    userScore: int = 0
    compScore: int = 0
    handsThrown: int = 0
    
    window = Tk()
    window.title("Rock, Paper, Scissors")
    window.geometry("250x180")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
