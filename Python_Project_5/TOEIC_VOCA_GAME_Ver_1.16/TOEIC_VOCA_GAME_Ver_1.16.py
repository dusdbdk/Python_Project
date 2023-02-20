from tkinter import *
from tkinter import ttk
import random
from datetime import datetime

BGCOLOR = "#8142DB"
CORRECT_COLOR = "#47C83E"
WRONG_COLOR = "#FF5A5A"
BTN_COLOR = "#F0F0F0"

import csv
with open("TOEIC_VOCA.csv", "r", encoding="UTF-8") as file:
    questions = list(csv.reader(file))

win = Tk()

win.title("TOEIC_VOCA_GAME Ver 1.16")
win.geometry("430x300" + "+500+200")
win.config(bg=BGCOLOR)
win.resizable(False, False)

correct = 0
num_t = 0
count = 0

def score():
    question_label.destroy()
    for i in range(4):
        button[i].destroy()
    lab3.destroy()
    my_score = correct/num_t * 100
    remind_label = Label(win, text='REMIND', font=("Arial", 30, "bold"), fg='white', bg = BGCOLOR)
    remind_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    remind_label.place(x = 190, y = 40)
    num_words = len(wrong_answers)
    wrong_list = Listbox(win, highlightthickness=1, highlightcolor = "white", highlightbackground = "white", bg = "white", fg = "black", font = ("Arial", 15, "bold"))
    wrong_list.grid(row=0, column=0, sticky='nsew')
    if num_words > 28:
        win.geometry("550x715" + "+500+200")
        wrong_list.place(x = 40, y = 130, width = 450, height = 465)
    elif num_words >= 1:
        win.geometry(f"550x{len(wrong_answers) * 25 + 250}+500+200")
        wrong_list.place(x = 40, y = 130, width = 450, height = str(len(wrong_answers) * 25))
    scrollbar = ttk.Scrollbar(win, orient="vertical", command=wrong_list.yview)
    if num_words > 28:
        scrollbar.place(x = 490, y = 130, height = 465)
    elif num_words >= 1:
        scrollbar.place(x = 490, y = 130, height = str(len(wrong_answers) * 25))
    wrong_list.configure(yscrollcommand=scrollbar.set)
    wrong_list.config(yscrollcommand=scrollbar.set)
    for question, meaning in wrong_answers:
        wrong_list.insert(END, ' ' + question + ' : ' + meaning)
    if my_score == 100:
        win.geometry("580x270")
        wrong_list.destroy()
        scrollbar.destroy()
        remind_label.destroy()
        score_label = Label(win, text="만점입니다! 축하합니다!", font=("Arial", 30, "bold"), bg = BGCOLOR, fg = 'white')
        score_label.place(x = 60, y = 90, width = 450, height = 60 )
        copyright_label = Label(win, text="Copyright 2023. lapore All rights reserved. " + str(datetime.now().year), font=("Arial", 7), bg=BGCOLOR, fg="white")
        copyright_label.place(relx=1.0, rely=1.0, anchor='se')
    if num_words > 28:
        if 100 > my_score >= 80:
            score_label = Label(win, text=f'{my_score:.0f}' "점입니다. 합격입니다.", font=("Arial", 18, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 75, y = 625, width = 390, height = 30)
        elif my_score < 80:
            score_label = Label(win, text=f'{my_score:.0f}' "점입니다. 다시 공부해보세요.", font=("Arial", 18, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 75, y = 625, width = 390, height = 30)
    elif num_words >= 1:
        if 100 > my_score >= 80:
            score_label = Label(win, text=f'{my_score:.0f}' "점입니다. 합격입니다.", font=("Arial", 18, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 75, y = str(len(wrong_answers) * 25 + 170), width = 390, height = 30)
        elif my_score < 80:
            score_label = Label(win, text=f'{my_score:.0f}' "점입니다. 다시 공부해보세요.", font=("Arial", 18, "bold"), bg = BGCOLOR, fg = 'white')
            score_label.place(x = 75, y = str(len(wrong_answers) * 25 + 170), width = 390, height = 30)
        

used_questions = []

def next_question():
    global answer
    global count
    global cur_question
    global choice
    count += 1
    for i in range(4):
        button[i].config(bg = BTN_COLOR)
    while True:
        choice = random.sample(questions, 4)
        answer = int(random.randint(0,3))
        cur_question = choice[answer][0]
        if cur_question not in used_questions:
            used_questions.append(cur_question)
            break
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
        button[idx].config(bg = CORRECT_COLOR)
        win.after(500, next_question)
        correct += 1
    else:
        button[answer].config(bg = CORRECT_COLOR)
        win.after(500, next_question)
        wrong_answers.append((cur_question, choice[answer][1]))
        button[idx].config(bg = WRONG_COLOR)

def btn_f():
    global num_t
    num_t = int(ent.get())
    lab.destroy()
    ent.destroy()
    lab2.destroy()
    start_btn.destroy()
    win.geometry("430x600" + "+500+200")
    next_question()

# 질문 개수 Label 
lab = Label(win)
lab.config(text = "몇 개의 단어를 테스트 할까요?", font = ("Arial", 15, "bold"), bg = BGCOLOR, fg = "white")
lab.grid(column = 0, row = 0, padx = 5, pady = 30)
copyright_label = Label(win, text="Copyright 2023. Lapore All rights reserved. ", font=("Arial", 7), bg=BGCOLOR, fg="white")
copyright_label.place(relx=1.0, rely=1.0, anchor='se')

# Entry
ent = Entry(win, font = ("Arial", 19, "bold"), justify = "center")
ent.grid(column = 0, row = 1)
ent.place(x=180,
        y=100,
        height=50,
        width=50)

# n개 Label
lab2 = Label(win)
lab2.config(text = "개",  font = ("Arial", 15, "bold"), bg = BGCOLOR, fg = "white")
lab2.grid(column = 0, row = 2)
lab2.place(x = 232,
        y = 112,
        height = 30,
        width = 30)

# 시작 Button
start_btn = Button(win)
start_btn.config(text = "START!", font = ("Arial", 20, "bold"))
start_btn.config(command = btn_f)
start_btn.grid(column = 0, row = 2, columnspan = 2, pady = 100)

# 질문 Label
question_label = Label(win, height = 2, font = ("Arial", 35, "bold"), bg = BGCOLOR, fg = "white")
question_label.grid(pady = 30)

# 선택 Button
button = []
for i in range(4):
    btn = Button(win, text = f"No.{i}", width = 35, height = 2, font = ("Arial", 15, "bold"), bg = BTN_COLOR, command = lambda idx = i: check(idx))
    btn.grid()
    button.append(btn)

# 하단 점수 Label
lab3 = Label(win)
lab3.place(x = 40,
        y = 500,
        height = 30,
        width = 350)

win.mainloop()