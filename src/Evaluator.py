from QuestGenerator import BiTree
from fractions import Fraction


class Evaluator:

    def __init__(self):
        pass

    def evaluate(self, node: BiTree) -> Fraction:
        if node.node_type == 1:
            if node.val == 0:
                return self.evaluate(node.lchild) + self.evaluate(node.rchild)
            if node.val == 1:
                return self.evaluate(node.lchild) - self.evaluate(node.rchild)
            if node.val == 2:
                return self.evaluate(node.lchild) * self.evaluate(node.rchild)
            if node.val == 3:
                return self.evaluate(node.lchild) / self.evaluate(node.rchild)
        return Fraction(node.val)
