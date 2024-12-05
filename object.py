import abc

ObjectType = str

INTEGER_OBJ = "INTEGER"
BOOLEAN_OBJ = "BOOLEAN"
NULL_OBJ = "NULL"

class Object(abc.ABC):
    @abc.abstractmethod
    def type(self) -> ObjectType:
        pass

    @abc.abstractmethod
    def inspect(self) -> str:
        pass

class Integer(Object):
    def __init__(self, value: int):
        self.value = value

    def type(self) -> ObjectType:
        return INTEGER_OBJ
    
    def inspect(self) -> str:
        return str(self.value)

class Boolean(Object):
    def __init__(self, value: bool):
        self.value = value

    def type(self) -> ObjectType:
        return BOOLEAN_OBJ
    
    def inspect(self) -> str:
        return str(self.value).lower()

class Null(Object):
    def type(self) -> ObjectType:
        return NULL_OBJ
    
    def inspect(self) -> str:
        return "null"