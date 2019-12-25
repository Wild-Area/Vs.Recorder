from typing import Optional, List

from vsrecorder.scenes import GameScene, AvailableScenes
from vsrecorder.types import Image, Vec2


def parse_scene(image: Image) -> Optional[GameScene]:
    for SceneType in AvailableScenes:
        scene = SceneType.try_parse(image)
        if scene is not None:
            return scene
    return None


def scan_text(image: Image, top_left: Optional[Vec2]=None, size: Optional[Vec2]=None) -> List[str]:
    return []
