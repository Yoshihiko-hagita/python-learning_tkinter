
from src.gui.frames.log_in_frame import LogInFrame
from src.gui.frames.home_frame import HomeFrame
from src.gui.frames.user_management_frame import UserManagementFrame
from src.gui.frames.user_form_frame import UserFormFrame

class FrameManager:
    def __init__(self, parent):
        self.parent = parent

    def init_frames(self, parent):
        self.frames = {}

        for FrameClass in (
            LogInFrame,
            HomeFrame,
            UserManagementFrame,
            UserFormFrame
        ):
            frame = FrameClass(parent, self)

            self.frames[FrameClass.__name__] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

            self.show_frame("LogInFrame")

    # =========================
    # 画面切替
    # =========================
    def show_frame(self, name,**kwargs):

        frame = self.frames[name]

        frame.tkraise()
        
        mode = kwargs.get("mode")
        user = kwargs.get("user")
        
        frame.mode = mode

        # タイトル変更
        if name == "LogInFrame":

            self.parent.title(
                "【備品管理システム】- [ログイン画面]"
            )

        elif name == "HomeFrame":

            self.parent.title(
                "【備品管理システム】- [ホーム画面]"
            )
        elif name == "UserManagementFrame":

            self.parent.title(
                "【備品管理システム】- [ユーザー管理画面]"
            )

        elif mode == "New":
            self.parent.title(
                "【備品管理システム】- [ユーザー新規登録画面]"
            )
            frame.user_form_frame.config(
                text="ユーザー新規登録"
            )
        elif mode == "Edit":
            self.parent.title(
                "【備品管理システム】- [ユーザー編集画面]"
            )
            frame.user_form_frame.config(
                text="ユーザー編集"
            )
            frame.set_user_info(user)
