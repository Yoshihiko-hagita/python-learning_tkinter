# main.py 完全メモ

# このファイルの役割

このファイルはアプリケーションの起動ファイル。

役割は以下の3つ。

1. root(Tk)の作成
2. 各画面(Frame)の生成
3. 画面切替管理

実際の流れは

```text
main.py 起動
    ↓
App生成
    ↓
LogInFrame生成
MainFrame生成
    ↓
最初はLogInFrame表示
    ↓
ログインボタン押下
    ↓
MainFrame表示
```

---

# インポート

```python
import tkinter as tk
```

Tkinter本体を読み込む。

以降、

```python
tk.Tk
tk.Frame
tk.Label
```

などが使用可能になる。

---

```python
import ctypes
```

Windows APIを呼び出すためのモジュール。

今回はIMEの文字サイズずれ防止に使用している。

---

# DPI設定

```python
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass
```

WindowsのDPIスケーリング問題対策。

---

## DPIとは

Windowsで

```text
125%
150%
200%
```

などの画面拡大率を設定している場合、

TkinterのEntryで日本語入力中に

```text
変換候補の位置がズレる
文字サイズがズレる
```

などの問題が発生することがある。

---

## SetProcessDpiAwareness(1)

Windowsへ

```text
このアプリはDPIを理解しています
```

と通知する。

その結果、

TkinterとIMEのズレが軽減される。

---

## try-exceptにしている理由

MacやLinuxでは

```python
ctypes.windll
```

が存在しない。

そのためエラー回避のために

```python
except Exception:
    pass
```

としている。

---

# 画面クラス読み込み

```python
from src.gui.log_in_frame import LogInFrame
```

ログイン画面クラスを読み込む。

---

```python
from src.gui.main_frame import MainFrame
```

ホーム画面クラスを読み込む。

---

# Appクラス

```python
class App(tk.Tk):
```

Tkを継承したアプリ本体。

---

## 継承イメージ

```text
tk.Tk
  ↑
 App
```

App自身がrootウィンドウになる。

---

# コンストラクタ

```python
def __init__(self):
```

App生成時に自動実行される。

---

```python
super().__init__()
```

Tkを生成する。

実質

```python
root = tk.Tk()
```

と同じ。

---


# ウィンドウサイズ

```python
width = 800
height = 600
```

固定サイズを変数化。

---

# サイズ変更禁止

```python
self.resizable(
    False,
    False
)
```

---

## 第1引数

横方向

```python
False
```

変更不可。

---

## 第2引数

縦方向

```python
False
```

変更不可。

---

結果

```text
□最大化
サイズ変更
```

ができなくなる。

---

# モニターサイズ取得(ウィンドウをPCの中央に配置するため)

```python
screen_width = self.winfo_screenwidth()
```

モニター横幅取得。

例

```text
1920
```

---

```python
screen_height = self.winfo_screenheight()
```

モニター縦幅取得。

例

```text
1080
```

---

# 中央座標計算

```python
x = (screen_width - width) // 2
```

ウィンドウを中央に配置するためのX座標。

例

```text
(1920 - 800) ÷ 2

= 560
```

---

```python
y = (screen_height - height) // 2
```

Y座標計算。

例

```text
(1080 - 600) ÷ 2

= 240
```

---

# ウィンドウ配置

```python
self.geometry(
    f"{width}x{height}+{x}+{y}"
)
```

結果

```python
800x600+560+240
```

のようになる。

意味は

```text
幅 800
高さ 600
X座標 560
Y座標 240
```

つまり

```text
画面中央に表示
```

となる。

---

# rootサイズ追従設定

```python
self.rowconfigure(
    0,
    weight=1
)
```

rootの0行目を伸縮可能にする。

---

```python
self.columnconfigure(
    0,
    weight=1
)
```

rootの0列目を伸縮可能にする。

---

## Excelで考える

```text
      A
   +------+
1  |      |
   +------+
```

A1セルを画面いっぱいに広げる設定。

---

# Frame管理用辞書

```python
self.frames = {}
```

空の辞書作成。

---

目的は

```python
self.frames["LogInFrame"]
```

や

```python
self.frames["MainFrame"]
```

で画面を取り出せるようにすること。

---

# Frame生成ループ

```python
for FrameClass in (
    LogInFrame,
    MainFrame
):
```

順番に

```python
LogInFrame
```

↓

```python
MainFrame
```

を取り出す。

---

## 1周目

```python
FrameClass = LogInFrame
```

---

## 2周目

```python
FrameClass = MainFrame
```

---

# Frame生成

```python
frame = FrameClass(self)
```

1周目

```python
frame = LogInFrame(self)
```

---

2周目

```python
frame = MainFrame(self)
```

になる。

---

# 辞書へ保存

```python
self.frames[FrameClass.__name__] = frame
```

---

## __name__

クラス名取得。

例

```python
LogInFrame.__name__
```

↓

```python
"LogInFrame"
```

---

結果

```python
self.frames["LogInFrame"] = frame
```

になる。

---

2周目は

```python
self.frames["MainFrame"] = frame
```

になる。

---

最終的な辞書

```python
{
    "LogInFrame": LogInFrameオブジェクト,
    "MainFrame": MainFrameオブジェクト
}
```

---

# Frame配置

```python
frame.grid(
    row=0,
    column=0,
    sticky="nsew"
)
```

生成したFrameを配置。

---

## row=0

0行目。

---

## column=0

0列目。

---

つまり全Frameを同じ場所へ配置する。

---

Excelイメージ

```text
      A
   +-------+
1  | Login |
   +-------+
```

さらに

```text
      A
   +-------+
1  | Main  |
   +-------+
```

も同じA1へ配置する。

---

結果

```text
LoginFrame
MainFrame
```

が重なる。

---

## sticky="nsew"

セル全体へ広げる。

---

### n

North

---

### s

South

---

### e

East

---

### w

West

---

意味

```text
上下左右いっぱいに広げる
```

---

# 初期画面表示

```python
self.show_frame(
    "LogInFrame"
)
```

起動直後はログイン画面を表示する。

---

# 画面切替関数

```python
def show_frame(self, name):
```

画面切替専用関数。

---

# Frame取得

```python
frame = self.frames[name]
```

例

```python
self.frames["MainFrame"]
```

取得。

---

# 前面へ表示

```python
frame.tkraise()
```

重なっているFrameの中で一番前へ出す。

---

イメージ

```text
MainFrame
↑
LogInFrame
```

↓

```python
tkraise()
```

↓

```text
LogInFrame
↑
MainFrame
```

---

# タイトル変更

```python
if name == "LogInFrame":
```

ログイン画面表示時。

---

```python
self.title(
    "【備品管理システム】- [ログイン画面]"
)
```

タイトル変更。

---

```python
elif name == "MainFrame":
```

ホーム画面表示時。

---

```python
self.title(
    "【備品管理システム】- [ホーム画面]"
)
```

ホーム画面用タイトルへ変更。

---

# 起動処理

```python
if __name__ == "__main__":
```

このファイルが直接実行された場合のみ実行。

---

# App生成

```python
app = App()
```

Appクラス生成。

ここで

```python
__init__()
```

が実行される。

---

流れ

```text
root作成
↓
Frame生成
↓
Frame配置
↓
ログイン画面表示
```

---

# イベントループ開始

```python
app.mainloop()
```

Tkinter開始。

---

これが無いと

```text
画面表示
ボタンクリック
キーボード入力
画面更新
```

が動かない。

---

# 全体構成図

```text
App(Tk)
│
├─ LogInFrame
│      ↓
│   ログイン画面
│
└─ MainFrame
       ↓
    ホーム画面
```

両方とも

```text
row=0
column=0
```

へ重ねて配置。

切替時は

```python
show_frame()
    ↓
tkraise()
```

によって前面表示を切り替えている。