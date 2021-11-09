from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):

        with cls._lock:

            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class ChocolateBoiler(metaclass=SingletonMeta):

    def __init__(self):
        self._empty = True
        self._boiled = False

    def fill(self):
        if self.empty:
            self._empty = False
            self._boiled = False

    def drain(self):
        if not self.empty and self.boiled:
            self._empty = True
            self._boiled = False

    def boil(self):
        if not self.empty and not self.boiled:
            self._boiled = True

    @property
    def empty(self):
        return self._empty

    @property
    def boiled(self):
        return self._boiled

    def __str__(self):
        return f"Empty: {self.empty}\nBoiled: {self.boiled}"


boiler = ChocolateBoiler()
print("Initial state:")
print(boiler)

print("\nFilling the boiler with chocolate..")
boiler.fill()
print(boiler)

print("\nBoiling the chocolate")
boiler.boil()
print(boiler)

print("\nDraining the boiler..")
boiler.drain()
print(boiler)
