from object import Object

class Environment:
    def __init__(self, store: dict[str, Object] = None, outer: 'Environment' = None):
        self.store = store if store is not None else {}
        self.outer = outer

    @classmethod
    def new_environment(cls) -> 'Environment':
        return cls(store={}, outer=None)

    @classmethod
    def new_enclosed_environment(cls, outer: 'Environment') -> 'Environment':
        env = cls.new_environment()
        env.outer = outer
        return env

    def get(self, name: str) -> tuple[Object, bool]:
        obj = self.store.get(name)
        if obj is None and self.outer is not None:
            return self.outer.get(name)
        return obj, obj is not None

    def set(self, name: str, val: Object) -> Object:
        self.store[name] = val
        return val
