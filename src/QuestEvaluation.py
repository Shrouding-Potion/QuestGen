from fractions import Fraction

class Evaluation:

    prior = {'+':0, '-':0, '*':1, '/':1, '^':2} #算符优先级表

    def getvalue(self, num1, num2, operator):
        # 获取运算结果
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise Exception("Divisor = 0")
            return Fraction(num1, num2)
        elif operator == "^":
            return pow(num1, num2)

    def process(self, data, opt):
        operator = opt.pop()
        num2 = data.pop()
        num1 = data.pop()
        num3 = self.getvalue(num1, num2, operator)
        data.append(num3)

    def Caculator(self, line):
        # 中缀表达式转换为后缀表达式的过程中同时计算结果
        opt = []
        data = []
        i = 0
        while i < len(line):
            if line[i] == ' ' or line[i] == '\n':
                pass
            elif line[i].isdigit():
                start = i
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                data.append(int(line[start: i + 1]))
            elif line[i] == ')':
                while opt[-1] != '(':
                    self.process(data, opt)
                opt.pop()
            elif not opt or opt[-1] == "(":
                opt.append(line[i])
            elif line[i] == "(" or self.prior[line[i]] > self.prior[opt[-1]]:
                opt.append(line[i])
            else:
                while opt and self.prior[line[i]] <= self.prior[opt[-1]]:
                    if opt[-1] == "(":
                        break
                    self.process(data, opt)
                opt.append(line[i])
            i += 1
        while opt:
            self.process(data, opt)
    
        return data.pop()
