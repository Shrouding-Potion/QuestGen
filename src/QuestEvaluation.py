from fractions import Fraction
from math import gcd

class Evaluation:

    prior = {'+':0, '-':0, '*':1, '/':1, '^':2}
    numberator = 1
    denominator = 1

    def getvalue(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            divisor = gcd(num1, num2)
            if num2 == 1:
                return num1
            elif divisor != num2:
                self.numberator *= int(num1/divisor)
                self.denominator *= int(num2/divisor)
                return False
            else:
                return num1 / num2
        elif operator == "^":
            return pow(num1, num2)

    def process(self, data, opt):
        operator = opt.pop()
        num2 = data.pop()
        num1 = data.pop()
        num3 = self.getvalue(num1, num2, operator)
        if num3:
            data.append(num3)

    def Caculator(self):
        r = open("QuestGen\\src\\solve-me.txt", 'r', encoding = 'UTF-8')
        lines = r.readlines()
        for line in lines:
            opt = []
            data = []
            i = 0
            self.denominator = 1
            self.numberator = 1
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
            
            if self.numberator == 1 and self.denominator == 1:
                print('{:g}'.format(data.pop()))
            else:
                if data:
                    self.numberator *= data.pop()
                print (Fraction(self.numberator, self.denominator))

        r.close()
                    
if __name__ == '__main__':
   A = Evaluation()
   A.Caculator()