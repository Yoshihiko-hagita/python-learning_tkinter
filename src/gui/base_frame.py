import tkinter as tk

from src.gui.frames.sidemenu_frame import SideMenuFrame

class BaseFrame(tk.Frame):

    def __init__(self,parent,frame_manager,**kwargs):
        super().__init__(parent,**kwargs)

        self.frame_manager = frame_manager

        self.sidemenu = SideMenuFrame(
            self,
            frame_manager
        )

        self.sidemenu.pack(
            side="left",
            fill="y"
        )