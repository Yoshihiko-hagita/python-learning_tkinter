CREATE TABLE tbl_history
(
    history_id      INT IDENTITY(1,1) PRIMARY KEY,
    employee_id     VARCHAR(8) NOT NULL,
    item_id         VARCHAR(20) NOT NULL,
    rental_date     DATE NOT NULL,
    due_date        DATE NOT NULL,
    return_date     DATE NULL,
    status          NVARCHAR(20) NOT NULL,
                    CHECK (
                        status IN (
                            'RENTAL',
                            'RETURNED',
                            'STOP',
                            'REPAIR'
                            )
                        ),
    created_at      DATETIME2(0) NOT NULL DEFAULT SYSDATETIME(),
    updated_at      DATETIME2(0) NOT NULL DEFAULT SYSDATETIME(),

    CONSTRAINT CK_tbl_history_due_date
    CHECK (due_date >= rental_date)
);