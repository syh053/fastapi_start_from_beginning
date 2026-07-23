from typing import TypeVar, Callable

T = TypeVar('T')


def service_provide(cls: type[T]) -> Callable[[], T]:
    def dependency():
        return cls()
    return dependency
