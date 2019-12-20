from vsrecorder.scenes.base import AvailableScenes, GameScene
from vsrecorder.scenes.searching import SearchingScene

AvailableScenes.extend([
    SearchingScene
])

__all__ = [
    'AvailableScenes', 'GameScene',
    'SearchingScene'
]
