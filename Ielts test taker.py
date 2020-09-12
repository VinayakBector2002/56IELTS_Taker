
import tkinter as tk













from tkinter import *

import os
from PIL import ImageTk, Image
import sounddevice as sd
from scipy.io.wavfile import write

def txt_Editor():
    import tkinter 
    import os	 
    from tkinter.messagebox import *
    from tkinter.filedialog import *

    class Notepad: 

        __root = Tk() 

        # default window width and height 
        __thisWidth = 300
        __thisHeight = 300
        __thisTextArea = Text(__root) 
        __thisMenuBar = Menu(__root) 
        __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
        __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
        
        # To add scrollbar 
        __thisScrollBar = Scrollbar(__thisTextArea)	 
        __file = None

        def __init__(self,**kwargs): 

            # Set icon 
            try: 
                    self.__root.wm_iconbitmap("Notepad.ico") 
            except: 
                    pass

            # Set window size (the default is 300x300) 

            try: 
                self.__thisWidth = kwargs['width'] 
            except KeyError: 
                pass

            try: 
                self.__thisHeight = kwargs['height'] 
            except KeyError: 
                pass

            # Set the window text 
            self.__root.title("Untitled - Notepad") 

            # Center the window 
            screenWidth = self.__root.winfo_screenwidth() 
            screenHeight = self.__root.winfo_screenheight() 
        
            # For left-alling 
            left = (screenWidth / 2) - (self.__thisWidth / 2) 
            
            # For right-allign 
            top = (screenHeight / 2) - (self.__thisHeight /2) 
            
            # For top and bottom 
            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                                self.__thisHeight, 
                                                left, top)) 

            # To make the textarea auto resizable 
            self.__root.grid_rowconfigure(0, weight=1) 
            self.__root.grid_columnconfigure(0, weight=1) 

            # Add controls (widget) 
            self.__thisTextArea.grid(sticky = N + E + S + W) 
            
            # To open new file 
            self.__thisFileMenu.add_command(label="New", 
                                            command=self.__newFile)	 
            
            # To open a already existing file 
            self.__thisFileMenu.add_command(label="Open", 
                                            command=self.__openFile) 
            
            # To save current file 
            self.__thisFileMenu.add_command(label="Save", 
                                            command=self.__saveFile)	 

            # To create a line in the dialog		 
            self.__thisFileMenu.add_separator()										 
            self.__thisFileMenu.add_command(label="Exit", 
                                            command=self.__quitApplication) 
            self.__thisMenuBar.add_cascade(label="File", 
                                        menu=self.__thisFileMenu)	 
            
            # To give a feature of cut 
            self.__thisEditMenu.add_command(label="Cut", 
                                            command=self.__cut)			 
        
            # to give a feature of copy	 
            self.__thisEditMenu.add_command(label="Copy", 
                                            command=self.__copy)		 
            
            # To give a feature of paste 
            self.__thisEditMenu.add_command(label="Paste", 
                                            command=self.__paste)		 
            
            # To give a feature of editing 
            self.__thisMenuBar.add_cascade(label="Edit", 
                                        menu=self.__thisEditMenu)	 
            
            # To create a feature of description of the notepad 
            self.__thisHelpMenu.add_command(label="About Notepad", 
                                            command=self.__showAbout) 
            self.__thisMenuBar.add_cascade(label="Help", 
                                        menu=self.__thisHelpMenu) 

            self.__root.config(menu=self.__thisMenuBar) 

            self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
            
            # Scrollbar will adjust automatically according to the content		 
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
        
            
        def __quitApplication(self): 
            self.__root.destroy() 
            # exit() 

        def __showAbout(self): 
            showinfo("Notepad","Nothing to hide :)") 

        def __openFile(self): 
            
            self.__file = askopenfilename(defaultextension=".txt", 
                                        filetypes=[("All Files","*.*"), 
                                            ("Text Documents","*.txt")]) 

            if self.__file == "": 
                
                # no file to open 
                self.__file = None
            else: 
                
                # Try to open the file 
                # set the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                self.__thisTextArea.delete(1.0,END) 

                file = open(self.__file,"r") 

                self.__thisTextArea.insert(1.0,file.read()) 

                file.close() 

            
        def __newFile(self): 
            self.__root.title("Untitled - Notepad") 
            self.__file = None
            self.__thisTextArea.delete(1.0,END) 

        def __saveFile(self): 

            if self.__file == None: 
                # Save as new file 
                self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                                defaultextension=".txt", 
                                                filetypes=[("All Files","*.*"), 
                                                    ("Text Documents","*.txt")]) 

                if self.__file == "": 
                    self.__file = None
                else: 
                    
                    # Try to save the file 
                    file = open(self.__file,"w") 
                    file.write(self.__thisTextArea.get(1.0,END)) 
                    file.close() 
                    
                    # Change the window title 
                    self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                    
                
            else: 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 

        def __cut(self): 
            self.__thisTextArea.event_generate("<<Cut>>") 

        def __copy(self): 
            self.__thisTextArea.event_generate("<<Copy>>") 

        def __paste(self): 
            self.__thisTextArea.event_generate("<<Paste>>") 

        def run(self): 

            # Run main application 
            self.__root.mainloop() 




    # Run main application 
    notepad = Notepad(width=600,height=400) 
    notepad.run() 

def Delete_screen():
    screen.destroy()

def speaking_Test():
    def Og():
        import argparse
        import tempfile
        import queue
        import sys

        import sounddevice as sd
        import soundfile as sf
        import numpy  # Make sure NumPy is loaded before it is used in the callback
        assert numpy  # avoid "imported but unused" message (W0611)


        def int_or_str(text):
            """Helper function for argument parsing."""
            try:
                return int(text)
            except ValueError:
                return text


        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        args, remaining = parser.parse_known_args()
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            'filename', nargs='?', metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        parser.add_argument(
            '-c', '--channels', type=int, default=1, help='number of input channels')
        parser.add_argument(
            '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
        args = parser.parse_args(remaining)

        q = queue.Queue()


        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            q.put(indata.copy())


        try:
            if args.samplerate is None:
                device_info = sd.query_devices(args.device, 'input')
                # soundfile expects an int, sounddevice provides a float:
                args.samplerate = int(device_info['default_samplerate'])
            if args.filename is None:
                args.filename = tempfile.mktemp(prefix= test_entry.get()+'___' ,
                                                suffix='.wav', dir='')

            # Make sure the file is opened before recording anything:
            with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                            channels=args.channels, subtype=args.subtype) as file:
                with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                    channels=args.channels, callback=callback):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while True:
                        file.write(q.get())
        except KeyboardInterrupt:
            print('\nRecording finished: ' + repr(args.filename))
            parser.exit(0)
        except Exception as e:
            parser.exit(type(e).__name__ + ': ' + str(e))

    def stop():
        return KeyboardInterrupt
      

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
    Button(speaking,text = "Stop Recording ",height = "2", width = "30", command = stop).pack()
    

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
  
