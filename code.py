from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("Tic-Tac-Toe Game")
root.geometry("500x500+0+0")
root.resizable(0, 0)
root.state("zoomed")

# This Function just show messagebox and show's Winner of Game #


def winner_name(t):
    msg.showinfo("-----End of The Game-----",
                 f"'{t}' wins \nWinner of This Game is '{t}'")


# This Function disble all buttons when we gets winner and unbind all applied events #
def disable_all():
    for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        i.config(state=DISABLED)
        i.unbind("<Button-1>")

# This Function Restart the Game


def restart():
    global clicked, count
    clicked = True
    count = 0
    for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        i.config(text="", bg="red", fg="#fff", state=NORMAL)
        i.bind("<Button-1>", check_clicked)

# This Function show Developer of this Game #


def about_developer():
    msg.showinfo("About Developer!!",
                 "This Game is Developed By Mr.Aniket Gade")

# This Function check's who is winner #


def checkwinner():
    global winner
    winner = False
    # Checking If X wins or not
    if b1["text"] == b2["text"] == b3["text"] == "X":
        for i in b1, b2, b3:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b4["text"] == b5["text"] == b6["text"] == "X":
        for i in b4, b5, b6:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b7["text"] == b8["text"] == b9["text"] == "X":
        for i in b7, b8, b9:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b1["text"] == b4["text"] == b7["text"] == "X":
        for i in b1, b4, b7:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b2["text"] == b5["text"] == b8["text"] == "X":
        for i in b2, b5, b8:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b3["text"] == b6["text"] == b9["text"] == "X":
        for i in b3, b6, b9:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b1["text"] == b5["text"] == b9["text"] == "X":
        for i in b1, b5, b9:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    elif b3["text"] == b5["text"] == b7["text"] == "X":
        for i in b3, b5, b7:
            i.config(bg="blue")
        winner = True
        winner_name("X")
        disable_all()
    # Check If 'O' Wins or not
    elif b1["text"] == b2["text"] == b3["text"] == "O":
        for i in b1, b2, b3:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b4["text"] == b5["text"] == b6["text"] == "O":
        for i in b4, b5, b6:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b7["text"] == b8["text"] == b9["text"] == "O":
        for i in b7, b8, b9:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b1["text"] == b4["text"] == b7["text"] == "O":
        for i in b1, b4, b7:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b2["text"] == b5["text"] == b8["text"] == "O":
        for i in b2, b5, b8:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b3["text"] == b6["text"] == b9["text"] == "O":
        for i in b3, b6, b9:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b1["text"] == b5["text"] == b9["text"] == "O":
        for i in b1, b5, b9:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()
    elif b3["text"] == b5["text"] == b7["text"] == "O":
        for i in b3, b5, b7:
            i.config(bg="blue")
        winner = True
        winner_name("O")
        disable_all()

    # This code If match is Tied
    if winner == False and count == 9:
        msg.showinfo("Match Tied!", "Hey This match is Tied!")
        disable_all()

# checkwinner() function Ends #


# =============== Function for Inputing Entries from User STARTS ============= #
clicked = True
count = 0


def check_clicked(event):
    global clicked, count
    button_text = event.widget.cget("text")
    if button_text == "" and clicked == True:
        event.widget["text"] = "X"
        clicked = False
        count += 1
        checkwinner()
    elif button_text == "" and clicked == False:
        event.widget["text"] = "O"
        clicked = True
        count += 1
        checkwinner()
    else:
        msg.showerror("Box Alerady Selected!", "Click to another Empty box!")

# =============== Function for Inputing Entries from User ENDS ============= #


game_window = Frame(root)
game_window.pack(fill=X, expand=1, padx=400)

b1 = Button(game_window)
b1.grid(row=0, column=0)
b2 = Button(game_window)
b2.grid(row=0, column=1)
b3 = Button(game_window)
b3.grid(row=0, column=2)

b4 = Button(game_window)
b4.grid(row=1, column=0)
b5 = Button(game_window)
b5.grid(row=1, column=1)
b6 = Button(game_window)
b6.grid(row=1, column=2)

b7 = Button(game_window)
b7.grid(row=2, column=0)
b8 = Button(game_window)
b8.grid(row=2, column=1)
b9 = Button(game_window)
b9.grid(row=2, column=2)

for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
    i.config(width=9, height=4, bd=2, relief=SOLID, background="Red",
             cursor="hand2", font=('Vernda', 25, 'bold'), fg="#fff", bg="red")
    i.bind("<Button-1>", check_clicked)


# Creating Menu for Restarting Game #
Menubar = Menu(root)
restart_menu = Menu(Menubar, tearoff=False, fg="#fff",
                    bg="blue", font=('helevetica', 15, 'bold'))
restart_menu.add_command(label="Restart Game", command=restart)
restart_menu.add_command(label="About The Developer", command=about_developer)
Menubar.add_cascade(label="Menu-Options", menu=restart_menu)


root.config(background="cyan", menu=Menubar)
root.mainloop()
