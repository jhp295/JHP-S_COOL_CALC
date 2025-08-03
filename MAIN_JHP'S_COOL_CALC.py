import tkinter as tk

def on_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("jhp's Cool Calc")
root.geometry("300x400")
root.resizable(False, False)

# Display Entry
display = tk.Entry(root, font=("Segoe UI", 24), borderwidth=2, relief="solid", justify='right')
display.pack(fill="both", padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create button grid
btn_frame = tk.Frame(root)
btn_frame.pack()

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, font=("Segoe UI", 18), command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, font=("Segoe UI", 18), command=lambda c=char: on_click(c))
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Clear button at bottom
clear_btn = tk.Button(root, text="Clear", font=("Segoe UI", 16), bg="#ff4d4d", fg="white", command=clear_display)
clear_btn.pack(fill="both", padx=10, pady=10)

root.mainloop()