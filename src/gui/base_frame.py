import tkinter as tk

from src.gui.frames.sidemenu_frame import SideMenuFrame


class BaseFrame(tk.Frame):
    def __init__(self, parent, frame_controller, **kwargs):
        super().__init__(parent, **kwargs)

        self.frame_controller = frame_controller

        self.sidemenu = SideMenuFrame(self, frame_controller)

        self.sidemenu.pack(side="left", fill="y")
