

# Tic Tac Toe on Tkinter


import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

# Create a 3x3 grid of buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 20), width=3, height=1)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

player = "X"  # Start with player X
def button_click(row, col):
    global player
    if buttons[row][col]["text"] == " " and check_winner() is False:
        buttons[row][col]["text"] = player
        if player == "X":
            player = "O"
        else:
            player = "X"

def check_winner():
    # Check rows
    for row in buttons:
            return True
    # Check columns
    for col in range(3):
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return True
    return False

# Bind the button click event to the button_click function
for i in range(3):
    for j in range(3):
        buttons[i][j]["command"] = lambda row=i, col=j: button_click(row, col)

root.mainloop()
