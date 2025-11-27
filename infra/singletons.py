from threading import Lock


class _SingletonMeta(type):
    _instances = {}
    _lock = Lock()


    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Config(metaclass=_SingletonMeta):
    def __init__(self):
        self.strategy = 'menor_preco'
        self.currency = 'BRL'

    @classmethod
    def get_instance(cls):
        return cls()

class Logger(metaclass=_SingletonMeta):
    def __init__(self):
        self.logs = []

    @classmethod
    def get_instance(cls):
        return cls()


    def log(self, message: str):
        self.logs.append(message)
        print(message)

class TariffTable(metaclass=_SingletonMeta):
    def __init__(self):
        self._table = {}

    @classmethod
    def get_instance(cls):
        return cls()

    def set(self, key, value):
        self._table[key] = value

    def get(self, key, default=None):
        return self._table.get(key, default)