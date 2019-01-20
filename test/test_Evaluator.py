import unittest
import Evaluator
from BiTree import BiTree
from fractions import Fraction


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.ev = Evaluator.Evaluator()

    def tearDown(self):
        pass

    def test_number(self):
        root = BiTree(0, 5)
        self.assertEqual(5, self.ev.evaluate(root))

    def test_add(self):
        root = BiTree(1, 0)  # (-7) + 6
        root.set_lchild(BiTree(0, -7))
        root.set_rchild(BiTree(0, 6))
        self.assertEqual(-1, self.ev.evaluate(root))

    def test_sub(self):
        root = BiTree(1, 1)  # (-7) - 6
        root.set_lchild(BiTree(0, -7))
        root.set_rchild(BiTree(0, 6))
        self.assertEqual(-13, self.ev.evaluate(root))

    def test_mul(self):
        root = BiTree(1, 2)  # (-7) × 6
        root.set_lchild(BiTree(0, -7))
        root.set_rchild(BiTree(0, 6))
        self.assertEqual(-42, self.ev.evaluate(root))

    def test_div(self):
        root = BiTree(1, 3)  # (-14) ÷ 6
        root.set_lchild(BiTree(0, -14))
        root.set_rchild(BiTree(0, 6))
        self.assertEqual(Fraction(-7, 3), self.ev.evaluate(root))

    def test_pow(self):
        root = BiTree(1, 4)  # (-2) ^ 3
        root.set_lchild(BiTree(0, -2))
        root.set_rchild(BiTree(0, 3))
        self.assertEqual(-8, self.ev.evaluate(root))


if __name__ == '__main__':
    unittest.main()
