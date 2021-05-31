import tkinter 
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox


val = ""
A = 0
operator = ""


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
    
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_C_isclicked():
    global A 
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)
    

def btn_bre_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "()"
    val = val + "()"
    data.set(val)

def btn_per_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "%"
    val = val + "%"
    data.set(val)

def btn_div_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_mul_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_min_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_sub_isclicked():
    global operator
    global val
    global A 
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_eql_isclicked():
    global operator
    global val
    global A 
    A = float(val)
    operator = "="
    val = val + "="
    data.set(val)

def btn_dot_isclicked():
    global val
    val = val + "."
    data.set(val)

def btn_zero_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_pm_isclicked():
    global operator
    global val
    global A
    A = float(val)
    operator = "+/-"
    val = val + "+/-"
    data.set(val)



def result():
    global operator
    global val
    global A
    val2 = val
    if operator == "+" :
        x = float((val2.split("+")[1]))
        C = A + x    
        data.set(C)
        val = str(C) 

    elif operator == "-" :
        x = float((val2.split("-")[1]))
        C = A - x    
        data.set(C)
        val = str(C) 

    elif operator == "*" :
        x = float((val2.split("*")[1]))
        C = A * x    
        data.set(C)
        val = str(C) 

    elif operator == "/" :
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Division By 0 Not Support")
            A = ""
            val = ""
            data.set(val)
        else:
            C = float(A / x)
            data.set(C)
            val = str(C)

    elif operator == "%" :
        x = float((val2.split("%")[1]))
        C = A % x    
        data.set(C)
        val = str(C)

    elif operator == "." :
        x = float((val2.split(".")[1]))
        C = A . A    
        data.set(C)
        val = str(C) 



root = tkinter.Tk()
root.geometry("350x550+300+300")
# root.resizable(0,0)  ----------------------------> ReSizeble the Calcuator
root.title("Calculator")
root.wm_iconbitmap('F:\Calc_logo.png')
root.iconphoto(False, tk.PhotoImage(file='F:\Calc_logo.png'))



data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font = ("Arial", 48,),
    textvariable=data,
    background="white",
    fg="black",
)
lbl.pack(expand=True, fill="both")

brow1 = Frame(root,bg="light grey")
brow1.pack(expand = TRUE, fill = "both",)

brow2 = Frame(root)
brow2.pack(expand = TRUE, fill = "both",)

brow3 = Frame(root)
brow3.pack(expand = TRUE, fill = "both",)

brow4 = Frame(root)
brow4.pack(expand = TRUE, fill = "both",)

brow5 = Frame(root)
brow5.pack(expand = TRUE, fill = "both",)


btn1 = Button(
    brow1,
    text = "C",
    font = ("Arial", 26, BOLD),
    relief=GROOVE,
    border=0,
    command=btn_C_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)


btn2 = Button(
    brow1,
    text = "()",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_bre_isclicked,

)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    brow1,
    text = "%",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_per_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    brow1,
    text = "/",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_div_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

# ---------------------------------------------------

btn1 = Button(
    brow2,
    text = "7",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0, 
    command=btn_7_isclicked, 
)
btn1.pack(side=LEFT, expand=True, fill="both",)


btn2 = Button(
    brow2,
    text = "8",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0, 
    command=btn_8_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    brow2,
    text = "9",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    brow2,
    text = "*",
    font = ("Arial", 24,),
    relief=GROOVE,
    border=0,
    command=btn_mul_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

# -------------------------------------------------

btn1 = Button(
    brow3,
    text = "4",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0, 
    command=btn_4_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)


btn2 = Button(
    brow3,
    text = "5",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    brow3,
    text = "6",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    brow3,
    text = "-",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_min_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

# ------------------------------------------------------


btn1 = Button(
    brow4,
    text = "1",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0, 
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)


btn2 = Button(
    brow4,
    text = "2",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    brow4,
    text = "3",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    brow4,
    text = "+",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0, 
    command=btn_sub_isclicked,

)
btn4.pack(side=LEFT, expand=True, fill="both",)

# ----------------------------------------------------


btn1 = Button(
    brow5,
    text = "+/-",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_pm_isclicked, 
)
btn1.pack(side=LEFT, expand=True, fill="both",)


btn2 = Button(
    brow5,
    text = "0",
    font = ("Arial", 26,),
    relief=GROOVE,
    border=0,
    command=btn_zero_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    brow5,
    text = ".",
    font = ("Arial", 26, BOLD),
    relief=GROOVE,
    border=0, 
    command=btn_dot_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    brow5,
    text = "=",
    font = ("Arial", 26, BOLD),
    relief=GROOVE,
    border=0,
    command=result,
)
btn4.pack(side=LEFT, expand=True, fill="both",)


root.mainloop()