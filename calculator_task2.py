"""Muhammad Talha"""
from tkinter import *
import math

def press_btn(numb):
    global txt
    txt=txt+str(numb)
    txt_lbl.set(txt)
def clear():
    global txt
    txt_lbl.set("")
    txt=""
def equalto():
    global txt
    try:
        total=str(eval(txt))
        
        txt_lbl.set(total)
        txt=total
   
    except SyntaxError:
        txt_lbl.set("Syntax Error")
        txt=""
    except :
         txt_lbl.set(Error)
         txt=""
def sqr_root():
    global txt
    try:
        result = math.sqrt(float(txt))
        txt_lbl.set(result)
        txt = str(result)
    except:
        txt_lbl.set("Error")
        txt = ""

def fact():
    global txt
    try:
        num = int(txt)
        if num < 0:
            txt_lbl.set("Error")
            txt = ""
        else:
            result = math.factorial(num)
            txt_lbl.set(result)
            txt = str(result)
    except:
        txt_lbl.set("Error")
        txt = ""

root=Tk()
root.title("Calculator")
root.geometry("450x450")
txt=""
txt_lbl=StringVar()

label=Label(root, textvariable=txt_lbl,font=('bold',20),bg="white",width=20,height=1,relief="solid")
label.pack()
frame=Frame(root)
frame.pack()



padx = 0.1 * root.winfo_fpixels("1i")  # Convert 1 inch to pixels
pady = 0.1 * root.winfo_fpixels("1i")

btn1=Button(frame,text=1,height=2,width=7,font=30,
            command=lambda:press_btn(1))
btn1.grid(row=3,column=0, padx=padx, pady=pady)

btn2=Button(frame,text=2,height=2,width=7,font=30,
            command=lambda:press_btn(2))
btn2.grid(row=3,column=1, padx=padx, pady=pady)

btn3=Button(frame,text=3,height=2,width=7,font=30,
            command=lambda:press_btn(3))
btn3.grid(row=3,column=2, padx=padx, pady=pady)

btn4=Button(frame,text=4,height=2,width=7,font=30,
            command=lambda:press_btn(4))
btn4.grid(row=2,column=0, padx=padx, pady=pady)

btn5=Button(frame,text=5,height=2,width=7,font=30,
            command=lambda:press_btn(5))
btn5.grid(row=2,column=1, padx=padx, pady=pady)

btn6=Button(frame,text=6,height=2,width=7,font=30,
            command=lambda:press_btn(6))
btn6.grid(row=2,column=2, padx=padx, pady=pady)

btn7=Button(frame,text=7,height=2,width=7,font=30,
            command=lambda:press_btn(7))
btn7.grid(row=1,column=0, padx=padx, pady=pady)

btn8=Button(frame,text=8,height=2,width=7,font=30,
            command=lambda:press_btn(8))
btn8.grid(row=1,column=1, padx=padx, pady=pady)

btn9=Button(frame,text=9,height=2,width=7,font=30,
            command=lambda:press_btn(9))
btn9.grid(row=1,column=2, padx=padx, pady=pady)

btn0=Button(frame,text=0,height=2,width=7,font=30,
            command=lambda:press_btn(0))
btn0.grid(row=4,column=1, padx=padx, pady=pady)

mark=Button(frame,text="!",height=2,width=7,font=30,
            command=fact)
mark.grid(row=4,column=0, padx=padx, pady=pady)

dec=Button(frame,text=".",height=2,width=7,font=30,
            command=lambda:press_btn("."))
dec.grid(row=4,column=2, padx=padx, pady=pady)

equal=Button(frame,text="=",height=2,width=7,font=30,
            command=equalto)
equal.grid(row=4,column=3, padx=padx, pady=pady)

plus=Button(frame,text="+",height=2,width=7,font=30,
            command=lambda:press_btn("+"))
plus.grid(row=3,column=3, padx=padx, pady=pady)

minus=Button(frame,text="-",height=2,width=7,font=30,
            command=lambda:press_btn("-"))
minus.grid(row=2,column=3, padx=padx, pady=pady)

mult=Button(frame,text="*",height=2,width=7,font=30,
            command=lambda:press_btn("*"))
mult.grid(row=1,column=3, padx=padx, pady=pady)

div=Button(frame,text="/",height=2,width=7,font=30,
            command=lambda:press_btn("/"))
div.grid(row=0,column=1, padx=padx, pady=pady)

sqr_root=Button(frame,text="√",height=2,width=7,font=30,
            command=sqr_root)
sqr_root.grid(row=0,column=2, padx=padx, pady=pady)

bt=Button(frame,text="<-",height=2,width=7,font=30,
            command=lambda:press_btn("<-"))
bt.grid(row=0,column=3, padx=padx, pady=pady)

clr=Button(frame,text="C",height=2,width=7,font=30,
            command=clear)
clr.grid(row=0,column=0, padx=padx, pady=pady)

root.mainloop()
