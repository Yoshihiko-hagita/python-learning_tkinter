CREATE TABLE tbl_users
(
    employee_id    VARCHAR(8) PRIMARY KEY,
    user_name      VARCHAR(100) NOT NULL,
    password_hash  VARCHAR(255) NOT NULL,

    authority      VARCHAR(20) NOT NULL
                   CHECK (authority IN ('ADMIN','USER')),

    mail_address   VARCHAR(100) NULL UNIQUE,

    created_at     DATETIME2(0) NOT NULL
                   DEFAULT SYSDATETIME(),

    updated_at     DATETIME2(0) NOT NULL
                   DEFAULT SYSDATETIME()
);