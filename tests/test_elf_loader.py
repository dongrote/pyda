from loaders.elf import *
import unittest

class TestELFLoader(unittest.TestCase):
    def setUp(self):
        self.loader = ELFLoader()

if '__main__' == __name__:
    unittest.main()
