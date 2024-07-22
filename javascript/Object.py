from __future__ import annotations as _

from typing import Any
from re import search, sub


__all__ = (
    'Object',
)


def applyCustomDict(dictString: str) -> dict:
    while s := search(reExp := r'\{+(?!.*\{+).*?}', dictString):
        dictString = sub(reExp, f'CustomDict({list(eval(s.group()).items())})', dictString, count=1)
    return eval(dictString)


class CustomDict(dict):
    def __getattr__(self, item) -> Any:
        return super().get(item)

    def __setattr__(self, key, value) -> None:
        return super().__setitem__(key, value)

    def __init__(self, seq=None, **kwargs) -> None:
        super().__init__()
        [self.__setitem__(key, value) for key, value in (dict(seq) | kwargs if seq else kwargs).items()]

    def __call__(self, seq=None, **kwargs) -> CustomDict:
        [self.__setitem__(key, value) for key, value in applyCustomDict(str(dict(seq) | kwargs if seq else kwargs)).items()]
        return self

    def __hash__(self) -> hash:
        return hash(self.__class__.__name__)

    def __or__(self, other) -> type(CustomDict):
        return type(self)

    def __ror__(self, other) -> type(CustomDict):
        return type(self)


class ObjectMeta(type):
    def __new__(mcs, name, bases, attrs) -> CustomDict | Object:
        if not attrs.get('__check__'):
            return CustomDict(attrs.get('__annotations__', {}))
        return super().__new__(mcs, name, bases, attrs)


class Object(metaclass=ObjectMeta):
    __check__ = True
