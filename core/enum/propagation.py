from enum import Enum, auto

class Propagation(str,Enum):
    REQUIRED = "required"
    REQUIRED_NEW = "required_new"


class SortOrder(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'


