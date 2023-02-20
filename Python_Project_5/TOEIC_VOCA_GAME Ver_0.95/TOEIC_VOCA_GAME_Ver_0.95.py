from tkinter import *
import random
from datetime import datetime

BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import csv
with open("TOEIC_VOCA.csv", "r", encoding="UTF-8") as file:
    questions = list(csv.reader(file))

win = Tk()

win.title("TOEIC_VOCA_GAME_Ver_0.95")
win.geometry("430x300")
win.config(bg=BGCOLOR)
win.resizable(False, False)

correct = 0
num_t = 0
count = 0

def score():
    win.geometry("550x700")
    question_label.destroy()
    for i in range(4):
        button[i].destroy()
    lab3.destroy()
    my_score = correct/num_t * 100
    remind_label = Label(win, text='REMIND', font=("Arial", 30, "bold"), fg='white', bg = BGCOLOR)
    remind_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    remind_label.place(x = 190, y = 40)
    num_words = len(wrong_answers)
    wrong_list = Listbox(win, highlightthickness=3, highlightcolor = "white", highlightbackground = "white", bg = "#3E497A", fg = "white", font = ("Arial", 15, "bold"))
    wrong_list.place(x = 80, y = 120, width = 390, height = num_words * 31)
    for question, meaning in wrong_answers:
        wrong_list.insert(END, ' ' + question + ' : ' + meaning)
        if my_score >= 80:
            score_label = Label(win, text=f'{my_score:.0f}' "���Դϴ�. �հ��Դϴ�.", font=("Arial", 15, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 80, y = 130+num_words*30+30, width = 390, height = 30)
        elif my_score < 80:
            score_label = Label(win, text=f'{my_score:.0f}' "���Դϴ�. �ٽ� ���� ������.", font=("Arial", 15, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 80, y = 130+num_words*30+30, width = 390, height = 30)
        
def next_question():
    global answer
    global count
    global cur_question
    global choice
    win.geometry("430x600" + "+500+200")
    count += 1
    for i in range(4):
        button[i].config(bg = BTN_COLOR)
    choice = random.sample(questions, 4)
    answer = int(random.randint(0,3))
    cur_question = choice[answer][0]
    question_label.config(text=cur_question)
    lab3.config(text = "Question. "f"{count} / " f"{num_t}", justify = "center", font = ("Arial", 15, "bold"), bg = BGCOLOR, fg = "white")
    for i in range(4):
        button[i].config(text=choice[i][1])
    if count > num_t:
        score()

wrong_answers = []

def check(idx):
    global correct
    idx = int(idx)
    if answer == idx:
        correct += 1
        button[idx].config(bg = CORRECT_COLOR)
        win.after(500, next_question)
    else:
        wrong_answers.append((cur_question, choice[answer][1]))
        button[idx].config(bg = WRONG_COLOR)
        button[answer].config(bg = CORRECT_COLOR)
        win.after(500, next_question)

def btn_f():
    global num_t
    num_t = int(ent.get())
    lab.destroy()
    ent.destroy()
    lab2.destroy()
    start_btn.destroy()
    next_question()

# ���� ���� Label 
lab = Label(win)
lab.config(text = "��� �ܾ �׽�Ʈ �ұ��?", font = ("Arial", 15, "bold"), bg = BGCOLOR, fg = "white")
lab.grid(column = 0, row = 0, padx = 5, pady = 30)

# Entry
ent = Entry(win, font = ("Arial", 19, "bold"), justify = "center")
ent.grid(column = 0, row = 1)
ent.place(x=180,
        y=100,
        height=50,
        width=50)

# n�� Label
lab2 = Label(win)
lab2.config(text = "��",  font = ("Arial", 15, "bold"), bg = BGCOLOR, fg = "white")
lab2.grid(column = 0, row = 2)
lab2.place(x = 232,
        y = 112,
        height = 30,
        width = 30)

# ���� Button
start_btn = Button(win)
start_btn.config(text = "START!", font = ("Arial", 20, "bold"))
start_btn.config(command = btn_f)
start_btn.grid(column = 0, row = 2, columnspan = 2, pady = 100)

# ���� Label
question_label = Label(win, height = 2, font = ("Arial", 35, "bold"), bg = BGCOLOR, fg = "white")
question_label.grid(pady = 30)

# ���� Button
button = []
for i in range(4):
    btn = Button(win, text = f"No.{i}", width = 35, height = 2, font = ("Arial", 15, "bold"), bg = BTN_COLOR, command = lambda idx = i: check(idx))
    btn.grid()
    button.append(btn)

# �ϴ� ���� Label
lab3 = Label(win)
lab3.place(x = 40,
        y = 500,
        height = 30,
        width = 350)


win.mainloop()