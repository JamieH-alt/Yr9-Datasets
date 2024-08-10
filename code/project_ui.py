import tkinter

import customtkinter
import customtkinter as ctk
from PIL import Image

import project_main

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("625x350")
root.minsize(625, 340)
root.maxsize(625, 340)
root.title("CTTM Temperature Mapping")

frame = customtkinter.CTkFrame(master=root, height=340, width=425)
frame.place(x=200, y=0)
frame2 = customtkinter.CTkFrame(master=root, width=200, height=340)
frame2.place(x=0, y=0)

frame.columnconfigure(1, weight=1, pad=0)
frame.columnconfigure(2, weight=1, pad=0)

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)

label = customtkinter.CTkLabel(master=frame2, text="Temperature Mapping", font=("Roboto", 18))
label.place(relx=0.05, rely=0)

entries = []
entrycolumn = -1
entryrowstart = 0
entryrow = 0
def addEntry():
    global frame
    global entrycolumn
    global entryrow, entryrowstart
    if entrycolumn == 2:
        if (len(entries) % 12 == 0):
            return
    if len(entries) % 12 == 0:
        if (entrycolumn == 2):
            entrycolumn = 0
        else:
            entrycolumn += 1
        entryrow = entryrowstart
    entryrow += 1
    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Location").grid(row=entryrow, column=entrycolumn)
    entries.append(entry)

def enterButton():
    locations = []
    for i in frame.winfo_children():
        if (i.get() != ""):
            locations.append(i.get())
    if len(locations) == 0:
        return
    project_main.registerLocations(locations)

def show():
    global frame
    image = customtkinter.CTkImage(dark_image=Image.open('logo.png'), size=(100, 75))
    label = customtkinter.CTkLabel(master=frame2, text="", image=image).place(relx=0.25, rely=0.3)
    button = customtkinter.CTkButton(master=frame2, text="+", font=("Roboto", 11), command=addEntry).place(relx=0.15, rely=0.8)
    enterbutton = customtkinter.CTkButton(master=frame2, text="Enter", font=("Roboto", 11), command=enterButton).place(relx=0.15, rely=0.9)

addEntry()
show()

root.mainloop()