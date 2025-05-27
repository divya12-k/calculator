import tkinter as tk

def on_click(op):
    global expression
    expression += str(op)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

# Creating main window
root = tk.Tk()
root.title("Simple Calculator")

expression = ""
equation = tk.StringVar()

entry_field = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify="right", bd=10)
entry_field.grid(columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "C":
        action = lambda: clear()
    elif button == "=":
        action = lambda: calculate()
    else:
        action = lambda b=button: on_click(b)
        
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 20),
              command=action).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()