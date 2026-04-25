import tkinter as tk
from tkinter import messagebox
import datetime
import matplotlib.pyplot as plt


sessions = []  


def save_session():
    subject  = subject_entry.get().strip()
    duration = duration_entry.get().strip()

    if subject == "" or duration == "":
        messagebox.showwarning("Warning", "Fill all boxes")
        return


    if not duration.isdigit():
        messagebox.showwarning("Warning", "Give Time in Numbers!")
        return


    date = datetime.date.today()    
    mins = int(duration)            


    sessions.append((date, subject, mins))   
    file = open("study_log.txt", "a", encoding="utf-8")
    file.write(f"{date} | {subject} | {mins}\n")
    file.close()


    messagebox.showinfo("Saved!", f"{subject} — {mins} Minutes have saved!")
    subject_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)


def show_graph():
    if len(sessions) == 0:
        messagebox.showinfo("Empty", "First save something!")
        return

    data = {}
    for date, subject, mins in sessions:   
        if subject in data:
            data[subject] += mins
        else:
            data[subject] = mins

    plt.bar(list(data.keys()), list(data.values()), color="skyblue")
    plt.xlabel("Subject")
    plt.ylabel("Minutes")
    plt.title("Study Progress")
    plt.tight_layout()
    plt.show()


def show_stats():
    if len(sessions) == 0:
        messagebox.showinfo("Empty", "There is bo data!")
        return

    total = 0
    for date, subject, mins in sessions:   
        total += mins

    hours = total // 60    
    left  = total % 60      
    messagebox.showinfo("Stats",
        f"Total Session : {len(sessions)}\n"
        f"Total Time  : {hours} Hour {left} Minute"
    )


def view_log():
    if len(sessions) == 0:
        messagebox.showinfo("Empty", "There is no reac!")
        return

    text = ""
    for date, subject, mins in sessions:    
        text += f"{date}  |  {subject}  |  {mins} min\n"

    messagebox.showinfo("Study Log", text)


root = tk.Tk()
root.title("StudyMate")
root.geometry("320x420")
root.config(bg="#1e1e2e")


tk.Label(root, text="StudyMate", font=("Courier New", 18, "bold"),
         bg="#1e1e2e", fg="#7c6af7").pack(pady=16)


tk.Label(root, text="Subject:", bg="#1e1e2e", fg="white",
         font=("Courier New", 10)).pack()
subject_entry = tk.Entry(root, font=("Courier New", 12), bg="#2a2a3e",
                         fg="white", insertbackground="white", relief="flat", bd=6)
subject_entry.pack(pady=4)


tk.Label(root, text="Minutes:", bg="#1e1e2e", fg="white",
         font=("Courier New", 10)).pack()
duration_entry = tk.Entry(root, font=("Courier New", 12), bg="#2a2a3e",
                          fg="white", insertbackground="white", relief="flat", bd=6)
duration_entry.pack(pady=4)


buttons = [
    ("Save Session", save_session, "#7c6af7"),
    ("Show Graph",   show_graph,   "#e67e22"),
    ("Statistics",   show_stats,   "#27ae60"),
    ("View Log",     view_log,     "#3498db"),
]


for label, command, color in buttons:
    tk.Button(root, text=label, command=command, bg=color, fg="white",
              font=("Courier New", 10, "bold"), relief="flat",
              pady=7, width=22).pack(pady=4)


root.mainloop()