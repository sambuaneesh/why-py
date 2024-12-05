import abc

ObjectType = str

INTEGER_OBJ = "INTEGER"
BOOLEAN_OBJ = "BOOLEAN"
NULL_OBJ = "NULL"
RETURN_VALUE_OBJ = "RETURN_VALUE"
ERROR_OBJ = "ERROR"

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
    
class ReturnValue(Object):
    def __init__(self, value: Object):
        self.value = value

    def type(self) -> ObjectType:
        return RETURN_VALUE_OBJ

    def inspect(self) -> str:
        return self.value.inspect()

class Error(Object):
    def __init__(self, message: str):
        self.message = message

    def type(self) -> ObjectType:
        return ERROR_OBJ

    def inspect(self) -> str:
        return f"ERROR: {self.message}"
