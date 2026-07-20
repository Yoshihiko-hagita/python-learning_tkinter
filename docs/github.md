# GitHub

## GitHubとは

GitHubは、Gitで管理しているプロジェクトをインターネット上で管理できるサービス。

GitはローカルPC内で履歴管理を行う仕組みだが、
GitHubを利用することで、

- バックアップ
- チーム開発
- 複数PCでの開発
- ソースコード共有

ができるようになる。

---

## GitとGitHubの違い

### Git

ローカルPCで履歴を管理する仕組み。

例

```text
自分のPC
└ Git
```

---

### GitHub

Gitの履歴をクラウド上に保存するサービス。

例

```text
自分のPC
└ Git
      ↓
GitHub
```

---

## なぜGitHubが必要なのか

Gitだけでも開発は可能。

しかし、

- PC故障
- SSD故障
- OS再インストール
- 別PCで作業したい

などの場合に履歴が消失する可能性がある。

GitHubへ保管することで、

クラウド上にバックアップされる。

---

## GitHubでできること

### ① ソースコードのバックアップ

GitHub上へソースコードを保存できる。

---

### ② 複数PCでの開発

自宅PC

↓

GitHub

↓

会社PC

のように同じプロジェクトを利用可能。

---

### ③ チーム開発

複数人で同じプロジェクトを開発できる。

---

### ④ Pull Request

変更内容をレビューしてもらえる。

---

### ⑤ ブランチ管理

GitHub上でもブランチを管理できる。

---

## GitHub運用の流れ

Gitの初期設定とコミットが完了したら、
GitHubへ連携する。

---

# ① GitHubへアクセス

ブラウザでGitHubへアクセスする。

---

## URL

```text
https://github.com
```

---

## GitHubアカウント

今回の学習環境

```text
Yoshihiko-hagita
```

---

# ② New Repository作成

ログイン後、

右上の

```text
+
↓
New repository
```

を選択する。

---

## Repository名

プロジェクト名と同じ名前にする。

例

```text
python-learning_tkinter
```

---

## Visibility

通常は

```text
Private
```

を選択する。

---

## なぜPrivate？

学習用コードを非公開で管理できるため。

---

## 実務では？

社内開発ではPrivateが一般的。

OSS（公開プロジェクト）はPublicを使用する。

---

# ③ Repository作成

```text
Create repository
```

を押す。

---

## 何をしているのか

GitHub上に保存先を作成している。

---

## イメージ

```text
GitHub
└ python-learning_tkinter
```

が作成される。

---

# ④ GitHubとGitを紐付ける

作成後、

VS Codeへ戻る。

---

## 現在の状態

```text
ローカルPC
└ Git
```

---

## 目標

```text
ローカルPC
└ Git
      ↓
GitHub
```

を実現する。

---

# ⑤ リモートリポジトリ登録

```powershell
git remote add origin リポジトリURL
```

例

```powershell
git remote add origin https://github.com/Yoshihiko-hagita/python-learning_tkinter.git
```

---

## 何をしているのか

GitHubを保存先として登録している。

---

## originとは

GitHub保存先の別名。

一般的に

```text
origin
```

を使用する。

---

## 確認方法

```powershell
git remote -v
```

---

## 実行結果例

```text
origin  https://github.com/Yoshihiko-hagita/python-learning_tkinter.git
origin  https://github.com/Yoshihiko-hagita/python-learning_tkinter.git
```

---

# ⑥ mainブランチへ変更

```powershell
git branch -M main
```

---

## なぜ必要か

Gitのデフォルトブランチを

```text
main
```

へ統一するため。

---

## 実務でもmainが一般的

```text
main
feature/uv
feature/tkinter
feature/sql
```

---

# ⑦ GitHubへ初回Push

```powershell
git push -u origin main
```

---

## 何をしているのか

ローカルGitの内容をGitHubへアップロードしている。

---

## 各意味

### push

GitHubへ送信

---

### origin

GitHub保存先

---

### main

送信するブランチ

---

### -u

追跡設定

---

## 追跡設定とは

初回のみ実施する。

---

実施前

```text
ローカルmain
GitHub main
```

が別管理。

---

実施後

```text
main
↓
origin/main
```

が紐付く。

---

## 実務メリット

次回以降

```powershell
git push
```

だけでよくなる。

---

# ⑧ GitHubで確認

GitHub画面を更新する。

---

## 確認内容

README.md

.gitignore

src

docs

などが表示される。

---

## 表示されていれば成功

```text
ローカルPC
↓
Git
↓
GitHub
```

の連携完了。

---

# 普段の運用

## 作業開始

ブランチ作成

```powershell
git switch -c feature/tkinter
```

---

## 作業終了

変更確認

```powershell
git status
```

ステージング

```powershell
git add .
```

コミット

```powershell
git commit -m "Add tkinter screen"
```

Push

```powershell
git push -u origin feature/tkinter
```

---

## Pull Request

GitHub上で

```text
feature/tkinter
↓
main
```

へのPull Requestを作成する。

---

## Merge

レビュー後

```text
Merge
```

を実施。

---

## featureブランチ削除

GitHub側

```text
feature/tkinter
```

削除。

---

ローカル側

```powershell
git branch -d feature/tkinter
```

削除。

---

# よく使うGitHub連携コマンド

## リモート確認

```powershell
git remote -v
```

---

## Push

```powershell
git push
```

---

## Pull

```powershell
git pull
```

---

## ブランチ一覧

```powershell
git branch
```

---

## 新規ブランチ

```powershell
git switch -c feature/○○
```

---

# GitHubを使うメリット

✅ バックアップ

✅ クラウド保存

✅ チーム開発

✅ Pull Request

✅ ブランチ運用

✅ 複数PC利用

---

# Gitだけとの違い

Gitのみ

```text
ローカルPC
└ Git
```

GitHubあり

```text
ローカルPC
└ Git
      ↓
GitHub
```

GitHubがあることで、
安全に履歴を保管できる。

---

# ここまででできること

✅ GitHubリポジトリ作成

✅ GitHubとGit連携

✅ Push

✅ Pull

✅ ブランチ運用

✅ Pull Request

✅ Merge

---

# 次は uv.md へ

GitとGitHubでソースコード管理ができるようになった。

次はuvを利用して、

- 仮想環境
- パッケージ管理
- 依存関係管理

を行う。