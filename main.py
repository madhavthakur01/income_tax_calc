import tkinter as tk
from tkinter import messagebox

def calculate_tax(income):
    tax = 0
    rebate = 0
    
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

    if income <= 500000:
        rebate = min(tax, 12500)

    final_tax = tax - rebate
    if final_tax < 0:
        final_tax = 0

    return tax, rebate, final_tax

def show_tax():
    income_str = entry_income.get().strip()
    
    if not income_str:
        messagebox.showerror("Error", "Please enter your income.")
        return
    
    try:
        income = float(income_str)
        if income < 0:
            messagebox.showerror("Error", "Income cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric income.")
        return

    tax, rebate, final_tax = calculate_tax(income)

    result_text = f"Tax before rebate: ₹{tax:.2f}\nRebate (87A): ₹{rebate:.2f}\nFinal Tax Payable: ₹{final_tax:.2f}"
    result_label.config(text=result_text)

def save_details():
    income_str = entry_income.get().strip()
    
    if not income_str:
        messagebox.showerror("Error", "Please enter your income.")
        return

    try:
        income = float(income_str)
        if income < 0:
            messagebox.showerror("Error", "Income cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric income.")
        return

    tax, rebate, final_tax = calculate_tax(income)

    try:
        with open("tax_records.txt", "a") as f:
            f.write(f"Income: ₹{income:.2f}, Tax: ₹{tax:.2f}, Rebate: ₹{rebate:.2f}, Final Tax: ₹{final_tax:.2f}\n")
        messagebox.showinfo("Success", "Details saved successfully in 'tax_records.txt'!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save: {e}")

def clear_fields():
    entry_income.delete(0, tk.END)
    result_label.config(text="")

def show_about():
    messagebox.showinfo("About", "Income Tax Calculator\nFinal Year Project\nMade by Madhav!")

# GUI
root = tk.Tk()
root.title("Income Tax Calculator")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

heading = tk.Label(root, text="Income Tax Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#2e7d32")
heading.pack(pady=10)

entry_label = tk.Label(root, text="Enter Annual Income (₹):", font=("Arial", 12), bg="#f0f0f0")
entry_label.pack(pady=5)

entry_income = tk.Entry(root, font=("Arial", 12))
entry_income.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

calc_btn = tk.Button(btn_frame, text="Calculate Tax", font=("Arial", 12), bg="#4caf50", fg="white", command=show_tax)
calc_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(btn_frame, text="Save Details", font=("Arial", 12), bg="#2196f3", fg="white", command=save_details)
save_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 12), bg="#f44336", fg="white", command=clear_fields)
clear_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 13), bg="#f0f0f0", justify="left")
result_label.pack(pady=20)

about_btn = tk.Button(root, text="About", font=("Arial", 10), bg="#757575", fg="white", command=show_about)
about_btn.pack(side="bottom", pady=10)

root.mainloop()
