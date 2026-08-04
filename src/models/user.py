from dataclasses import dataclass

@dataclass
class User:
    employee_id: str
    name: str
    mail_address: str
    authority: str
    password: str
    password_confirm: str