from abc import ABC
import tkinter as tk
from MainWindow import MainWindow


class ExportIPWindow(MainWindow, ABC):

    def setMainWindow(self):
        super().setMainWindow()
        # Aca agregamos las cosas extra que hace
        # Setlabels
        # SetWidgets
        # etc...
