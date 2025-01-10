from tkinter import *
import math

"""
# Project 19: Pomodoro

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 30 Dec 2024
- **Last Modified**: 10 Jan 2025

## Description:
The Pomodoro Timer is a productivity app that uses the **Tkinter** and **math** modules to create a user-friendly and visually appealing interface. The app features:
- A tomato image displaying the countdown timer.
- Interactive colors indicating work or break sessions.
- Labels showing the current status (Work, Short Break, Long Break).
- Two buttons: **Start** to begin the timer and **Reset** to reset it.

The Pomodoro method involves:
- **25 minutes of focused work**.
- **5 minutes of short break** after each session.
- A tick mark added to the UI for each completed cycle.
- **20 minutes of long break** after 4 completed cycles.

## How to Use:
1. Run `app.py`.
2. Click the **Start** button to begin the timer.
3. The UI will display the current status (Work/Break) and the countdown timer.
4. After completing a cycle, a tick mark will appear in the UI.
5. Click the **Reset** button to reset the timer to 00:00.

## Level
- **Level**: Intermediate
- **Skills**: GUI Development, Event-Driven Programming, Timer Logic
- **Domain**: Productivity Tools

## Features
- Dynamic GUI with status labels, timer, and tick marks.
- Easy-to-use Start and Reset buttons.
- Automatically switches between Work, Short Break, and Long Break sessions.
- Tracks completed cycles with visual ticks.

## Screenshots
The `screenshots` folder contains gameplay screenshots showcasing the application's features and interface.

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: Double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

**Created by Pranjal Sarnaik**  
*© 2024-2025. All rights reserved.*
"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TICK = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """This resets the timer."""
    global REPS, TICK
    REPS = 0
    TICK = ""
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    add_check_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #


def count_down(count):
    """This changes the timer text present on canvas."""
    # math.floor() rounds a number down to the nearest integer.
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:

        # Method 1 for adding checkmark after each two rounds
        global TICK
        if REPS % 2 == 0:
            TICK += "✔"
            add_check_label.config(text=TICK)
            # if len(TICK) % 3 == 0:
            #     TICK += "\n"
            #     add_check_label.config(text=TICK)
            # else:
            #     add_check_label.config(text=TICK)

        start_timer()

        # method 2
        # work_session = math.floor(REPS/2)
        # for _ in range(work_session):
        #     TICK += "✔"
        # add_check_label.config(text=TICK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer():
    """This checks what to do like is it work or break and based on this it will provide seconds to work to count_down function."""
    global REPS
    REPS += 1

    # REPS = 1357
    work_sec = WORK_MIN * 60
    # REPS = 8
    long_break_sec = LONG_BREAK_MIN * 60
    # REPS = 246
    short_break_sec = SHORT_BREAK_MIN * 60

    # Method 1 for conditions
    # if REPS % 2 != 0:
    #     count_down(work_sec)
    # elif REPS % 8 == 0:
    #     count_down(long_break_sec)
    # elif REPS % 2 == 0:
    #     count_down(short_break_sec)

    if REPS < 9:
        if REPS % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        elif REPS % 2 == 0:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            timer_label.config(text="Work", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro by Pranjal Sarnaik")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, "bold"))
timer_label.grid(column=1, row=0)

# Canvas lets us put many things on top of each other, like in this case image and text.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

add_check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
add_check_label.grid(column=1, row=4)

# window.mainloop() continuously checks for events (like window.after() callbacks or user interactions)
# and keeps the program running.
window.mainloop()
