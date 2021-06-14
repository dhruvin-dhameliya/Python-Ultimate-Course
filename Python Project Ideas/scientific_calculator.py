from tkinter import * 
import tkinter
from tkinter import messagebox
import math as m

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error" 
                messagebox.showerror("Error","Can not valid operation.")

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


def clear():
    ex = screen.get()
    ex = ex[0:len(ex)-1]
    screen.delete(0, END)
    screen.insert(0, ex)

# Some useful variabes
font=("Verdana", 32)


root = Tk()
root.geometry("400x675+500+75")
# root.resizable(0,0) # ----------------------------> ReSizeble the Calcuator
root.title("Calculator By Dhruvin")
root.wm_iconbitmap('F:\Calc_logo.png')
root.iconphoto(False,tkinter.PhotoImage(file='F:\Calc_logo.png'))


# Screen in display text:
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font='Verdana 45', justify=RIGHT)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Buttons:
btnFrame = Frame(root)
btnFrame.pack()

btn_Clr = Button(btnFrame, text="←", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white", fg="orange", command=clear)
btn_Clr.grid(row=0, column=3)


btn_C = Button(btnFrame, text="C", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white", fg="orange")
btn_C.grid(row=1, column=0)
btn_C.bind("<Button-1>", click)


btn_br = Button(btnFrame, text="()", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_br.grid(row=1, column=1)
btn_br.bind("<Button-1>", click)


btn_pr = Button(btnFrame, text="%", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_pr.grid(row=1, column=2)
btn_pr.bind("<Button-1>", click)


btn_div = Button(btnFrame, text="/", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_div.grid(row=1, column=3)
btn_div.bind("<Button-1>", click)


btn_7 = Button(btnFrame, text="7", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_7.grid(row=2, column=0)
btn_7.bind("<Button-1>", click)


btn_8 = Button(btnFrame, text="8", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_8.grid(row=2, column=1)
btn_8.bind("<Button-1>", click)


btn_9 = Button(btnFrame, text="9", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_9.grid(row=2, column=2)
btn_9.bind("<Button-1>", click)


btn_mul = Button(btnFrame, text="*", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_mul.grid(row=2, column=3)
btn_mul.bind("<Button-1>", click)


btn_4 = Button(btnFrame, text="4", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_4.grid(row=3, column=0)
btn_4.bind("<Button-1>", click)


btn_5 = Button(btnFrame, text="5", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_5.grid(row=3, column=1)
btn_5.bind("<Button-1>", click)


btn_6 = Button(btnFrame, text="6", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_6.grid(row=3, column=2)
btn_6.bind("<Button-1>", click)


btn_min = Button(btnFrame, text="-", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_min.grid(row=3, column=3)
btn_min.bind("<Button-1>", click)


btn_1 = Button(btnFrame, text="1", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_1.grid(row=4, column=0)
btn_1.bind("<Button-1>", click)


btn_2 = Button(btnFrame, text="2", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_2.grid(row=4, column=1)
btn_2.bind("<Button-1>", click)


btn_3 = Button(btnFrame, text="3", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_3.grid(row=4, column=2)
btn_3.bind("<Button-1>", click)


btn_add = Button(btnFrame, text="+", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_add.grid(row=4, column=3)
btn_add.bind("<Button-1>", click)


btn_pm = Button(btnFrame, text="±", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_pm.grid(row=5, column=0)
btn_pm.bind("<Button-1>", click)


btn_0 = Button(btnFrame, text="0", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_0.grid(row=5, column=1)
btn_0.bind("<Button-1>", click)


btn_dot = Button(btnFrame, text=".", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white")
btn_dot.grid(row=5, column=2)
btn_dot.bind("<Button-1>", click)



btn_eql = Button(btnFrame, text="=", font=font, width=3, relief="ridge", activebackground="orange", activeforeground="white", fg="orange")
btn_eql.grid(row=5, column=3)
btn_eql.bind("<Button-1>", click)



# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************



# Scientific Calculator :
scFrame = Frame(root)

btn_sin = Button(scFrame, text="sin", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_sin.grid(row=1, column=4)

btn_cos = Button(scFrame, text="cos", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_cos.grid(row=1, column=5)

btn_tan = Button(scFrame, text="tan", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_tan.grid(row=1, column=6)

btn_sinh = Button(scFrame, text="sinh", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_sinh.grid(row=2, column=4)

btn_cosh = Button(scFrame, text="cosh", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_cosh.grid(row=2, column=5)

btn_tanh = Button(scFrame, text="tanh", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_tanh.grid(row=2, column=6)

btn_pow = Button(scFrame, text="˄", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_pow.grid(row=3, column=4)

btn_sqrt = Button(scFrame, text="√", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_sqrt.grid(row=3, column=5)

btn_fecto = Button(scFrame, text="x!", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_fecto.grid(row=3, column=6)

btn_Deg = Button(scFrame, text="Deg", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_Deg.grid(row=4, column=4)

btn_Rad = Button(scFrame, text="Rad", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_Rad.grid(row=4, column=5)

btn_log = Button(scFrame, text="log", font="Verdana 32", width=4, relief="ridge", activebackground="orange", activeforeground="white")
btn_log.grid(row=4, column=6)





normalcalc = True

# Function Start:
def calculator_sc(event):
    btn = event.widget
    text = btn['text']
    ex = screen.get()
    answer = ''
    if text == 'Deg':
        answer = str(m.degrees(float(ex)))

    elif text == 'Rad':
        answer = str(m.radians(float(ex)))

    elif text == 'sin':
        answer = str(m.sin(m.radians(int(ex))))

    elif text == 'cos':
        answer = str(m.cos(m.radians(int(ex))))
    
    elif text == 'tan':
        answer = str(m.tan(m.radians(int(ex))))
    
    elif text == 'sinh':
        answer = str(m.sinh(m.radians(int(ex))))
    
    elif text == 'cosh':
        answer = str(m.cosh(m.radians(int(ex))))
    
    elif text == 'tanh':
        answer = str(m.tanh(m.radians(int(ex))))
    
    elif text == '˄':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    
    elif text == '√':
        answer = m.sqrt(int(ex))
    
    elif text == 'x!':
        answer = str(m.factorial(int(ex)))

    elif text == 'log':
        answer = str(m.log10(int(ex)))


    screen.delete(0, END) 
    screen.insert(0, answer) 


def sc_click():
    global normalcalc
    if normalcalc:
        btnFrame.pack_forget()
        scFrame.pack(side=LEFT)
        btnFrame.pack(side=LEFT)
        root.geometry("725x675+500+75")
        normalcalc = False
    else:
        scFrame.pack_forget()
        root.geometry("400x675+500+75")
        normalcalc = True

# End Function...
btn_Deg.bind("<Button-1>", calculator_sc)
btn_Rad.bind("<Button-1>", calculator_sc)
btn_sin.bind("<Button-1>", calculator_sc)
btn_cos.bind("<Button-1>", calculator_sc)
btn_tan.bind("<Button-1>", calculator_sc)
btn_sinh.bind("<Button-1>", calculator_sc)
btn_cosh.bind("<Button-1>", calculator_sc)
btn_tanh.bind("<Button-1>", calculator_sc)
btn_pow.bind("<Button-1>", calculator_sc)
btn_sqrt.bind("<Button-1>", calculator_sc)
btn_fecto.bind("<Button-1>", calculator_sc)
btn_log.bind("<Button-1>", calculator_sc)


fontMenu=("", 15)

menubar = Menu(root)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific", command=sc_click) 

menubar.add_cascade(label="≡ Open Navigation", menu=mode)

root.config(menu=menubar)

root.mainloop()
