from typing import Optional, List

from vsrecorder.scenes import GameScene, AvailableScenes
from vsrecorder.types import Image


def parse_scene(image: Image) -> Optional[GameScene]:
    for SceneType in AvailableScenes:
        scene = SceneType.try_parse(image)
        if scene is not None:
            return scene
    return None


def scan_text(image: Image) -> Optional[List[str]]:
    return None
