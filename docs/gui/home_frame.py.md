# HomeFrame 作成メモ

## この画面の構成

```text
HomeFrame
│
├─ SideFrame（左メニュー）
│
└─ home_contents_frame（メインコンテンツ）
    │
    ├─ rental_frame（現在貸出中の備品）
    │   └─ Treeview
    │
    ├─ notice_frame（お知らせ）
    │   └─ Listbox
    │
    └─ version_label（バージョン表示）
```

---

# import

```python
import tkinter as tk
from tkinter import ttk
from src.gui.frams.side_frame import SideFrame
```

## import tkinter as tk

Tkinter本体を読み込む。

使用例

```python
tk.Frame
tk.Label
tk.Button
tk.Listbox
```

など。

---

## from tkinter import ttk

Tkinterのデザイン強化版を読み込む。

使用例

```python
ttk.Button
ttk.Treeview
ttk.LabelFrame
```

見た目がWindows標準に近くなる。

---

## from src.gui.frams.side_frame import SideFrame

自作したサイドメニューを読み込んでいる。

---

# HomeFrameクラス

```python
class HomeFrame(tk.Frame):
```

Home画面を表すクラス。

Frameを継承しているため、

```python
HomeFrame
```

自体が画面部品になる。

---

# super()

```python
super().__init__(
    parent,
    bg="white"
)
```

親クラス(Frame)を初期化する。

### parent

このフレームの親。

例

```python
HomeFrame(root)
```

なら

```python
root
```

が親になる。

---

### bg

背景色。

```python
bg="white"
```

↓

```text
背景が白色
```

---

# SideFrame生成

```python
self.side_frame = SideFrame(self)
```

左メニュー作成。

親は

```python
self
```

つまり

```python
HomeFrame
```

になる。

---

# SideFrame配置

```python
self.side_frame.pack(
    side="left",
    fill="y"
)
```

## side="left"

左側へ配置。

```text
┌─────────────┐
│Side│        │
│Menu│        │
└─────────────┘
```

---

## fill="y"

縦方向に伸ばす。

```text
高さいっぱいになる
```

---

# メインコンテンツ領域

```python
home_contents_frame = tk.Frame(
    self,
    bg="#FFFFFF"
)
```

右側のコンテンツ領域を作成。

ここに

- 貸出中一覧
- お知らせ
- バージョン

を配置する。

---

# メインコンテンツ配置

```python
home_contents_frame.pack(
    side="right",
    fill="both",
    expand=True
)
```

## side="right"

右へ配置。

---

## fill="both"

横・縦両方へ伸ばす。

---

## expand=True

余った領域を使用する。

これが無いと

```python
Frame
```

が広がらない。

---

# 現在貸出中の備品

```python
rental_frame = ttk.LabelFrame(
    home_contents_frame,
    text="現在貸出中の備品"
)
```

枠付きグループを生成。

表示

```text
┌ 現在貸出中の備品 ──────┐
│                        │
└────────────────────────┘
```

---

# rental_frame配置

```python
rental_frame.pack(
    fill="both"
)
```

フレームを広げる。

---

# Treeview

```python
self.tree = ttk.Treeview(...)
```

表を作成する。

表示例

```text
ID        名称       品番
--------------------------------
EQ-A001   PC        XXXX
EQ-A002   マウス     YYYY
```

---

# columns

```python
columns = (
    "id",
    "name",
    "model",
    "qty",
    "return_date"
)
```

データ列定義。

---

# heading()

```python
self.tree.heading(
    "id",
    text="ID"
)
```

列タイトルを設定。

表示

```text
ID
```

---

# column()

```python
self.tree.column(
    "id",
    width=100
)
```

列サイズを設定。

---

## width

列幅

```python
width=100
```

↓

```text
100px
```

---

## anchor

文字位置

```python
anchor="center"
```

中央揃え。

---

# Treeview配置

```python
self.tree.pack(
    fill="both",
    expand=True,
    ipady=100
)
```

---

## ipady

内部余白。

大きくすると高さが増える。

---

# Treeviewへデータ追加

```python
self.tree.insert(
    "",
    "end",
    values=("EQ-A001", "PC")
)
```

行を追加する。

結果

```text
EQ-A001 PC
```

が表示される。

---

# お知らせ枠

```python
notice_frame = ttk.LabelFrame(
    home_contents_frame,
    text="お知らせ"
)
```

表示

```text
┌ お知らせ ─────┐
│               │
└───────────────┘
```

---

# notice_frame配置

```python
notice_frame.pack(
    fill="both",
    expand=True
)
```

余った領域まで広げる。

---

# Listbox

```python
notice_list = tk.Listbox(...)
```

一覧表示用。

表示例

```text
返却期限が近い備品があります
新しいVerがリリースされました
最新版をダウンロードしてください
```

---

# Listbox配置

```python
notice_list.pack(
    fill="both",
    ipady=30
)
```

---

# Listboxへデータ追加

```python
notice_list.insert(
    tk.END,
    "新しいVerがリリースされました"
)
```

末尾へ追加する。

---

# バージョン表示

```python
version_label = tk.Label(
    home_contents_frame,
    text="Ver 1.0.0"
)
```

ラベル生成。

表示

```text
Ver 1.0.0
```

---

# バージョン位置固定

```python
version_label.place(
    relx=1.0,
    rely=1.0,
    anchor="se"
)
```

## relx

親横幅の割合。

```python
0.0
```

左

```python
0.5
```

中央

```python
1.0
```

右

---

## rely

親高さの割合。

```python
0.0
```

上

```python
1.0
```

下

---

## anchor

基準位置。

```python
"se"
```

右下。

結果

```text
画面右下固定
```

---

# よく使う pack()

## 説明

部品を順番に配置する。

---

### side

配置方向

```python
side="top"
```

上

```python
side="bottom"
```

下

```python
side="left"
```

左

```python
side="right"
```

右

---

### fill

伸ばす方向

```python
fill="x"
```

横

```python
fill="y"
```

縦

```python
fill="both"
```

両方

---

### expand

余った領域を使う

```python
expand=True
```

大きくなる

```python
expand=False
```

必要サイズのみ

---

### padx

左右余白

```python
padx=10
```

左右10px

---

### pady

上下余白

```python
pady=10
```

上下10px

---

# よく使う place()

## 説明

絶対位置または割合位置へ配置。

---

### x

左からの距離

```python
x=100
```

左から100px

---

### y

上からの距離

```python
y=50
```

上から50px

---

### relx

横の割合

```python
0.0 ～ 1.0
```

---

### rely

縦の割合

```python
0.0 ～ 1.0
```

---

### anchor

基準点

```python
nw
```

左上

```python
center
```

中央

```python
se
```

右下

---

# よく使う Label

```python
tk.Label
```

文字表示用。

主なパラメータ

```python
text
```

表示文字

```python
font
```

フォント

```python
bg
```

背景色

```python
fg
```

文字色

---

# よく使う Frame

```python
tk.Frame
```

部品をまとめる箱。

主なパラメータ

```python
bg
```

背景色

```python
width
```

幅

```python
height
```

高さ

---

# よく使う Button

```python
ttk.Button
```

押せるボタン。

主なパラメータ

```python
text
```

表示文字

```python
command
```

押した時に実行する関数

例

```python
command=self.login
```

---

# よく使う Treeview

```python
ttk.Treeview
```

一覧表。

主なメソッド

```python
heading()
```

見出し設定

```python
column()
```

列設定

```python
insert()
```

行追加

```python
selection()
```

選択行取得

```python
delete()
```

行削除

---

# 学習時の考え方

画面は基本的に

```text
Frame
 ├ Label
 ├ Button
 ├ Entry
 ├ Treeview
 └ Listbox
```

の組み合わせで作る。

まずFrameで領域を分割し、その中へ必要な部品を配置すると管理しやすい。
``