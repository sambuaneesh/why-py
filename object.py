import abc
from typing import List, TYPE_CHECKING
from ast1 import Identifier, BlockStatement

# to avoid circular import
if TYPE_CHECKING:
    from environment import Environment

ObjectType = str

INTEGER_OBJ = "INTEGER"
BOOLEAN_OBJ = "BOOLEAN"
NULL_OBJ = "NULL"
RETURN_VALUE_OBJ = "RETURN_VALUE"
ERROR_OBJ = "ERROR"
FUNCTION_OBJ = "FUNCTION"


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


class Function(Object):
    def __init__(
        self, parameters: List[Identifier], body: BlockStatement, env: 'Environment'
    ):
        self.parameters = parameters
        self.body = body
        self.env = env

    def type(self) -> ObjectType:
        return FUNCTION_OBJ

    def inspect(self) -> str:
        return f"fn({', '.join([p.string() for p in self.parameters])}) {{ ... }}"
