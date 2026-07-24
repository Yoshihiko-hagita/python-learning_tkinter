import tkinter as tk

from src.gui.frams.side_frame import SideFrame

class MainFrame(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            bg="white"
        )

        self.side_frame = SideFrame(self)

        self.side_frame.pack(
            side="left",
            fill="y"
        )

