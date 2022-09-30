import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Button Demo")


def action_button():
    print("bouton cliqué")


# exit button
exit_button = ttk.Button(root, text="Cliquez moi !", command=action_button())

exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
print("apres la mainloop")
