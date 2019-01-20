import unittest

from QuestEvaluation import Evaluation


class TestEvaluation(unittest.TestCase):

    def test_getvalue(self):
        x = Evaluation()
        a = x.getvalue(1, 2, '+')
        self.assertEqual(a, 3)
        b = x.getvalue(-1, -1, '-')
        self.assertEqual(b, 0)
        c = x.getvalue(0, -8, '*')
        self.assertEqual(c, 0)
        d = x.getvalue(3, 1, '/')
        self.assertEqual(d, 3)
        e = x.getvalue(0, 10, '^')
        self.assertEqual(e, 0)

    def test_process(self):
        data = [2, 7]
        opt = ['^']
        x = Evaluation()
        x.process(data, opt)
        self.assertEqual(data, [128])

    def test_caculator(self):
        x = Evaluation()
        Q = '1/(3 + 8*2 - 19)'
        try:
            a = x.Caculator(Q)
        except Exception:
            print("Divisor = 0")
        Q = '0/1'
        A = x.Caculator(Q)
        self.assertEqual(A, 0)
        Q = '1 + 1 - 1000'
        A = x.Caculator(Q)
        self.assertEqual(A, -998)
        Q = '0*8'
        A = x.Caculator(Q)
        self.assertEqual(A, 0)


if __name__ == "__main__":
    unittest.main()
