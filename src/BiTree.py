class BiTree:
    # 注意：除数不为0 - 遇见0改值 - 子树怎么确定是不是0？
    # 指数不能太大！
    operators = [' + ', ' - ', ' × ', ' ÷ ', ' ** ']

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

    @staticmethod
    def set_power_operator(on_off):
        BiTree.operators[4] = ' ^ ' if on_off else ' ** '

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
