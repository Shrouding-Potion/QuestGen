import QuestGenerator as Qg
import Evaluator
import sys
import getopt
from BiTree import BiTree

USAGE = '''
  
  Usage:
    -h, print this help, 显示帮助
    -n, num of expressions to generate (default: 4), 生成表达式数量
    -l, num of operators in each expression (default: 4), 每个表达式的算符数
    -e, enable Exponential Operator, 允许指数算符
    -^, Exponential Operator print as '^' rather than '**', 
        指数算符输出为 '^', 而不是'**'
'''

if __name__ == '__main__':
    num = 4
    operators = 4
    exp = False
    verbose = False

    # 解析参数
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:l:ev^")
    except getopt.GetoptError as e:
        print('\n  ' + e.msg + '\n')
        exit(21)
    else:
        for op, value in opts:
            if op == '-h':
                print(USAGE)
                exit(0)
            elif op == '-n':
                num = int(value)
            elif op == '-l':
                operators = int(value)
            elif op == '-e':
                exp = True
            elif op == '-v':
                verbose = True
            elif op == '-^':
                BiTree.set_power_operator(True)

    g = Qg.QuestGenerator()
    g.generate(quantity=num, operators=operators, enable_power=exp)
    ev = Evaluator.Evaluator()

    # 显示结果
    if verbose:
        for out in g.output_list:
            print(out.to_string())
        for out in g.output_list:
            print(str(ev.evaluate(out)))
    print('\n  Generate complete\n  Writing to file...')

    # 写入文件
    with open('quests.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out.to_string() + '\n')
    with open('solutions.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(str(ev.evaluate(out)) + '\n')

    print('\n  All work done')
