from sqlalchemy import Enum

class UserRole(str, Enum):
    GERERAL = 'GERERAL'
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'