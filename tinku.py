import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create and pack the widgets
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(frame, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=10)

task_listbox = tk.Listbox(root, width=80, height=20)
task_listbox.pack(pady=10)

# Start the application
root.mainloop()
