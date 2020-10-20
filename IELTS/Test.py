import tkinter as tk
import threading

class App():
    def __init__(self, master):
        self.isrecording = False
        self.button = tk.Button(main, text='rec')
        self.button.bind("<Button-1>", self.startrecording)
        self.button.bind("<ButtonRelease-1>", self.stoprecording)
        self.button.pack()

    def startrecording(self, event):
        self.isrecording = True
        t = threading.Thread(target=self._record)
        t.start()

    def stoprecording(self, event):
        self.isrecording = False

    def _record(self):
        while self.isrecording:
            print ("Recording")

main = tk.Tk()
app = App(main)
main.mainloop()
