from object import *

class Environment:
    def __init__(self, store: dict[str, Object] = None):
        self.store = store if store is not None else {}

    def get(self, name: str) -> tuple[Object, bool]:
        obj = self.store.get(name)
        return obj, obj is not None

    def set(self, name: str, val: Object) -> Object:
        self.store[name] = val
        return val
