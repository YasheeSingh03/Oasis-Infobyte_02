# weight(kg)/height2(m2)
import tkinter as tk
import tkinter as tk
from tkinter import font
from tkinter import messagebox, simpledialog, font

def generate_password():
    n=float(user_entry.get())
    en=float(entry1.get())
    bmi=n/(en**2)
    pass_ent.delete(0, tk.END)
    pass_ent.insert(tk.END, bmi)

    if bmi<18.5:
        messagebox.showinfo("", f"Your Bmi is, {bmi}. You are Underweight!")
    elif (bmi>18.5):
        messagebox.showinfo("", f"Your Bmi is, {bmi}. You have Normal Weight!")
    elif (bmi>25):
        messagebox.showinfo("", f"Your Bmi is, {bmi}. You are Overweight!")
    elif bmi>30:
        messagebox.showinfo("", f"Your Bmi is, {bmi}. You are Obese!")

def reset():
    user_entry.delete(0,tk.END)
    entry1.delete(0,tk.END)
    pass_ent.delete(0,tk.END)

    

window = tk.Tk()
window.title("BMI CALCULATOR")
p=tk.Label(window,text="BMI CALCULATOR",fg="blue",font=("Arial", 12, "bold"))

custom_font = font.Font(p,p.cget("font"))
custom_font.configure(underline=True, size=10)

p.configure(font=custom_font)

p.grid(row=0,column=1)

user_name=tk.Label(window,text="Weight(in kg):")
user_entry=tk.Entry(window)
user_name.grid(row=4,column=0,padx=10,pady=5)
user_entry.grid(row=4,column=1)
pass_len=tk.Label(window,text="Height(in meter):")
entry1=tk.Entry(window)

pass_len.grid(row=5,column=0,padx=10,pady=5)
entry1.grid(row=5,column=1)
pass_label = tk.Label(window, text="YOUR BMI:")
pass_ent = tk.Entry(window)
pass_label.grid(row=6,column=0,padx=10,pady=5)
pass_ent.grid(row=6 ,column=1)


gen_pass = tk.Button(window, text="BMI",fg="white",bg="blue", command=generate_password)
gen_pass.grid(row=7,column=1,sticky="nsew",padx=12,pady=6)

reset=tk.Button(window,text="Reset",command=reset)
reset.grid(row=9,column=1,sticky="nsew",padx=18,pady=6)
window.mainloop()