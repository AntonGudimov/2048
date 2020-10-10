from enum import Enum


class GameState(Enum):
    NOT_PLAYING = 0
    PLAYING = 1
    WIN = 2
    FAIL = 3
