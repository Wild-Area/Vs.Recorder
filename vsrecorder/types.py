from typing import TypeVar, Tuple, NewType
import cv2
import numpy


T = TypeVar('T')
U = TypeVar('U')
Vec2 = NewType('Vec2', Tuple[int, int])


class Image:
    def __init__(self, data: numpy.ndarray):
        self.data = data

    @classmethod
    def from_file(cls, filename: str):
        return cls(cv2.imread(filename))
