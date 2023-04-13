import unittest
from pycachera import cache

class TestBasic(unittest.TestCase):
    def test_basic(self):
        key = '3cb364efb70fb9718a7dc2a5cc2b004d'
        assert cache().cachekey_gen((1,2,[1,2,],{'key':1,'key2':2})) == key
    def test_basicMPI(self):
        key = 'f09a45adb1f8a4ef6d7d58b44bc0e72e'
        assert cache(with_mpi=True).cachekey_gen((1,2,[1,2,],{'key':1,'key2':2})) == key