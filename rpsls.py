from tkinter import *
import random
user = int
computer = int
win = 0
lose = 0


def rpsls(win, lose, user):
    computer = random.randrange(1, 4)
    if user == computer:
        var.set("Draw. \n No Points")
    elif user == 1 and computer == 3:
        var.set("You chose Rock, Sheldon chose Scissors. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 1 and computer == 2:
        var.set("You chose Rock, Sheldon chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 1:
        var.set("You chose Paper, Sheldon chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 3:
        var.set("You chose Paper, Sheldon chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, Sheldon chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, Sheldon chose Paper. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 4 and computer == 3:
        var.set("You chose Spock, Sheldon chose Scissors. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 4 and computer == 1:
        var.set("You chose Spock, Sheldon chose Rock. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 4 and computer == 5:
        var.set("You chose Spock, Sheldon chose Lizard. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 4 and computer == 2:
        var.set("You chose Spock, Sheldon chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 1:
        var.set("You chose Lizard, Sheldon chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 2:
        var.set("You chose Lizard, Sheldon chose Paper. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 5 and computer == 3:
        var.set("You chose Lizard, Sheldon chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, Sheldon chose Spock. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 1 and computer == 4:
        var.set("You chose Rock, Sheldon chose Spock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 4:
        var.set("You chose Paper, Sheldon chose Spock. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 3 and computer == 4:
        var.set("You chose Scissors, Sheldon chose Spock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, Sheldon chose Spock. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 1 and computer == 5:
        var.set("You chose Rock, Sheldon chose Lizard. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 2 and computer == 5:
        var.set("You chose Paper, Sheldon chose Lizard. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 5:
        var.set("You chose Scissors, Sheldon chose Lizard. \nYou win")
        wins.set(wins.get() + 1)

    elif user == 4 and computer == 5:
        var.set("You chose Spock, Sheldon chose Lizard. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)
    else:
        var.set("Thank You for playing. \nYou have " + str(win) +
                " wins and " + str(lose) + " losses.")


window = Tk()
window.title("RPSLS GAME")
window.config(padx=100, pady=100, bg="#553e67")
Button1 = Button(window, text="Rock", bg="white",
                 fg="black", font=("Poppins", 18, "bold"), command=lambda: rpsls(win, lose, 1))
Button1.grid(row=0, column=1)
Button2 = Button(window, text="Paper", bg="white",
                 fg="black", font=("Poppins", 18, "bold"), command=lambda: rpsls(win, lose, 2))
Button2.grid(row=0, column=2)
Button3 = Button(window, text="Scissors", bg="white",
                 fg="black", font=("Poppins", 18, "bold"), command=lambda: rpsls(win, lose, 3))
Button3.grid(row=0, column=3)
Button4 = Button(window, text="Lizard", bg="white",
                 fg="black", font=("Poppins", 18, "bold"), command=lambda: rpsls(win, lose, 4))
Button4.grid(row=0, column=4)
Button5 = Button(window, text="Spoke", bg="white",
                 fg="black", font=("Poppins", 18, "bold"), command=lambda: rpsls(win, lose, 5))
Button5.grid(row=0, column=5)
var = StringVar()
var.set("Welcome!")
l = Label(window, textvariable=var, pady=20, bg="#553e67",
          fg="white", font=("Poppins", 25, "bold"))
l.grid(row=2, column=2, columnspan=3)
wins = IntVar()
wins.set(win)
x = Label(window, textvariable=wins, pady=20, bg="#553e67",
          fg="white", font=("Poppins", 18, "bold"))
x.grid(row=4, column=2, columnspan=3, padx=50)
labeled = Label(window, text="Total Score", bg="#553e67",
                fg="white", font=("Poppins", 20, "bold"), pady=10)
labeled.grid(row=3, column=2, columnspan=3)
window.mainloop()
