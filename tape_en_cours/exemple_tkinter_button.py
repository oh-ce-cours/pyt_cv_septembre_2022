import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

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
    showinfo(title="Information", message="Download button clicked!")


# exit button
exit_button = ttk.Button(root, text="Cliquez moi !", command=action_button)
exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
print("apres la mainloop")
