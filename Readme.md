# 软工作业 - 四则运算生成

> 博客地址
>
> - [Shadow-Priest] https://www.jianshu.com/p/c168e46e87c2
> - [Ash0ne] https://blog.csdn.net/weixin_43904922/article/details/86350033

---

### 依赖

> PyQt5
>
> pyqt5-tools
>
> pyinstaller

### 参数列表

```bash
  
  Usage:
    -h, print this help, 显示帮助
    -n, num of expressions to generate (default: 4), 生成表达式数量
    -l, num of operators in each expression (default: 4), 每个表达式的算符数
    -e, enable Exponential Operator, 允许指数算符
    -p, Exponential Operator print as '^' rather than '**', 
        指数算符输出为 '^', 而不是'**'3
    -v, verbose output, 冗长输出 - 打印将写入的题目和答案
    -i, interactive mode, 交互模式，允许用户输入答案并得到正误统计
    
```

### 打包

```bash
pyinstaller -F src/main.py
pyinstaller -F src/gui-main.py --windowed
```

