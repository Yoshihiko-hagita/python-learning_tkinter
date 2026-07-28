# SQL Server 在庫管理システム 学習メモ

## 現在の進捗

### データベース

```sql
EquipmentDB
```

作成済み

---

## 作成済みテーブル

### tbl_users（ユーザマスタ）

|カラム名|説明|
|---------|---------|
|employee_id|社員ID(PK)|
|user_name|氏名|
|password_hash|パスワードハッシュ|
|authority|権限|
|mail_address|メールアドレス|
|created_at|登録日時|
|updated_at|更新日時|

### 制約

- PRIMARY KEY
    - employee_id

- CHECK
    - authority IN ('ADMIN','USER')

- UNIQUE
    - mail_address

---

### tbl_items（備品マスタ）

|カラム名|説明|
|---------|---------|
|item_key|内部キー(PK)|
|item_id|備品ID|
|item_name|備品名|
|model_no|品番|
|category|カテゴリ|
|quantity|総保有数|
|available_qty|貸出可能数|
|remarks|備考|
|created_at|登録日時|
|updated_at|更新日時|

### 制約

- PRIMARY KEY
    - item_key

- UNIQUE
    - item_id

- CHECK
    - quantity >= 0

- CHECK
    - available_qty >= 0

- CHECK
    - available_qty <= quantity

---

### tbl_history（履歴マスタ）

|カラム名|説明|
|---------|---------|
|history_id|履歴ID(PK)|
|employee_id|社員ID(FK)|
|item_id|備品ID(FK)|
|rental_date|貸出日|
|due_date|返却予定日|
|return_date|返却日|
|status|状態|
|created_at|登録日時|
|updated_at|更新日時|

### 制約

- PRIMARY KEY
    - history_id

- CHECK
    - status IN
      - RENTAL
      - RETURNED
      - STOP
      - REPAIR

---

## 外部キー作成済み

### ユーザとの関連

```text
tbl_users.employee_id
        ↓
tbl_history.employee_id
```

```sql
FK_tbl_history_users
```

---

### 備品との関連

```text
tbl_items.item_id
        ↓
tbl_history.item_id
```

```sql
FK_tbl_history_items
```

---

## ER図完成

```text
tbl_users
      │
      │
      ▼

tbl_history

      ▲
      │
      │

tbl_items
```

---

# 次にやること

## 優先度①

アプリからデータ登録できるようにする

### tbl_users

- ユーザー登録

### tbl_items

- 備品登録
- 備品更新

### tbl_history

- 貸出登録
- 返却登録

---

## 優先度②

SQL学習

### SELECT

```sql
SELECT
```

### WHERE

```sql
WHERE
```

### ORDER BY

```sql
ORDER BY
```

### JOIN

```sql
INNER JOIN
```

---

## 優先度③

インデックス学習

学習予定

```sql
CREATE INDEX
```

対象候補

```sql
tbl_history.employee_id
```

```sql
tbl_history.item_id
```

---

## 優先度④

ビュー(View)

学習予定

```sql
CREATE VIEW
```

例

- 貸出中一覧
- 返却期限超過一覧

---

## 優先度⑤

ストアドプロシージャ

学習予定

```sql
CREATE PROCEDURE
```

例

- 備品貸出処理
- 備品返却処理

---

## メモ

現在のDB設計は在庫管理システムの初版(v1)として十分使用可能。

今後はテーブル設計を増やすより、

「アプリから登録・更新・検索できること」

を優先する。