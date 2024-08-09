from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Temperature Mapping")
root.configure(background="#665d82")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

ttk.Label(root, text="One is responsible for all he is involved").grid(column=0, row=0)
ttk.Label(root, text="- Maya Angelou").grid(column=0, row=1)

root.mainloop()