from abc import ABCMeta, abstractmethod
from typing import Optional, List, Type, TypeVar

from vsrecorder.types import Image

T = TypeVar('T', bound='GameScene')


class GameScene(metaclass=ABCMeta):
    scene_name: str = 'Unknown'

    @classmethod
    @abstractmethod
    def try_parse(cls: Type[T], image: Image) -> Optional[T]:
        pass

    @abstractmethod
    def pretty_print(self) -> str:
        pass


AvailableScenes: List[Type[T]] = []
