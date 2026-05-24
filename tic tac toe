import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe - vs AI or Friend")
root.geometry("450x750")

# --- MASTER VARIABLES ---
player = "X"
game_over = False
buttons = [] 
score_x = 0
score_o = 0
# New: Variable to track the game mode (True = vs AI, False = 2 Player)
vs_ai = tk.BooleanVar(value=True) 

# --- MODE SELECTOR ---
mode_frame = tk.Frame(root)
mode_frame.pack(pady=5)
tk.Label(mode_frame, text="Mode:", font=('Arial', 12)).pack(side=tk.LEFT)
tk.Radiobutton(mode_frame, text="vs AI", variable=vs_ai, value=True, font=('Arial', 12)).pack(side=tk.LEFT)
tk.Radiobutton(mode_frame, text="2 Players", variable=vs_ai, value=False, font=('Arial', 12)).pack(side=tk.LEFT)

lbl_turn = tk.Label(root, text="Player X's Turn", font=('Arial', 14), fg="red")
lbl_turn.pack(pady=5)

lbl_score = tk.Label(root, text="Score: X = 0 | O = 0", font=('Arial', 16, 'bold'))
lbl_score.pack(pady=10)

def update_score_display():
    lbl_score.config(text=f"Score: X = {score_x} | O = {score_o}")

def reset_game():
    global player, game_over
    player = "X"
    game_over = False
    lbl_turn.config(text="Player X's Turn", fg="red")
    for b in buttons:
        b.config(text="", bg="lightgray", state="normal")

def ai_move():
    global game_over
    if game_over: return

    # 1. CHECK IF AI CAN WIN
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        marks = [buttons[i]["text"] for i in combo]
        if marks.count("O") == 2 and marks.count("") == 1:
            move = combo[marks.index("")]
            click_button(buttons[move])
            return

    # 2. CHECK IF AI NEEDS TO BLOCK PLAYER
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        marks = [buttons[i]["text"] for i in combo]
        if marks.count("X") == 2 and marks.count("") == 1:
            move = combo[marks.index("")]
            click_button(buttons[move])
            return

    # 3. TAKE CENTER IF OPEN
    if buttons[4]["text"] == "":
        click_button(buttons[4])
        return

    # 4. OTHERWISE, PICK RANDOM
    empty_buttons = [b for b in buttons if b["text"] == ""]
    if empty_buttons:
        click_button(random.choice(empty_buttons))





def check_winner():
    global game_over, score_x, score_o
    # Full win list: Rows, Columns, and Diagonals
    win_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    
    for combo in win_list:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            game_over = True
            winner = buttons[combo[0]]["text"] 
            
            if winner == "X": score_x += 1
            else: score_o += 1
            
            update_score_display() 
            for index in combo:
                buttons[index].config(bg="lightgreen")
                
            if messagebox.askyesno("Game Over", f"Player {winner} Wins! Play again?"):
                reset_game()
            else:
                root.destroy()
            return True

    if all(b["text"] != "" for b in buttons):
        game_over = True
        if messagebox.askyesno("Tic Tac Toe", "It's a tie! Play again?"):
            reset_game()
        else:
            root.destroy()
        return True
    return False

def click_button(b):
    global player, game_over
    if b["text"] == "" and not game_over:
        b["text"] = player
        b.config(fg="red" if player == "X" else "blue")
        
        if not check_winner():
            if player == "X":
                player = "O"
                # Update text based on mode
                status = " (AI)" if vs_ai.get() else ""
                lbl_turn.config(text=f"Player O's Turn{status}", fg="blue")
                
                # Only trigger AI if mode is set to vs AI
                if vs_ai.get():
                    root.after(500, ai_move)
            else:
                player = "X"
                lbl_turn.config(text="Player X's Turn", fg="red")

# --- BOARD LAYOUT ---
frm = tk.Frame(root, bg="#fa6305", padx=10, pady=10)
frm.pack(pady=20)

for i in range(9):
    btn = tk.Button(frm, text="", width=5, height=2, font=('Arial', 20, 'bold'), bg="lightgray")
    btn.config(command=lambda b=btn: click_button(b))
    btn.grid(row=i//3, column=i%3, padx=4, pady=4)
    buttons.append(btn)

btn_restart = tk.Button(root, text="RESTART BOARD", font=('Arial', 12, 'bold'), command=reset_game)
btn_restart.pack(pady=20)

root.mainloop()

