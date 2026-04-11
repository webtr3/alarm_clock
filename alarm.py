import time
import winsound
from tkinter import *

root = Tk()
root.title("Alarm Clock")
root.geometry("300x420")
root.resizable(False, False)
root.configure(bg="#b3e5fc")

alarm_var = StringVar()
status_var = StringVar()

Label(root, text="Alarm Clock", font=("Segoe UI", 16, "bold"), bg="#b3e5fc").pack(pady=15)

entry = Entry(root, textvariable=alarm_var, justify="right",
            font=("Segoe UI", 16), bd=2, relief="groove")
entry.pack(ipady=5, padx=20, fill="x")

status = Label(root, textvariable=status_var,
            font=("Segoe UI", 10), bg="#b3e5fc")
status.pack(pady=5)

def append_text(value):
    alarm_var.set(alarm_var.get() + value)

def clear():
    alarm_var.set("")

def check_alarm():
    while True:
        current = time.strftime("%I:%M %p")
        if current == alarm_var.get():
            winsound.Beep(1000, 1000)
            status_var.set("Alarm ringing!")
            break
        time.sleep(1)

def set_alarm():
    alarm_time = alarm_var.get()
    if alarm_time:
        status_var.set(f"Alarm set for {alarm_time}")
        root.after(1000, check_alarm)

frame = Frame(root, bg="#b3e5fc")
frame.pack(pady=10)

buttons = [
    ('1','2','3','AM'),
    ('4','5','6','PM'),
    ('7','8','9',':'),
    ('C','0','','')
]

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        if val:
            action = clear if val == 'C' else lambda v=val: append_text(v)
            Button(frame, text=val, width=5, height=2,
                font=("Segoe UI", 10),
                command=action).grid(row=r, column=c, padx=5, pady=5)

Button(root, text="Set Alarm", font=("Segoe UI", 11, "bold"),
    width=15, command=set_alarm).pack(pady=10)

root.mainloop()