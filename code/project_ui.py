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

entryvalues = []
entries = []
entrycolumn = -1
entryrowstart = 0
entryrow = 0
rawentrycount = 0
entrycount = 0

def remove(entry: customtkinter.CTkEntry, button: customtkinter.CTkButton):
    global entrycount, rawentrycount, entryvalues
    global frame
    if (entrycount == 1):
        return
    for i in frame.winfo_children():
        if (isinstance(i, customtkinter.CTkEntry)):
            if (i.get() != "" and i.get() != entry.get()):
                entryvalues.append(i.get())             
    entry.destroy()
    button.destroy()
    entrycount = 0
    rawentrycount -= 1
    for i in frame.winfo_children():
        i.destroy()
    for i in entryvalues:
        addDetailedEntry(i)
        rawentrycount -= 1
    rawentrycount -= len(entryvalues)
    entryvalues = []
    for i in range(0, rawentrycount):
        addEntry()
    rawentrycount = entrycount

def addDetailedEntry(string):
    global frame
    global entrycolumn
    global entryrow, entryrowstart
    global entrycount, rawentrycount
    if (entrycount >= 36):
        return
    if entrycount % 12 == 0:
        entrycolumn = entrycount/12
    stringvar = customtkinter.StringVar()
    stringvar.set(string)
    entryrow = entrycount % 12
    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Location", textvariable=stringvar, width=(425/3-(340/12)))
    entry.place(x=entrycolumn*(425/3),y=entryrow*(340/12))
    entrybutton = customtkinter.CTkButton(master=frame, text="-", font=("Roboto", 13, "bold"), command=lambda: remove(entry, entrybutton), width=340/12, fg_color="#b94040")
    entrybutton.place(x=(entrycolumn + 1)*(425/3) - (340/12), y=entryrow*(340/12))
    entries.append(entry)
    entrycount += 1
    rawentrycount += 1


def addEntry():
    global frame
    global entrycolumn
    global entryrow, entryrowstart
    global entrycount, rawentrycount
    if (entrycount >= 36):
        return
    if entrycount % 12 == 0:
        entrycolumn = entrycount/12
    entryrow = entrycount % 12
    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Location", width=(425/3-(340/12)))
    entry.place(x=entrycolumn*(425/3),y=entryrow*(340/12))
    entrybutton = customtkinter.CTkButton(master=frame, text="-", font=("Roboto", 13, "bold"), command=lambda: remove(entry, entrybutton), width=340/12, fg_color="#b94040")
    entrybutton.place(x=(entrycolumn + 1)*(425/3) - (340/12), y=entryrow*(340/12))
    entries.append(entry)
    entrycount += 1
    rawentrycount += 1

def enterButton():
    locations = []
    for i in frame.winfo_children():
        if (isinstance(i, customtkinter.CTkEntry) and i.get() != ""):
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