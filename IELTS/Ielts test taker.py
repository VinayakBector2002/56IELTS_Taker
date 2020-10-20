
import tkinter as tk






from tkinter import *


import os
from PIL import ImageTk, Image
import sounddevice as sd
from scipy.io.wavfile import write

def txt_Editor():
    import Notepad

def Delete_screen():
    screen.destroy()
def Listening_Test():
    from tkinter import filedialog
    from pygame import mixer

    class MusicPlayer:
        def __init__(self, window ):
            window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
            Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
            Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
            Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
            Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
            Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60) 
            self.music_file = False
            self.playing_state = False
        def load(self):
            self.music_file = filedialog.askopenfilename()
        def play(self):
            if self.music_file:
                mixer.init()
                mixer.music.load(self.music_file)
                mixer.music.play()
        def pause(self):
            if not self.playing_state:
                mixer.music.pause()
                self.playing_state=True
            else:
                mixer.music.unpause()
                self.playing_state = False
        def stop(self):
            mixer.music.stop()
    global Listening
    Listening = Toplevel(screen)
    Listening.title("IELTS Listening")
    Listening.geometry("500x500")
    MusicPlayer(Listening)   
def speaking_Test():
    def OG2():
        Button(speaking,text = "Stop Recording ",height = "2", width = "30", command = stop).pack()
        import VoiceRecorder


    def Og():
        Button(speaking,text = "Stop Recording ",height = "2", width = "30", command = stop).pack()
        import argparse
        import tempfile
        import queue
        import sys

        import sounddevice as sd
        import soundfile as sf
        import numpy  # Make sure NumPy is loaded before it is used in the callback
        assert numpy  # avoid "imported but unused" message (W0611)
        print("Og check")
        


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
    global stop 
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
    Button(speaking,text = "Record my test",height = "2", width = "30", command = OG2).pack()
    
    

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
  Button(text = "Give Listening Test", height = "2", width = "30", command =Listening_Test ).pack()
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
  
