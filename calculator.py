import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for the display
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons dynamically
for text, row, col in buttons:
    if text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=button_clear).grid(row=row, column=col, sticky='nsew')
    elif text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=button_equal).grid(row=row, column=col, sticky='nsew')
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky='nsew')

# Adjust rows and columns
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
