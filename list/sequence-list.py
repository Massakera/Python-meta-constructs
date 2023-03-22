class MySequence:
    def __init__(self, *args):
        self._items = list(args)

    def _getitem_(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __repr__(self) -> str:
        return f'MySequence({self._items!r})'

    def __setitem__(self, index, value):
        self._items[index] = value

    def __str__(self) -> str:
        return str(self._items)
