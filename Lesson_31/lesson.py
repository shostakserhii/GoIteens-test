from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


# with OpenFile('test_file.txt', 'w') as f:
#     f.write('our first context manager')

with open_file('test_file.txt', 'w') as f:
    f.write('our first context manager')
    print('wrote to file --- Done')
