CREATE TABLE tbl_items
(
    item_key        INT IDENTITY(1,1) PRIMARY KEY,
    item_id         VARCHAR(20) NOT NULL UNIQUE,
    item_name       NVARCHAR(100) NOT NULL,
    model_no        VARCHAR(100) NULL,
    category        VARCHAR(50) NOT NULL,
    quantity        INT NOT NULL
                    CHECK (quantity >= 0),
    available_qty   INT NOT NULL
                    CHECK (available_qty >= 0),
    remarks         VARCHAR(500) NULL,
    created_at      DATETIME2(0) NOT NULL DEFAULT SYSDATETIME(),
    updated_at      DATETIME2(0) NOT NULL DEFAULT SYSDATETIME(),

    CONSTRAINT CK_tbl_items_available_qty
        CHECK (available_qty <= quantity)
);