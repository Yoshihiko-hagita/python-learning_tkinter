# side_frame.py 説明メモ

## このファイルの役割

`SideFrame` はログイン後の画面で表示する「左側のメニュー」を作るためのクラス。

イメージ

```text
+---------------------------------------------------+
| 備品管理システム                                  |
+-----------------+---------------------------------+
| ホーム          |                                 |
| 備品一覧        |                                 |
| 備品登録        |         メイン画面              |
| 貸出            |                                 |
| 返却            |                                 |
| 履歴            |                                 |
| ユーザー管理    |                                 |
+-----------------+---------------------------------+
```

左側のメニュー部分だけを担当する。

---

# コード全体

```python
import tkinter as tk
from tkinter import ttk

class SideFrame(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=180,
            bg="#E8E8E8"
        )

        self.pack_propagate(False)

        menu_list = [
            ("ホーム", "HomeFrame"),
            ("備品一覧", "ItemListFrame"),
            ("備品登録", "ItemRegisterFrame"),
            ("貸出", "RentalFrame"),
            ("返却", "ReturnFrame"),
            ("履歴", "HistoryFrame"),
            ("ユーザー管理", "UserManageFrame")
        ]

        for text, frame_name in menu_list:

            btn = ttk.Button(
                self,
                text=text,
                command=lambda n=frame_name:
                    parent.show_content(n)
            )

            btn.pack(
                fill="x",
                padx=5,
                pady=2
            )
```

---

# import

```python
import tkinter as tk
from tkinter import ttk
```

## 何をしているか

Tkinterを使用するための読み込み。

---

```python
import tkinter as tk
```

Tkinter本体を使用できるようにする。

例

```python
tk.Frame
tk.Label
tk.Entry
```

など。

---

```python
from tkinter import ttk
```

ttkテーマ付きウィジェットを使用する。

例

```python
ttk.Button
ttk.Entry
ttk.Combobox
```

など。

見た目がWindows標準に近くなる。

---

# クラス定義

```python
class SideFrame(tk.Frame):
```

## 何をしているか

Frameを継承して新しい部品を作る。

つまり

```python
SideFrame
```

は

```python
Frameの機能
+
サイドメニュー機能
```

を持つ独自ウィジェットになる。

---

# コンストラクタ

```python
def __init__(self, parent):
```

## parentとは

このFrameを配置する親ウィジェット。

今回は

```python
MainFrame
```

になる予定。

イメージ

```text
MainFrame
 ├─ SideFrame
 └─ ContentFrame
```

---

# 親クラス初期化

```python
super().__init__(
    parent,
    width=180,
    bg="#E8E8E8"
)
```

## 何をしているか

Frameを作成している。

---

### parent

```python
parent
```

親を指定。

つまり

```text
MainFrame の中に SideFrame を作る
```

という意味。

---

### width=180

```python
width=180
```

サイドバーの幅を180pxに設定。

---

### bg

```python
bg="#E8E8E8"
```

背景色。

少し薄いグレー。

---

# pack_propagate(False)

```python
self.pack_propagate(False)
```

## 非常に重要

Tkinterはデフォルトで

```python
pack_propagate(True)
```

になっている。

---

その場合

```text
Frame
 └─ Button
```

なら、

FrameのサイズはButtonに合わせて小さくなる。

---

例えば

```python
width=180
```

を指定しても、

Buttonが100pxなら、

Frameも100px程度になる。

---

そこで

```python
self.pack_propagate(False)
```

を書く。

---

意味

```text
子ウィジェットのサイズに合わせるな
指定した幅(height)を優先しろ
```

---

結果

```python
width=180
```

が有効になる。

---

# メニュー一覧

```python
menu_list = [
    ("ホーム", "HomeFrame"),
    ("備品一覧", "ItemListFrame"),
    ("備品登録", "ItemRegisterFrame"),
    ("貸出", "RentalFrame"),
    ("返却", "ReturnFrame"),
    ("履歴", "HistoryFrame"),
    ("ユーザー管理", "UserManageFrame")
]
```

## 何をしているか

表示するメニューを管理している。

形式

```python
(
    ボタンの表示名,
    遷移先Frame名
)
```

---

例

```python
("ホーム", "HomeFrame")
```

意味

```text
表示名 → ホーム

押した時
↓
HomeFrameへ切り替える
```

---

# for文

```python
for text, frame_name in menu_list:
```

## 何をしているか

menu_listを1件ずつ取り出す。

---

1回目

```python
text = "ホーム"
frame_name = "HomeFrame"
```

---

2回目

```python
text = "備品一覧"
frame_name = "ItemListFrame"
```

---

3回目

```python
text = "備品登録"
frame_name = "ItemRegisterFrame"
```

---

というように順番に取り出す。

---

# ボタン作成

```python
btn = ttk.Button(
    self,
    text=text,
    command=lambda n=frame_name:
        parent.show_content(n)
)
```

## self

```python
self
```

つまり

```python
SideFrame
```

の中にボタンを作る。

---

## text=text

例えば

```python
text="ホーム"
```

になる。

結果

```text
ホーム
```

というボタンが表示される。

---

# command

```python
command=
```

は

```text
ボタンが押された時に実行する処理
```

を指定する。

---

# lambda

```python
lambda n=frame_name:
    parent.show_content(n)
```

## 何をしているか

ボタンが押された時に

```python
parent.show_content(n)
```

を実行する。

---

例えば

```python
frame_name = "HomeFrame"
```

なら

実質

```python
parent.show_content(
    "HomeFrame"
)
```

になる。

---

結果

```text
ホームボタン
↓
クリック
↓
HomeFrame表示
```

となる。

---

# なぜ lambda が必要なのか

次はNG。

```python
command=parent.show_content(frame_name)
```

これは

```text
ボタン生成時に即実行
```

されてしまう。

---

欲しいのは

```text
押された時に実行
```

なので

```python
lambda
```

を使う。

---

# n=frame_name の意味

これも重要。

もし

```python
lambda:
    parent.show_content(frame_name)
```

だと、

for文終了後の値しか参照しない。

---

結果

```text
どのボタンを押しても
UserManageFrame
```

になる。

---

そのため

```python
lambda n=frame_name:
```

と書いて、

その時点の値を保存している。

---

# pack

```python
btn.pack(
    fill="x",
    padx=5,
    pady=2
)
```

ボタンを配置している。

---

## fill="x"

```python
fill="x"
```

横方向いっぱいに広げる。

---

イメージ

```text
┌─────────────┐
│ ホーム      │
└─────────────┘
```

---

## padx=5

左右に5px余白を付ける。

---

## pady=2

上下に2px余白を付ける。

---

# 実際の動作

for文で以下のボタンが自動作成される。

```text
ホーム
備品一覧
備品登録
貸出
返却
履歴
ユーザー管理
```

---

ボタンをクリックすると

```python
parent.show_content(
    フレーム名
)
```

が呼ばれる。

---

例

```text
ホーム
↓
show_content("HomeFrame")

備品一覧
↓
show_content("ItemListFrame")

履歴
↓
show_content("HistoryFrame")
```

となり、右側の画面を切り替える。

---

# 今後追加するとき

例えば「棚卸」を追加したい場合。

```python
menu_list = [
    ("ホーム", "HomeFrame"),
    ("備品一覧", "ItemListFrame"),
    ("棚卸", "InventoryFrame")
]
```

を追加するだけでボタンが自動生成される。

for文を書き換える必要はない。

これがmenu_list方式のメリット。