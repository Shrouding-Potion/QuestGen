import random
from copy import deepcopy
from BiTree import BiTree
from Evaluator import Evaluator


class QuestGenerator:
    UPPERCAP = 28

    def __init__(self):
        self.output_list = []  # type: list[BiTree]
        self.deduplicate_set = set()  # type: set[str]

    def generate(self, quantity=1, operators=7, enable_power=False):
        for loop in range(quantity):
            nums = [BiTree(0, random.randint(0, self.UPPERCAP)) for _ in range(1, operators + 2)]
            ops = [BiTree(1, random.randint(0, len(BiTree.operators) - 2 + enable_power)) for _ in range(operators)]
            unfilled = ops[:]
            filled = nums[:]
            ev = Evaluator()

            # 链接成树
            while len(unfilled):
                i = random.randint(0, len(filled) - 1)
                unfilled[0].set_lchild(filled[i])
                filled.pop(i)

                # 除法 乘方 特殊处理
                i = random.randint(0, len(filled) - 1)
                if unfilled[0].node_type == 1 and unfilled[0].val == 3:
                    # 除数为0
                    if ev.evaluate(filled[i]) == 0:
                        unfilled[0].set_rchild(BiTree(0, random.randint(1, self.UPPERCAP)))
                    else:
                        unfilled[0].set_rchild(filled[i])
                elif unfilled[0].node_type == 1 and unfilled[0].val == 4:
                    # 指数过大 或 为分数
                    if abs(ev.evaluate(filled[i])) > 2 or ev.evaluate(filled[i]).denominator != 1:
                        unfilled[0].set_rchild(BiTree(0, random.randint(1, 2)))
                    else:
                        unfilled[0].set_rchild(filled[i])
                else:
                    unfilled[0].set_rchild(filled[i])
                filled.pop(i)

                filled.append(unfilled[0])
                unfilled.pop(0)

            if not self.deduplicate(filled[-1]):
                continue
            self.output_list.append(filled[-1])

    def deduplicate(self, root: BiTree):
        # 深拷贝 - 避免破坏原有的随机顺序
        inspect = deepcopy(root)
        QuestGenerator.format_expression(inspect)
        if inspect.to_string() in self.deduplicate_set:
            return False
        else:
            self.deduplicate_set.add(inspect.to_string())
            return True

    @staticmethod
    def format_expression(node: BiTree):
        if not node.lchild:
            return
        QuestGenerator.format_expression(node.lchild)
        QuestGenerator.format_expression(node.rchild)
        # 仅有+×可交换
        if node.val in (0, 2) and node.lchild.to_string() > node.rchild.to_string():
            tmp = node.lchild
            node.lchild = node.rchild
            node.rchild = tmp
