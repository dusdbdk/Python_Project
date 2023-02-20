BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import csv
from tkinter import *
import random
with open("TOEIC_VOCA.csv", "r", encoding="UTF-8-sig") as file:
    questions = data = list(csv.reader(file))

def next_question():
    global answer
    for i in range(4):
        button[i].config(bg=BTN_COLOR)

    choice = random.sample(questions, 4)
    answer = random.randint(0,3)
    cur_question = choice[answer][0]
    question_label.config(text=cur_question)

    for i in range(4):
        button[i].config(text=choice[i][1])

answer = 0

def check(idx):
    idx = int(idx)
    if answer == idx:
        button[idx].config(bg=CORRECT_COLOR)
        window.after(500, next_question)
    else:
        button[idx].config(bg=WRONG_COLOR)
        window.after(500, next_question)


window = Tk()
window.title("TOEIC_VOCA_GAME_Ver_0.31")
window.config(padx=30, pady=10, bg=BGCOLOR)

question_label = Label(window, width=20, height=2, text="test",
                        font=("Arial", 25, "bold"), bg=BGCOLOR, fg="white")

question_label.pack(pady=40)

button = []
for i in range(4):
    btn = Button(window, text=f"No.{i}", width=35, height=2, font=("Arial", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check(idx))

    btn.pack()
    button.append(btn)

next_btn = Button(window, text="Next", width=15, height=2, command=next_question, font=("Arial", 15, "bold"), bg=CORRECT_COLOR)

next_btn.pack(pady=30)

next_question()

window.mainloop()