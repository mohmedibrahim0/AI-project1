import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
current_player = "X"

buttons = []

def on_click(i):
    global current_player
    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        if check_win():
            tk.Label(window, text=f"🎉 Player {current_player} wins!", font=('Arial', 14)).grid(row=3, column=0, columnspan=3)
            disable_buttons()
        elif all(button["text"] != "" for button in buttons):
            tk.Label(window, text="🤝 It's a draw!", font=('Arial', 14)).grid(row=3, column=0, columnspan=3)
        else:
            current_player = "O" if current_player == "X" else "X"

def check_win():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "" for a, b, c in wins)

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

for i in range(9):
    btn = tk.Button(window, text="", width=6, height=3, font=('Arial', 20), command=lambda i=i: on_click(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

window.mainloop()