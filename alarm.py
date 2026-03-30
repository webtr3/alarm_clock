import time
import winsound
from tkinter import Tk, StringVar, Label, Entry, Button

box = Tk()
box.title("Alarm Clock")
box.geometry("300x420")  
box.resizable(False, False)
box.configure(bg="lightblue")

box2 = StringVar(box)

Label(box, text="Alarm Clock", font=("Arial", 15), bg="lightblue").place(x=90, y=20)

entry = Entry(box, justify="right", textvariable=box2, width=24, font=("Arial", 14), bg="white")
entry.place(x=15, y=60)

def add_int(text, store: StringVar):
    store.set(store.get() + text)

def set_alarm():
    alarm_time = box2.get()
    Label(box, text=f"Alarm set for {alarm_time}", font=("Arial", 10), bg="lightblue").place(x=70, y=100)

buttons = [
    ('1', 40, 150), ('2', 110, 150), ('3', 180, 150),
    ('4', 40, 200), ('5', 110, 200), ('6', 180, 200),
    ('7', 40, 250), ('8', 110, 250), ('9', 180, 250),
    ('0', 110, 300), (':', 250, 150), ('AM', 250, 200), ('PM', 250, 250)
]

for (text, x, y) in buttons:
    Button(box, height=2, width=5, text=text, font=("Arial", 9), bg="white",
        command=lambda t=text: add_int(t, box2)).place(x=x, y=y)

Button(box, height=2, width=10, text="Set Alarm", font=("Arial", 9),
    bg="white", command=set_alarm).place(x=170, y=302)

box.mainloop()