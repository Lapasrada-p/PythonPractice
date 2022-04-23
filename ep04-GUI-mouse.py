#pip install pyinstaller

from tkinter import * # Lib: Tk Interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title("Program for pressing to do something")
GUI.geometry('500x300')

def Calendar():
    pg.click(1855,1055)

def Google():
    webbrowser.open("https://www.google.com")
    
def PageLoong():
    webbrowser.open("https://www.facebook.com/loong.wissawakorn/")
B1 = Button(GUI, text= "Calandar", command=Calendar)
B1.pack(ipadx= 20, ipady =10, pady=20)

B2 = ttk.Button(GUI, text= "Google", command=Google)
B2.pack(ipadx= 20, ipady =10, pady=20)

B3 = ttk.Button(GUI, text= "Uncle engineer", command=PageLoong)
B3.pack(ipadx= 20, ipady =10, pady=20)

GUI.mainloop()