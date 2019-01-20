import unittest
import QuestGenerator as Qg
from BiTree import BiTree


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.g = Qg.QuestGenerator()

    def tearDown(self):
        pass

    def test_format_L1(self):
        node = BiTree(0, 4)
        self.g.format_expression(node)
        self.assertEqual('4', node.to_string())

    def test_format_L2(self):
        # 6 + 3 -> 3 + 6
        root = BiTree(1, 0)
        root.set_lchild(BiTree(0, 6))
        root.set_rchild(BiTree(0, 3))
        self.g.format_expression(root)
        self.assertEqual('3 + 6', root.to_string())

    def test_format_L3(self):
        # (6 + 5) × (4 - 2) -> (4 - 2) × (5 + 6)
        root = BiTree(1, 2)
        lft = BiTree(1, 0)
        lft.set_lchild(BiTree(0, 6))
        lft.set_rchild(BiTree(0, 5))
        r = BiTree(1, 1)
        r.set_lchild(BiTree(0, 4))
        r.set_rchild(BiTree(0, 2))
        root.set_lchild(lft)
        root.set_rchild(r)

        self.g.format_expression(root)
        self.assertEqual('(4 - 2) × (5 + 6)', root.to_string())

    def test_deduplicate(self):
        tree1 = BiTree(0, 4)

        tree2 = BiTree(1, 0)
        tree2.set_lchild(BiTree(0, 6))
        tree2.set_rchild(BiTree(0, 3))

        tree3 = BiTree(1, 2)
        lft = BiTree(1, 0)
        lft.set_lchild(BiTree(0, 6))
        lft.set_rchild(BiTree(0, 5))
        r = BiTree(1, 1)
        r.set_lchild(BiTree(0, 4))
        r.set_rchild(BiTree(0, 2))
        tree3.set_lchild(lft)
        tree3.set_rchild(r)

        self.assertEqual(True, self.g.deduplicate(tree1))
        self.assertEqual(False, self.g.deduplicate(tree1))
        self.assertEqual(True, self.g.deduplicate(tree2))
        self.assertEqual(False, self.g.deduplicate(tree2))
        self.assertEqual(True, self.g.deduplicate(tree3))
        self.assertEqual(False, self.g.deduplicate(tree3))


if __name__ == '__main__':
    unittest.main()
