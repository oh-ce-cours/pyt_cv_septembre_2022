import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import time
# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Button Demo")


def action_button():
    # action a effectuer quand on a cliqué sur le bouton
    # dans ce cadre, c'est une fonction de callback ou de rappel
    # on ne sait pas quand elle est appelée, c'est le framework qui le décide
    print("bouton cliqué")
    time.sleep(20)
    filenames = fd.askopenfilenames()
    showinfo(title="Information", message=f"{filenames}")
    for filename in filenames:
        print(open(filename).readline())


# exit button
exit_button = ttk.Button(root, text="Cliquez moi !", command=action_button)
exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
print("apres la mainloop")
