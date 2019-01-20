import unittest
from BiTree import BiTree


class TestBiTree(unittest.TestCase):
    def test_default_power(self):
        self.assertEqual(' ** ', BiTree.operators[4])

    def test_set_power(self):
        BiTree.set_power_operator(True)
        self.assertEqual(' ^ ', BiTree.operators[4])

    def test_set_power_2(self):
        BiTree.set_power_operator(False)
        self.assertEqual(' ** ', BiTree.operators[4])

    def test_op_priority(self):
        self.assertEqual(0, BiTree(1, 0).this_level)
        self.assertEqual(0, BiTree(1, 1).this_level)
        self.assertEqual(2, BiTree(1, 2).this_level)
        self.assertEqual(2, BiTree(1, 3).this_level)
        self.assertEqual(4, BiTree(1, 4).this_level)

    def test_to_string_L1(self):
        self.assertEqual('3', BiTree(0, 3).to_string())

    def test_to_string_L2(self):
        # 4 × 8
        root = BiTree(1, 2)
        root.set_lchild(BiTree(0, 4))
        root.set_rchild(BiTree(0, 8))
        self.assertEqual('4 × 8', root.to_string())

    def test_to_string_L3(self):
        # (5 + 6) ^ (4 - 2)
        root = BiTree(1, 4)
        lft = BiTree(1, 0)
        lft.set_lchild(BiTree(0, 5))
        lft.set_rchild(BiTree(0, 6))
        r = BiTree(1, 1)
        r.set_lchild(BiTree(0, 4))
        r.set_rchild(BiTree(0, 2))
        root.set_lchild(lft)
        root.set_rchild(r)
        self.assertEqual('(5 + 6) ** (4 - 2)', root.to_string())

        BiTree.set_power_operator(True)
        self.assertEqual('(5 + 6) ^ (4 - 2)', root.to_string())


if __name__ == '__main__':
    unittest.main()
