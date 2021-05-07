from PageExportIP import PageExportIP
from PageLoadIP import PageLoadIP
from tkinter import *

import settings
import tkinter as tk




class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888", "darkGreen": "#5c8712"}
        self.navIcon = PhotoImage(file="Resources/menu.png")
        self.closeIcon = PhotoImage(file="Resources/close.png")
        self.btnState = False

        p1 = PageLoadIP(self)
        p1.config(bg=color["white"])

        p2 = PageExportIP(self)
        p2.config(bg=color["white"])

        #p3 = Page3(self)

        buttonframe = tk.Frame(self, bg=color["green"])
        container = tk.Frame(self, bg=color["white"])

        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        homeLabel = tk.Label(buttonframe, text="IP Tracker", font="Bahnschrift 15", bg=color["green"], fg="gray17", height=2, padx=20)
        homeLabel.pack(side="right")

        p1.place(in_=container, x=280, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=280, y=0, relwidth=1, relheight=1)
        #p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.navRoot = tk.Frame(self, bg="gray17", height=1000, width=270)
        self.navRoot.place(x=-270, y=0)
        tk.Label(self.navRoot, font="Bahnschrift 15", bg=color["green"], fg="black", height=2, width=270, padx=20).place(x=0, y=0)

        b1 = tk.Button(self.navRoot, text="Cargar IPs", command=p1.lift, font="BahnschriftLight 15", bg="gray17", fg=color["white"], activebackground="gray17", activeforeground="green", bd=0)
        b2 = tk.Button(self.navRoot, text="Visualizar IPs", command=p2.updateTable, font="BahnschriftLight 15", bg="gray17", fg=color["white"], activebackground="gray17", activeforeground="green", bd=0)

        b1.place(x=25, y=80)
        b2.place(x=25, y=120)

        def switch():
            if self.btnState is True:
                for x in range(271):
                    self.navRoot.place(x=-x, y=0)
                    buttonframe.update()

                self.btnState = False
            else:
                for x in range(-270, 0):
                    self.navRoot.place(x=x, y=0)
                    buttonframe.update()

                self.btnState = True

        openBtn = tk.Button(buttonframe, image=self.navIcon, bg=color["green"], activebackground=color["green"], bd=0, padx=20, command=switch)
        openBtn.place(x=10,y=10)

        closeBtn = tk.Button(self.navRoot, image=self.closeIcon, bg=color["green"], activebackground=color["green"], bd=0, command=switch)
        closeBtn.place(x=240, y=12)

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    settings.init()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.resizable(width=False, height=False)
    root.mainloop()