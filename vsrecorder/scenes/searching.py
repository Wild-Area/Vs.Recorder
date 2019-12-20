from typing import Optional

from vsrecorder.scenes.base import GameScene
from vsrecorder.types import Image
from vsrecorder.utils import i18n


class SearchingScene(GameScene):
    scene_name = 'searching'

    battle_type = 'battle_type-rating'
    battle_format = 'battle_format-double'
    total = 0
    wins = 0
    loses = 0
    rank_level = 'rank_level-master_ball'
    rank = 1000

    def pretty_print(self) -> str:
        return '\n'.join('{key}: {value}'.format(
            key=key, value=value
        ) for (key, value) in (
            (i18n('Battle Type'), i18n(self.battle_type)),
            (i18n('Battle Format'), i18n(self.battle_format)),
            (i18n('Battle Times'), self.total),
            (i18n('Win'), self.wins),
            (i18n('Lose'), self.loses),
            (i18n('Rank Level'), i18n(self.rank_level)),
            (i18n('Rank'), self.rank)
        ) if value is not None)

    @classmethod
    def try_parse(cls, image: Image) -> Optional['SearchingScene']:
        return None
