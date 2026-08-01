import tkinter as tk
import ctypes # 日本語入力時のIMEの文字サイズずれ防止


# ==================================
# 日本語入力時のIMEの文字サイズずれ防止
# ==================================
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

from src.gui.frame_management import FrameManager

# ==================================
# Appクラス
# ==================================

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.init_window()
        self.frame_manager = FrameManager(self)
        self.frame_manager.init_frames(self)
        self.frame_manager.show_frame("LogInFrame")




    # ==================================
    # ウィンドウ初期化
    # ==================================
    def init_window(self):
        width = 800
        height = 600

        # ウィンドウサイズ変更不可
        self.resizable(False,False)

        # 画面を中央に配置するための座標を取得
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # 画面を中央に配置するためのX座標とY座標を計算
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # ウィンドウサイズ&画面を中央に配置
        self.geometry( f"{width}x{height}+{x}+{y}")

        # Excelで例えるとA1セルを画面いっぱいに広げる
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

# ==================================
# 起動
# ==================================

if __name__ == "__main__":

    app = App()

    app.mainloop()