import tkinter as tk

def calculate_sum():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 + num2)

root = tk.Tk()
root.title("Sum Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root, width=20)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root, width=20)
entry_num2.pack()

calculate_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
