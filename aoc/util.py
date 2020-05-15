class FileReader:
    def __init__(self, f):
        self._file = f

    def __iter__(self):
        return map(lambda x: x.strip(), iter(self._file))

    def iter_circular(self):
        """
        Python doesn't support resetting iterators so this loads the file data into memory so the looping can be
        repeated indefinitely until broken by the callee

        :return: Generator
        """
        lines = [line for line in self]
        cursor = 0
        while True:
            yield lines[cursor]
            cursor += 1
            if cursor == len(lines):
                cursor = 0
