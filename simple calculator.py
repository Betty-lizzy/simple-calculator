import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to show calculations
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create buttons dynamically
row = 1
col = 0
for label in buttons:
    btn = tk.Button(root, text=label, font=("Arial", 18), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    
    if label == "=":
        btn.config(command=calculate)
    else:
        btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18), width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the main loop
root.mainloop()
