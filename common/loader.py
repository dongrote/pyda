from cStringIO import StringIO

class Loader(object):
    def __init__(self, filename=''):
        self.filename = filename
        self.iobuf = StringIO()

        self._file = open(filename, 'rb')
        self.blob = self._file.read()
        self._file.close()

        self.iobuf.write(self.blob)

