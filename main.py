import tkinter as tk
import ctypes # 日本語入力時のIMEの文字サイズずれ防止


# ==================================
# 日本語入力時のIMEの文字サイズずれ防止
# ==================================
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


from src.gui.frames.log_in_frame import LogInFrame
from src.gui.frames.contents.home_frame import HomeFrame
from src.gui.frames.contents.user_management_frame import UserManagementFrame
from src.gui.frames.contents.user_register_frame import UserRegisterFrame


# ==================================
# Appクラス
# ==================================

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        # =========================
        # root設定
        # =========================

        width = 800
        height = 600

        self.resizable(
            False,
            False
        )


        # 画面サイズ取得
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


        # 中央座標計算
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2


        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )


        # rootサイズ追従
        self.rowconfigure(
            0,
            weight=1
        )

        self.columnconfigure(
            0,
            weight=1
        )


        # =========================
        # Frame作成
        # =========================

        self.frames = {}


        for FrameClass in (
            LogInFrame,
            HomeFrame,
            UserManagementFrame,
            UserRegisterFrame
        ):

            frame = FrameClass(self)

            self.frames[FrameClass.__name__] = frame


            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
            )


        # 最初はログイン画面
        self.show_frame(
            "UserManagementFrame"
        )


    # =========================
    # 画面切替
    # =========================

    def show_frame(self, name, **kwargs):

        frame = self.frames[name]

        if hasattr(frame, "on_show"):
            frame.on_show(**kwargs)

        frame.tkraise()


        # タイトル変更

        if name == "LogInFrame":

            self.title(
                "【備品管理システム】- [ログイン画面]"
            )

        elif name == "HomeFrame":

            self.title(
                "【備品管理システム】- [ホーム画面]"
            )
        elif name == "UserManagementFrame":

            self.title(
                "【備品管理システム】- [ユーザー管理画面]"
            )
        elif name == "UserRegisterFrame":

            self.title(
                "【備品管理システム】- [ユーザー新規登録画面]"
            )
            





# ==================================
# 起動
# ==================================

if __name__ == "__main__":

    app = App()

    app.mainloop()