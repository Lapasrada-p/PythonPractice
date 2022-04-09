#GUI-caluculator

from tkinter import *
from tkinter import ttk,messagebox
from tkinter import font

GUI = Tk() 
GUI.title("Supermarket")
GUI.geometry('900x750')

bg = PhotoImage(file='supermarket.png')
BG = Label(GUI, image=bg)
BG.pack()

title = Label(GUI,text="Welcome to Supermerket", font=(NORMAL,20))
title.pack(pady=5)

K = Label(GUI,text="กรุณากรอกราคาสินค้าต่อหน่วย", font=(NORMAL,20))
K.pack()

v_numberofGoods = StringVar()        #keep value of the number of goods
E = ttk.Entry(GUI, textvariable=v_numberofGoods, font=(NORMAL,20))  
E.pack()

L = Label(GUI,text="กรุณากรอกจำนวนสินค้า", font=(NORMAL,20))
L.pack()

v_quantity = StringVar()        #keep value of the cost of goods
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))  
E1.pack()

def Calculator():
    try:
        quan = float(v_quantity.get())
        quan1 = float(v_numberofGoods.get())
        if quan<=0 or quan1 <=0 :
            messagebox.showwarning('Error','Please input number greater than zero only')
            v_numberofGoods.set('')
            v_quantity.set('')
            E.focus()
        else: 
            calc = quan * quan1
            messagebox.showinfo('calculate','ราคาทั้งหมด {} บาท'.format(calc))
            v_numberofGoods.set('')
            v_quantity.set('')
            E.focus()
    except:
        messagebox.showwarning('Error','Please input number only')
        v_numberofGoods.set('')
        v_quantity.set('')
        E.focus()
        

button = ttk.Button(GUI, text='calculate', command= Calculator)
button.pack(ipadx=30, ipady=20, pady=20)  #inside padding
 
GUI.mainloop() #for program run all the time
