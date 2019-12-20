from typing import Optional

from vsrecorder.scenes import GameScene, AvailableScenes
from vsrecorder.types import Image


def parse_scene(image: Image) -> Optional[GameScene]:
    for SceneType in AvailableScenes:
        scene = SceneType.try_parse(image)
        if scene is not None:
            return scene
    return None
