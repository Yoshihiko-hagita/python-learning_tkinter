import os

from dotenv import load_dotenv

load_dotenv()

# =========================
# アプリ設定
# =========================
APP_TITLE = "【備品管理システム】"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# =========================
# 環境変数
# =========================
PASSWORD_HASH_ROUNDS = int(os.getenv("PASSWORD_HASH_ROUNDS", "12"))


# =========================
# 権限
# =========================
AUTHORITY_MAP = {
    "管理者": "ADMIN",
    "一般": "USER",
}

AUTHORITY_REVERSE_MAP = {
    v: k for k, v in AUTHORITY_MAP.items()
}
