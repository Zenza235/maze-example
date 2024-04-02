from enum import Enum

TILE_SIZE = 30


class Tile(Enum):
    EMPTY = 0, (0, 0, 0)
    WALL = 1, (200, 200, 200)
    START = 5, (200, 160, 0)
    END = 8, (128, 0, 128)
    PLAYER = 2, (50, 200, 50)

    def __new__(cls, *values):
        obj = object.__new__(cls)
        obj._value_ = values[0]
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj
        obj._all_values = values
        return obj

    def __repr__(self):
        return '<%s.%s: %s>' % (
            self.__class__.__name__,
            self.__name__,
            ', '.join([repr(v) for v in self._all_values])
        )

    @property
    def color(self):
        return self._all_values[1]
