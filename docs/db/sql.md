# SQL Server 基礎メモ

---

# SQLとは

SQL（Structured Query Language）は、データベースを操作するための言語です。

SQLでは、

- テーブルを作成する
- データを登録する
- データを更新する
- データを削除する
- データを検索する

などを行います。

---

# DDL（Data Definition Language）

## 概要

DDLとは、

**データベースの構造（テーブルなど）を定義するSQL**

のことです。

つまり、

「箱（テーブル）を作る・変更する・削除する」

ためのSQLです。

## 主なDDL

|SQL|説明|
|---|---|
|CREATE|テーブルを作成する|
|ALTER|テーブル構造を変更する|
|DROP|テーブルを削除する|
|TRUNCATE|テーブル内のデータをすべて削除する|

## 例

```sql
CREATE TABLE tbl_users
(
    employee_id VARCHAR(8) PRIMARY KEY,
    user_name VARCHAR(100)
);
```

このSQLは

「tbl_usersというテーブルを作成する」

DDLになります。

---

# DML（Data Manipulation Language）

## 概要

DMLとは、

**テーブル内のデータを操作するSQL**

です。

箱（テーブル）はすでに存在していて、

その中のデータを

- 登録
- 更新
- 削除
- 取得

します。

## 主なDML

|SQL|説明|
|---|---|
|SELECT|データ取得|
|INSERT|データ登録|
|UPDATE|データ更新|
|DELETE|データ削除|

## 例

```sql
INSERT INTO tbl_users
(
    employee_id,
    user_name
)
VALUES
(
    'E000001',
    'Yamada'
);
```

これは

「データを追加する」

DMLになります。

---

# テーブルとは

テーブルとは、

Excelの表のようなものです。

例

|社員ID|氏名|
|------|----|
|E000001|山田|
|E000002|佐藤|

SQL Serverでは、この表をテーブルと呼びます。

---

# PRIMARY KEY（主キー）

## 概要

テーブルの中で

**1件のデータを一意に識別する列**

です。

つまり

「絶対に重複しない値」

になります。

例

```
E000001
E000002
E000003
```

これはOKです。

しかし

```
E000001
E000001
```

は登録できません。

## 特徴

- 重複できない
- NULL不可
- テーブルに1つだけ

例

```sql
employee_id VARCHAR(8) PRIMARY KEY
```

---

# UNIQUE

## 概要

重複を禁止する制約です。

PRIMARY KEYとの違いは

「主キーではないが重複させたくない列」

に使用します。

例

メールアドレス

```
aaa@test.com
bbb@test.com
ccc@test.com
```

OK

```
aaa@test.com
aaa@test.com
```

NG

## 例

```sql
mail_address VARCHAR(100) UNIQUE
```

また、

```sql
item_id VARCHAR(20) UNIQUE
```

とすると

同じ備品IDは登録できません。

---

# PRIMARY KEY と UNIQUE の違い

|項目|PRIMARY KEY|UNIQUE|
|---|---|---|
|重複|不可|不可|
|NULL|不可|可能（SQL Serverでは1件まで）|
|作成数|1つだけ|複数可|

---

# CHECK制約

## 概要

指定した値しか登録できないようにする制約です。

例

```sql
authority VARCHAR(20)
CHECK(authority IN ('ADMIN','USER'))
```

登録可能

```
ADMIN
USER
```

登録不可

```
AAAA
管理者
123
```

---

# DEFAULT

## 概要

値が指定されなかった場合、

自動で値を設定します。

例

```sql
created_at DATETIME2(0)
DEFAULT SYSDATETIME()
```

INSERT時に

```sql
INSERT INTO tbl_users
(
    employee_id,
    user_name
)
VALUES
(
    'E000001',
    'Yamada'
);
```

created_atを書かなくても

現在日時が自動で入ります。

---

# GETDATE()

## 概要

現在の日時を取得する関数です。

例

```sql
SELECT GETDATE();
```

結果

```
2026-07-26 09:30:15.123
```

戻り値の型

```
DATETIME
```

---

# SYSDATETIME()

## 概要

現在日時を取得する関数です。

GETDATE()より高精度です。

例

```sql
SELECT SYSDATETIME();
```

結果

```
2026-07-26 09:30:15.1234567
```

戻り値

```
DATETIME2
```

現在はDATETIME2型と一緒に使用することが多いです。

---

# DATETIME と DATETIME2

## DATETIME

昔からある日時型

例

```
2026-07-26 09:30:15.123
```

---

## DATETIME2

DATETIMEの改良版です。

例

```sql
DATETIME2(0)
```

保存

```
2026-07-26 09:30:15
```

```sql
DATETIME2(3)
```

保存

```
2026-07-26 09:30:15.123
```

```sql
DATETIME2(7)
```

保存

```
2026-07-26 09:30:15.1234567
```

現在はDATETIME2を使用することが推奨されています。

---

# VARCHAR と NVARCHAR

## VARCHAR

英数字用

例

```sql
user_name VARCHAR(100)
```

---

## NVARCHAR

Unicode対応

日本語、中国語などが保存できます。

例

```sql
department NVARCHAR(100)
```

---

# N'文字列'

NVARCHARへ文字列を渡すときに使用します。

例

```sql
N'管理者'
```

英数字だけなら

```sql
'ADMIN'
```

でも問題ありません。

---

# IDENTITY

## 概要

自動採番機能です。

例

```sql
history_id INT IDENTITY(1,1)
```

登録すると

```
1
2
3
4
```

と自動で番号が付きます。

---

# IDENTITY(1,1) の意味

```
IDENTITY(開始値,増分)
```

例

```sql
IDENTITY(1,1)
```

結果

```
1
2
3
4
```

例

```sql
IDENTITY(100,10)
```

結果

```
100
110
120
130
```

---

# 自動採番を付ける判断基準

## 会社がすでに管理番号を持っている場合

例

社員番号

```
E000001
E000002
```

備品管理番号

```
PC000001
PC000002
```

このように

**業務上すでに一意な番号が存在するなら、基本的にはその番号を主キーとして利用できます。**

---

## 管理番号が存在しない場合

例

貸出履歴

操作ログ

エラーログ

コメント

履歴

これらは会社に番号が存在しません。

そのため

```sql
history_id INT IDENTITY(1,1)
```

のような自動採番を使用します。

---

# 外部キー（FOREIGN KEY）

## 概要

他のテーブルの主キーを参照するための列です。

例

```
tbl_users

employee_id
```

↓

```
tbl_history

employee_id
```

このように関連付けます。

メリット

- 存在しない社員番号を登録できない
- データの整合性を保てる

---

# 今回の備品管理システムの設計

## tbl_users

社員情報

```
employee_id（PK）
user_name
password_hash
authority
mail_address
created_at
updated_at
```

---

## tbl_items

備品情報

```
item_key（PK・IDENTITY）
item_id（UNIQUE）
item_name
model_no
category
quantity
available_qty
remarks
created_at
updated_at
```

---

## tbl_history

貸出履歴

```
history_id（PK・IDENTITY）
employee_id（FK）
item_key（FK）
rental_date
due_date
return_date
status
created_at
updated_at
```

---

# 設計で一番大切な考え方

データベース設計では、

「とりあえず自動採番を付ける」

ではなく、

**業務上すでに管理番号が存在するか**

を最初に考える。

存在するなら、その番号を利用する。

存在しないデータだけ、自動採番（IDENTITY）を使用する。

この考え方を身につけると、実務でも通用するデータベース設計ができるようになる。