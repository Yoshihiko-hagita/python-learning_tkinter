# log_in_frame.py 完全メモ

## このクラスの役割

```python
class LogInFrame(tk.Frame):
```

ログイン画面を作るためのFrameクラス。

Appクラスから生成され、

```python
LogInFrame(self)
```

として呼ばれる。

画面切替時には

```python
app.show_frame("LogInFrame")
```

で表示される。

---

# インポート

```python
import tkinter as tk
from tkinter import ttk
```

## import tkinter as tk

Tkinter本体を読み込む。

以降、

```python
tk.Frame
tk.Label
tk.Entry
```

などが使用可能になる。

---

## from tkinter import ttk

ttkウィジェットを使用する。

ttkは見た目が新しい部品群。

今回使用しているのは

```python
ttk.Entry
ttk.Button
```

である。

---

# クラス定義

```python
class LogInFrame(tk.Frame):
```

Frameを継承している。

つまりこのクラス自身が画面の土台になる。

---

# コンストラクタ

```python
def __init__(self, parent):
```

Frame生成時に自動実行される。

---

```python
super().__init__(parent, bg="#C5C3C3")
```

親ウィジェットに配置されるFrameを作成。

実際には

```python
tk.Frame(parent)
```

を呼んでいる。

背景色は

```python
#C5C3C3
```

のグレー。

---

# 入力エリア作成

```python
input_frame = tk.Frame(
    self,
    bg="#C5C3C3",
    pady=10
)
```

ログイン部品をまとめて配置するためのFrame。

Parentは

```python
self
```

つまりLogInFrame。

---

## pady=10

上下に余白を付ける。

---

# 入力エリア配置

```python
input_frame.place(
    relx=0.30,
    rely=0.30
)
```

place()を使用して座標配置する。

---

## relx=0.30

横方向30%位置。

---

## rely=0.30

縦方向30%位置。

---

イメージ

```text
+---------------------------+
|                           |
|                           |
|      input_frame          |
|         (30%)             |
|                           |
+---------------------------+
```

---

# 説明ラベル

```python
label_placeholder = tk.Label(
    input_frame,
    text="※ 英数字とハイフン(-)のみ入力可能です",
    font=("Meiryo UI", 8),
    fg="red",
    bg="#C5C3C3"
)
```

入力ルール説明用ラベル。

---

## text

表示文字列。

---

## font

フォント設定。

```python
("Meiryo UI", 8)
```

↓

```text
フォント名：Meiryo UI
サイズ：8
```

---

## fg

文字色。

```python
red
```

---

## bg

背景色。

---

# ラベル配置

```python
label_placeholder.grid(
    row=0,
    column=1
)
```

grid配置。

位置は

```text
0行1列
```

---

# 社員IDラベル

```python
label_id = tk.Label(
    input_frame,
    text="社員ID",
    font=("Meiryo UI", 10),
    bg="#C5C3C3"
)
```

社員ID入力欄のタイトル。

---

# 社員IDラベル配置

```python
label_id.grid(
    row=1,
    column=0,
    padx=(0,11)
)
```

位置

```text
1行0列
```

---

## padx=(0,11)

左右余白。

```text
左 0px
右11px
```

---

# 社員ID入力欄

## validatecommand登録

```python
vcmd_id = (
    self.register(self.validate_employee_no),
    "%P"
)
```

入力チェック関数をTkinterへ登録。

---

## register()

通常のPython関数を

Tkinterから呼べる関数へ変換する。

---

## "%P"

変更後の文字列。

例えば

```text
ABC
```

入力後なら

```python
new_value = "ABC"
```

として渡される。

---

# Entry作成

```python
self.entry_id = ttk.Entry(
    input_frame,
    font=("Meiryo UI",12),
    width=20,
    validate="key",
    validatecommand=vcmd_id
)
```

社員ID入力欄を作成。

---

## width=20

20文字程度の幅。

---

## validate="key"

キー入力ごとに検証する。

つまり1文字入力のたびに

```python
validate_employee_no()
```

が実行される。

---

## validatecommand

実行する検証関数。

---

# Entry配置

```python
self.entry_id.grid(
    row=1,
    column=1,
    padx=(5,0)
)
```

位置

```text
1行1列
```

---

# カーソル設定

```python
self.entry_id.focus_set()
```

画面表示時にカーソルを置く。

起動直後から入力可能になる。

---

# パスワードラベル

```python
label_password = tk.Label(
    input_frame,
    text="パスワード",
    font=("Meiryo UI",10),
    bg="#C5C3C3"
)
```

パスワード入力欄のタイトル。

---

# パスワードラベル配置

```python
label_password.grid(
    row=2,
    column=0,
    pady=(15,0)
)
```

位置

```text
2行0列
```

---

## pady=(15,0)

上に15px余白。

---

# パスワード入力チェック登録

```python
vcmd_password = (
    self.register(self.validate_password_no),
    "%P"
)
```

パスワード入力用の検証関数登録。

---

# パスワード入力欄

```python
self.entry_password = ttk.Entry(
    input_frame,
    show="*",
   *font=("Meiryo UI",12),
    width=2*,
    validate="key",
    validate*ommand=vcmd_password
)
```

パスワ*ド入力欄。

---

## show*"*"

入力内容を隠す*

例

```text
abcdef
```

↓

```tex*
******
```

---

# パスワード配置*
```python
self.entry_password.gri*(
    row=*,
*   column=1,
    padx=(5,0),
    p*dy=(15*0)
)
```

位置

```text
2行1列
```

--*

# ログインボタン

```python
*utton*login = ttk.Button(
    input_fram*,
*  *text="ログイン",
    command=self.logi*
)
```

ログインボタン生成。

---

## comman*=self.login

押されたら

```python
self*login()
```

を実行する。

---

# ボタン*置

*``python
button_login.grid(
    ro*=3,
    column=0,
    columnspan=2*
    pady=(30,10*
)
```

位置

```text
3行*
```

---

## column*pan*2

2列分使う。

つまり

```*ext
+-----+-----+
|    *ボタン |
+*----+-----+
*`*

ではなく

```text
+-----------+
*   ボタン   |
+-----------+
```

となる*

---

#*社員ID入力チェック

```python
*ef*validate_employee_no(self, new_val*e):
```

入力されるたびに呼ばれる。

---

## 空*字許可

```python
if new_value == "":*    return True*```

削除中でも入力可能にする。

---

*# 桁数制限

```python
if len*new*value) > 8:
    return False
```

*文字超え禁止。

---

## 文字チェック

```python*for*c in new_value:
```

1文字ずつ確認。

---*
```python
c.isascii()
```

ASCII*字か確認*

日本語はNG*

*--

```python
**isalnum()
```

英数字か確認。

---

```py*hon
c == "-"
```

ハイフン許可。

---

つま*許可されるのは

```text
A-Z
a*z
0-9
-
```

のみ。

---

# パスワード入力チェ*ク

```python
def*validate*password_no(self,*new_value):
```

ほぼ社員IDと同じ。

違いは桁数*限が無い。

---

# ログイン処理

```python
de* login(self):
```

ログインボタン押下時に実行。
*---

```python
app = self.master
`*`

親を取得。

今回の親は

```python
App
```*
オブジェクト。

---

```python
app.show_*rame(
    "MainFrame"
)
```

Appク*スの

```python
show_frame()
```

を呼*出す。

---

結果

```python
self.frame*["MainFrame"]
``*

が取得される。

---

*らに

```python
frame.tkraise()
```
*が実行される。

*--

結果

*``text
ログイン画面
↓
ホーム画面
*`*

へ*り*わる。

---

# 画面レイアウト図

```text
inpu*_frame

┌──────────────────┐
│ ※入力*能文字*  *│
├──────┬───────────┤
*社員ID│ Entry     *│
*──────┼───────────┤
│PW   *│ ******     │
├──────*────────*──┤
│     ログイン     *│
└──────────────────┘
``*

このinput_frame全*が

```*ython
place(relx=0.30, rely=0**0)
```

でLogInFrame上へ配置*れている。