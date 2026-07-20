# uv

## uvとは

uvはPythonの

- 仮想環境管理
- パッケージ管理
- 依存関係管理

を行うためのツール。

Rust製で非常に高速に動作する。

---

## なぜuvが必要なのか

Python開発ではプロジェクトごとに使用するライブラリが異なる。

例えば、

プロジェクトA

```text
pandas 2.0
```

プロジェクトB

```text
pandas 3.0
```

を利用したい場合がある。

---

もし仮想環境を使わないと、

```text
PC全体で1つの環境
```

になるため、

あるプロジェクトの変更が
別プロジェクトへ影響してしまう。

---

そこで、

```text
プロジェクトごとに独立した環境
```

を作るためにuvを利用する。

---

## uvでできること

### ① 仮想環境作成

例

```powershell
uv venv
```

---

### ② ライブラリ管理

例

```powershell
uv add pandas
```

---

### ③ 依存関係管理

例

```powershell
uv lock
```

---

### ④ 環境再現

例

```powershell
uv sync
```

---

## uvとvenvの違い

### venv

仮想環境のみ作成

```powershell
py -3.13 -m venv .venv
```

---

### uv

仮想環境

+

ライブラリ管理

+

依存関係管理

を行える

---

## イメージ

### venv

```text
仮想環境
```

---

### uv

```text
仮想環境
+
パッケージ管理
+
依存関係管理
```

---

そのため現在は

```text
uv推奨
```

となっている。

---

# uv運用の流れ

GitとGitHubの設定が完了したら、
uvでPython環境を構築する。

---

# ① uv初期化

```powershell
uv init
```

---

## 何をしているのか

Pythonプロジェクトとして初期化している。

---

## 実行するとどうなるか

以下のようなファイルが作成される。

```text
pyproject.toml
```

---

## pyproject.tomlとは

プロジェクト情報を管理するファイル。

例

```toml
[project]
name = "python-learning_tkinter"
version = "0.1.0"
requires-python = ">=3.13"
```

---

## 何ができるようになるのか

プロジェクト設定を管理できる。

---

## 実務でどう使うか

プロジェクト名

Pythonバージョン

依存ライブラリ

を管理する。

---

# ② 仮想環境作成

```powershell
uv venv
```

---

## 何をしているのか

そのプロジェクト専用のPython環境を作成している。

---

## 実行するとどうなるか

以下が作成される。

```text
.venv
```

---

## .venvとは

プロジェクト専用のPython環境。

---

## イメージ

```text
python-learning_tkinter
│
├─ .venv
├─ src
├─ docs
└─ pyproject.toml
```

---

## なぜ必要か

他のプロジェクトと環境を分離するため。

---

## 実務でどう使うか

プロジェクトごとに作成する。

---

# ③ 仮想環境有効化

```powershell
.venv\Scripts\activate
```

---

## 何をしているのか

現在のターミナルで

```text
このプロジェクト専用Python
```

を使用するように切り替えている。

---

## 実行後

```powershell
(.venv) PS C:\Work\python-learning_tkinter>
```

のように表示される。

---

## 何ができるようになるのか

以降のライブラリ操作が

```text
このプロジェクトだけ
```

へ適用される。

---

# 仮想環境終了

```powershell
deactivate
```

---

## 何をしているのか

仮想環境を終了する。

---

# ④ ライブラリ追加

例

```powershell
uv add pandas
```

---

## 何をしているのか

ライブラリをインストールしている。

---

## uv pip installとの違い

### uv pip install

```powershell
uv pip install pandas
```

インストールのみ

---

### uv add

```powershell
uv add pandas
```

インストール

+

pyproject.toml更新

+

uv.lock更新

---

## 実務ではどちら？

基本的に

```powershell
uv add
```

を使用する。

---

# ⑤ 依存関係確認

```powershell
uv tree
```

---

## 何をしているのか

ライブラリ同士の依存関係を表示している。

---

## 例

```text
pandas
├─ numpy
├─ python-dateutil
│  └─ six
└─ tzdata
```

---

## なぜ重要なのか

ライブラリが何を利用しているか分かる。

---

# ⑥ lockファイル生成

```powershell
uv lock
```

---

## 何をしているのか

現在のライブラリ構成を固定している。

---

## 実行するとどうなるか

```text
uv.lock
```

が作成される。

---

## なぜ必要か

チーム全員で同じ環境を使うため。

---

# ⑦ 環境再現

```powershell
uv sync
```

---

## 何をしているのか

pyproject.toml

+

uv.lock

を元に環境を再構築している。

---

## 実務でどう使うか

GitHubから取得後、

```powershell
uv sync
```

するだけで同じ環境を作成できる。

---

# 現在の推奨運用

ライブラリ追加

```powershell
uv add ライブラリ名
```

例

```powershell
uv add pandas
```

---

依存関係確認

```powershell
uv tree
```

---

環境再現

```powershell
uv sync
```

---

# よく使うコマンド一覧

## 初期化

```powershell
uv init
```

---

## 仮想環境作成

```powershell
uv venv
```

---

## 仮想環境有効化

```powershell
.venv\Scripts\activate
```

---

## 仮想環境終了

```powershell
deactivate
```

---

## ライブラリ追加

```powershell
uv add pandas
```

---

## 依存関係確認

```powershell
uv tree
```

---

## lock更新

```powershell
uv lock
```

---

## 環境再現

```powershell
uv sync
```

---

# Git・GitHub・uv の関係

## Git

履歴管理

---

## GitHub

クラウド管理

---

## uv

Python環境管理

---

## イメージ

```text
プロジェクト作成
↓
Git
↓
GitHub
↓
uv
↓
開発開始
```

---

# ここまででできること

✅ Pythonプロジェクト初期化

✅ 仮想環境作成

✅ 仮想環境有効化

✅ ライブラリ追加

✅ 依存関係管理

✅ 環境再現

✅ チーム開発対応

---

# 次は tkinter へ

Git

↓

GitHub

↓

uv

まで完了した。

次は

tkinterを使って画面を作成する。