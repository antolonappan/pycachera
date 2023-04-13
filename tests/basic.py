import unittest
from pycachera import cache

class TestBasic(unittest.TestCase):
    def test_basic(self):
        key = 'f09a45adb1f8a4ef6d7d58b44bc0e72e'
        assert cache().cachekey_gen((1,2,[1,2,],{'key':1,'key2':2})) == key