from enum import Enum


class Direction(Enum):
    # (row, col)
    NORTH = 0, (-1, 0)
    SOUTH = 1, (1, 0)
    EAST = 2, (0, 1)
    WEST = 3, (0, -1)

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
    def vec(self):
        return self._all_values[1]
