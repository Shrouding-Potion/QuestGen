import QuestGenerator as Qg
import Evaluator
import sys
import getopt

USAGE = '''
  
  Usage:
    -h, print this help
    -n, num of expressions to generate (default: 4)
    -l, num of operators in each expression (default: 4)
    -e, enable Exponential Operator (default false)
'''

if __name__ == '__main__':
    num = 4
    operators = 4
    exp = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:l:e")
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

    g = Qg.QuestGenerator()
    g.generate(quantity=num, operators=operators, enable_power=exp)
    ev = Evaluator.Evaluator()
    print(ev.evaluate(g.output_list[0]))

    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out.to_string() + '\n')
