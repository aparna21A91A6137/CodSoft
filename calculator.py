import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_operation(op):
    first_num = float(entry.get())
    global first_num_global
    first_num_global = first_num
    global operation
    operation = op
    entry.delete(0, tk.END)

def button_equal():
    second_num = float(entry.get())
    entry.delete(0, tk.END)
    if operation == "+":
        result = first_num_global + second_num
    elif operation == "-":
        result = first_num_global - second_num
    elif operation == "*":
        result = first_num_global * second_num
    elif operation == "/":
        if second_num != 0:
            result = first_num_global / second_num
        else:
            result = "Cannot divide by zero"
    entry.insert(0, result)
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=('Arial', 20), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]


for button_text, row, column in button_layout:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16))
    button.grid(row=row, column=column, padx=5, pady=5)
    if button_text.isnumeric() or button_text == ".":
        button.config(command=lambda txt=button_text: button_click(txt))
    elif button_text == "=":
        button.config(command=button_equal)
    elif button_text == "C":
        button.config(command=button_clear)
    else:
        button.config(command=lambda txt=button_text: button_operation(txt))

root.mainloop()

