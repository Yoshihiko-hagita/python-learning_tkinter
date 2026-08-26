from src.config.settings import APP_TITLE
from src.gui.frames.equipment_list_frame import EquipmentListFrame
from src.gui.frames.equipment_registration_frame import EquipmentRegistrationFrame
from src.gui.frames.home_frame import HomeFrame
from src.gui.frames.log_in_frame import LogInFrame
from src.gui.frames.user_form_frame import UserFormFrame
from src.gui.frames.user_management_frame import UserManagementFrame
from src.gui.frames.lending_frame import LendingFrame

# =========================
# 画面コントロール
# =========================
class FrameController:
    def __init__(self, parent):
        self.parent = parent

    # =========================
    # 画面初期化
    # =========================
    def init_frames(self, parent):
        self.frames = {}

        for FrameClass in (
            LogInFrame,
            HomeFrame,
            EquipmentListFrame,
            EquipmentRegistrationFrame,
            LendingFrame,
            UserManagementFrame,
            UserFormFrame,
        ):
            frame = FrameClass(parent, self)

            self.frames[FrameClass.__name__] = frame

            frame.grid(row=0, column=0, sticky="nsew")

    # =========================
    # 画面切替
    # =========================
    def show_frame(self, name, **kwargs):

        frame = self.frames[name]

        frame.tkraise()

        mode = kwargs.get("mode")
        user = kwargs.get("user")
        equipment = kwargs.get("equipment")

        frame.mode = mode

        if name == "LogInFrame":
            self.parent.title(f"{APP_TITLE} - [ログイン画面]")

        elif name == "HomeFrame":
            self.parent.title(f"{APP_TITLE} - [ホーム画面]")

        elif name == "EquipmentListFrame":
            self.parent.title(f"{APP_TITLE} - [備品一覧画面]")
            frame.load_equipment_list()

        elif name == "EquipmentRegistrationFrame":
            self.parent.title(f"{APP_TITLE} - [備品登録画面]")

        elif name == "LendingFrame":
            self.parent.title(f"{APP_TITLE} - [貸出画面]")
            frame.set_equipment_info(equipment)
            
        elif name == "UserManagementFrame":
            self.parent.title(f"{APP_TITLE} - [ユーザー管理画面]")
            frame.search_user()

        elif mode == "New":
            self.parent.title(f"{APP_TITLE} - [ユーザー新規登録画面]")
            frame.user_form_frame.config(text="ユーザー新規登録")
            frame.entry_id.config(state="normal")
            frame.clear_form()
            frame.show_password_var.set(False)
            frame.toggle_password()
            frame.button_cancel.config(state="!disabled")

        elif mode == "Edit":
            self.parent.title(f"{APP_TITLE} - [ユーザー編集画面]")
            frame.user_form_frame.config(text="ユーザー編集")
            frame.clear_form()
            frame.set_user_info(user)
            frame.entry_id.config(state="readonly")
            frame.show_password_var.set(False)
            frame.toggle_password()
            frame.button_cancel.config(state="disabled")
