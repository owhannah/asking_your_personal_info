# redo program #2
# add more info to ask and display. (Any info)

import tkinter as tk
import tkinter.messagebox as messagebox

def print(name, age, dream_job, skills):
    print = f"*** Welcome {name} ***\n\n"
    print += f"You are {age} years old with skills in {skills}.\n"
    print += f"Congratulations! Your dream job as a {dream_job} awaits you.\n"
    print += "Make every moment count on your journey!\n"
    print += "*" * 30  # Adding some decorative stars for aesthetics

    return print

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Formatted text has been copied to clipboard.")

def submit():
    name = entry_name.get()
    age = entry_age.get()
    dream_job = entry_dream_job.get()
    skills = entry_skills.get()
    fancy_text = print(name, age, dream_job, skills)
    copy_to_clipboard(fancy_text)

root = tk.Tk()
root.title("Personal Info")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_name = tk.Label(frame, text="Enter your name:")
label_name.grid(row=0, column=0, sticky="e")

entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_age = tk.Label(frame, text="Enter your age:")
label_age.grid(row=1, column=0, sticky="e")

entry_age = tk.Entry(frame)
entry_age.grid(row=1, column=1)

label_dream_job = tk.Label(frame, text="Enter your dream job:")
label_dream_job.grid(row=2, column=0, sticky="e")

entry_dream_job = tk.Entry(frame)
entry_dream_job.grid(row=2, column=1)

label_skills = tk.Label(frame, text="Enter your skills:")
label_skills.grid(row=3, column=0, sticky="e")

entry_skills = tk.Entry(frame)
entry_skills.grid(row=3, column=1)

submit_button = tk.Button(frame, text="DONE!", command=submit)
submit_button.grid(row=4, columnspan=2, pady=10)

root.mainloop()



