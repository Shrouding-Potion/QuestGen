import random
from copy import deepcopy


# from fractions import Fraction


class BiTree:
    # 注意：除数不为0 - 遇见0改值 - 子树怎么确定是不是0？
    # 指数不能太大！
    operators = (' + ', ' - ', ' × ', ' ÷ ', ' ^ ')

    def __init__(self, node_type=0, val=0):
        self.node_type = node_type  # 0为数值 1为算符
        self.val = val
        self.lchild = None  # type: BiTree
        self.rchild = None  # type: BiTree

        # 算符优先级
        if self.node_type == 1:
            self.this_level = 0
            if self.val in (0, 1):
                self.this_level = 0  # +- 0级
            elif self.val in (2, 3):
                self.this_level = 2  # ×÷ 2级
            elif self.val in (4,):
                self.this_level = 4  # ** 4级

    def set_lchild(self, lchild):
        self.lchild = lchild

    def set_rchild(self, rchild):
        self.rchild = rchild

    def set_children(self, lchild, rchild=None):
        self.lchild = lchild
        if rchild:
            self.rchild = rchild

    def to_string(self, upper_level=0):
        if self.node_type == 1:
            # 比较算符优先级决定是否加括号
            if upper_level > self.this_level:
                return '(' + self.lchild.to_string(self.this_level) + self.operators[self.val] + self.rchild.to_string(
                    self.this_level + 1) + ')'
            else:
                return self.lchild.to_string(self.this_level) + self.operators[self.val] + self.rchild.to_string(
                    self.this_level + 1)
        return str(self.val)


class QuestGenerator:
    def __init__(self):
        self.output_list = []  # type: list[BiTree]
        self.deduplicate_set = set()  # type: set[str]

    def generate(self, quantity=1, operators=7, enable_power=False):
        for loop in range(quantity):
            nums = [BiTree(0, x) for x in range(1, operators + 2)]
            ops = [BiTree(1, random.randint(0, len(BiTree.operators) - 2 + enable_power)) for _ in range(operators)]
            unfilled_ops = ops[:]
            filled_ops = nums[:]

            while len(unfilled_ops):
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_lchild(filled_ops[i])
                filled_ops.pop(i)
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_rchild(filled_ops[i])
                filled_ops.pop(i)

                filled_ops.append(unfilled_ops[0])
                unfilled_ops.pop(0)

            if not self.deduplicate(filled_ops[-1]):
                continue
            self.output_list.append(filled_ops[-1])
            print(self.output_list[-1].to_string())

    def gen_simple_divisor(self) -> BiTree:
        pass

    def gen_simple_power(self) -> BiTree:
        pass

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
