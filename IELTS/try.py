
import tkinter as tk
import time
from tkinter import *

import os
from PIL import ImageTk, Image
import sounddevice as sd
from scipy.io.wavfile import write

def txt_Editor():
    import Notepad

def Delete_screen():
    screen.destroy()


def speaking_Test():

    def Og():
        def stop():
            return KeyboardInterrupt

        Button(speaking,text = "Stop Recording ",height = "2", width = "30", command = stop).pack()
        
    def calling():
        test_name = test_entry.get()
        if test_name == "1":
            Image.open(r"C:\\Users\becto\Desktop\Documents\\Python Scripts\\IELTS\1.jpg").show()
            
            
        elif test_name=="2":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="3":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="4":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name=="5":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="6":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="7":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="8":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="9":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        elif test_name =="10":
            Image.open(r"C:\Users\becto\Desktop\Documents\Python Scripts\IELTS\1.jpg").show()
        
    global speaking
    speaking = Toplevel(screen)
    speaking.title("IELTS Speaking")
    speaking.geometry("500x500")
    
    test = StringVar()
    print("Checkpoint 1")
    global test_entry
    test_entry =  Entry(speaking, textvariable = test)
    test_entry.pack()
    print("Checkpoint 2")
    print("Checkpoint 3")
    calling()
    Button(speaking,text = "Record my test",height = "2", width = "30", command = Og).pack()
    
    

def main_screen():
  global screen
  screen = Tk()
  screen.configure(bg='#cc1a30')
  screen.geometry("650x700")
  photo = ImageTk.PhotoImage(Image.open("ielts.jpg"))
  panel = Label(screen, image = photo,bg='#cc1a30' )
  panel.pack( side = tk.TOP, fill = tk.X , expand = False)
  screen.title("IELTS TEST TAKER")
  Label(text = "Welcome! IELTS TEST TAKER", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "", bg='#cc1a30' ).pack()
  Button(text = "Give Listening Test", height = "2", width = "30", command ="speaking_Test" ).pack()
  Label(text = "", bg='#cc1a30' ).pack()
  Button(text = "Give Reading Test",height = "2", width = "30", command = "speaking_Test").pack()
  Label(text = "", bg='#cc1a30' ).pack()
  Button(text = "Give Writing Test", height = "2", width = "30", command = txt_Editor).pack()
  Label(text = "", bg='#cc1a30' ).pack()
  Button(text = "Give Speaking Test", height = "2", width = "30", command = speaking_Test).pack()
  Label(text = "", bg='#cc1a30' ).pack()
  Button(text = "EXIT", height = "2", width = "30", command = Delete_screen).pack()
  screen.mainloop()

main_screen()
  
