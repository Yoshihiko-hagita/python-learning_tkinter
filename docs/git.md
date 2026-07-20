# Git

## Gitとは

Gitはソースコードやファイルの変更履歴を管理するためのバージョン管理システム。

例えば、

- 昨日まで動いていたコードに戻したい
- どのファイルを変更したか確認したい
- 間違ってファイルを消してしまった
- 開発履歴を残したい

このようなことができる。

---

## なぜGitが必要なのか

プログラム開発では何度もコードを修正する。

例えば、

main.py

```python
print("Hello")
```

↓

```python
print("Hello World")
```

↓

```python
print("Hello Python")
```

のようにコードが変化していく。

Gitが無い場合、

- どのタイミングで変更したか分からない
- 元のコードに戻せない
- 誰が何を変更したか分からない

という問題が発生する。

Gitを使うと、

- いつ
- 何を
- なぜ

変更したのかを履歴として管理できる。

---

## Gitでできること

### ① 変更履歴を保存

コードの変更履歴を保存できる。

例

```text
2026-07-20
初回作成

2026-07-21
CSV取込機能追加

2026-07-22
Excel出力機能追加
```

---

### ② 過去の状態へ戻せる

過去の履歴へ戻すことができる。

例

```text
現在のコード
↓
バグ発生
↓
昨日の状態へ戻す
```

---

### ③ 変更箇所を確認できる

どこのコードを変更したか確認できる。

---

### ④ ブランチを作れる

機能ごとに開発を分けることができる。

例

```text
main

feature/git
feature/uv
feature/sql
feature/tkinter
```

---

# Git運用の流れ

プロジェクトフォルダを作成した後に、
まずGit管理を開始する。

---

# ① プロジェクトフォルダへ移動

```powershell
cd C:\Work\プロジェクト名
```

例

```powershell
cd C:\Work\python-learning_tkinter
```

---

## 何をしているのか

現在操作するプロジェクトフォルダへ移動している。

---

## 確認方法

```powershell
pwd
```

または

```powershell
Get-Location
```

---

# ② Git初期化

```powershell
git init
```

---

## 何をしているのか

Gitによるバージョン管理を開始している。

---

## 実行するとどうなるか

プロジェクトフォルダ内に

```text
.git
```

という隠しフォルダが作成される。

---

## .gitとは

Gitの管理情報が保存される場所。

中には

- コミット履歴
- ブランチ情報
- Git設定

などが格納される。

---

## Git初期化後のイメージ

```text
python-learning_tkinter
│
├─ .git
└─ その他ファイル
```

---

## 実務でどう使うか

新しいプロジェクト作成時に最初に実施する。

---

# ③ .gitignore 作成

## なぜ必要か

Gitへ登録したくないファイルを除外するため。

---

## 作成場所

```text
プロジェクトルート
```

例

```text
python-learning_tkinter
│
├─ .gitignore
```

---

## 内容

```gitignore
.venv/
__pycache__/
*.pyc
.vscode/
config/
data/output/
```

---

## 各項目の意味

### .venv/

Pythonの仮想環境。

各メンバーが個別に作成するためGit管理は不要。

---

### __pycache__/

Pythonが自動生成するキャッシュファイル。

---

### *.pyc

Pythonの中間ファイル（コンパイル済みファイル）。

---

### .vscode/

VS Codeの個人設定ファイル。

---

### config/

接続情報などの設定ファイル。

例

```ini
server=
database=
password=
```

機密情報を含むためGit管理しない。

---

### data/output/

Excel出力ファイルなど。

毎回生成できるため管理不要。

---

## 実務でどう使うか

不要ファイルや機密情報をGitへ登録しないために使用する。

---

# ④ Gitへ登録

## ④-1 変更状態確認

```powershell
git status
```

---

## 何をしているのか

Gitから見た現在の状態を確認している。

---

## よく確認する内容

- 変更されたファイル
- 新規ファイル
- 削除されたファイル

---

## 実務でどう使うか

作業完了時に必ず実行する。

---

## ④-2 ステージング

```powershell
git add .
```

---

## 何をしているのか

変更したファイルを

「コミット対象」

として登録している。

---

## イメージ

```text
編集
↓
git add .
↓
コミット待ち
```

---

## ポイント

この時点ではまだ履歴保存されていない。

---

## ④-3 コミット

```powershell
git commit -m "Initial commit"
```

---

## 何をしているのか

現在の状態を履歴として保存している。

---

## -m の意味

コミットメッセージ。

何を変更したかを記録する。

例

```powershell
git commit -m "Add CSV import feature"
```

---

## 良い例

```powershell
git commit -m "Add tkinter main screen"
```

```powershell
git commit -m "Add Excel export feature"
```

---

## 悪い例

```powershell
git commit -m "update"
```

理由

何を変更したのか分からない。

---

# Git運用でよく使うコマンド

## ブランチ作成

```powershell
git switch -c feature/tkinter
```

---

## ブランチ一覧

```powershell
git branch
```

---

## ブランチ切替

```powershell
git switch main
```

---

## 状態確認

```powershell
git status
```

---

## 履歴確認

```powershell
git log --oneline
```

---

# Git運用の基本サイクル

```powershell
git status

git add .

git commit -m "変更内容"
```

---

# Gitだけでも使える？

使える。

個人開発なら、

```text
Gitのみ
```

でも十分運用可能。

---

ただし、

- PC故障
- OS再インストール
- ディスク破損

などで履歴を失う可能性がある。

---

そのため実務では、

```text
Git
↓
GitHub
```

を組み合わせて使用する。

---

# ここまででできること

✅ Git管理開始

✅ 変更履歴保存

✅ 変更確認

✅ コミット

✅ ブランチ作成

✅ ブランチ切替

---

➡ 次は **github.md** へ

GitはローカルPC内で履歴管理を行う仕組み。

次はGitHubを利用し、

ローカルGitとGitHubを連携する。