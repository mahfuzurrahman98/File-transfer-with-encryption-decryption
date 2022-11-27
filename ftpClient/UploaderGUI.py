import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile


class UploaderGUI:
    file_path = ""

    def openWindow(self):
        file = filedialog.askopenfilename()
        f_obj = open(file, 'r')
        self.file_path = f_obj.name
        f_obj.name

    def closeWindow(self, window):
        window.destroy()

    def getPath(self):
        return self.file_path

    def run(self):
        window = tk.Tk()
        window.geometry("210x100")  # Size of the window
        window.resizable(width=False, height=False)
        window.title('ftpClient')
        b1 = tk.Button(window, text='Upload File', width=25,
                       command=lambda: self.openWindow())
        b2 = tk.Button(window, text='Send', width=10,
                       command=lambda: self.closeWindow(window))
        b1.grid(row=2, column=1)
        b2.grid(row=6, column=1)
        window.mainloop()

