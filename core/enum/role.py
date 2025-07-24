from enum import Enum, auto

class Role(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    TUTOR = "tutor"
    SUPER_ADMIN = "superadmin"
