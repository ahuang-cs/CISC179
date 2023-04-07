import os
import time
import unittest


class FileIOTest(unittest.TestCase):
    def setUp(self):
        self.fileName = __class__.__name__ + str(time.time())

    def tearDown(self):
        os.remove(self.fileName)

    def getFileName(self):
        return self.fileName