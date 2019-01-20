import sys
import mainwnd
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import QuestGenerator as Qg
import Evaluator


class MyWindow(QMainWindow, mainwnd.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels(['题目', '答案', '正确?'])
        self.timer = QTimer()
        self.label_3.setText('')
        self.label_4.setText('20s')

        self.g = Qg.QuestGenerator()
        self.ev = Evaluator.Evaluator()
        self.submitted = False
        self.correct = False
        self.remaining = 20

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.timer.timeout.connect(self.timer_timeout)

    def timer_timeout(self):
        self.remaining -= 1
        if self.remaining < 0:
            self.pushButton_3_clicked()
            return
        self.label_4.setText('{}s'.format(self.remaining))

    def pushButton_clicked(self):
        # 记录上题结果
        if len(self.g.output_list):
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(self.g.output_list[-1].to_string()))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(str(self.ev.evaluate(self.g.output_list[-1]))))
            self.tableWidget.setItem(0, 2, QTableWidgetItem('Yes' if self.correct else 'No'))
            self.submitted = False
            self.correct = False
            self.label_3.setText('')
            self.remaining = 20
            self.label_4.setText('{}s'.format(self.remaining))

        # 产生新题目
        self.g.generate(quantity=1, operators=2, enable_power=False)
        self.line_quest.setText(self.g.output_list[-1].to_string())
        self.line_answer.setText('')
        self.timer.start(1000)

    # 查看答案按钮
    def pushButton_2_clicked(self):
        if not len(self.g.output_list):
            return
        self.line_answer.setText(str(self.ev.evaluate(self.g.output_list[-1])))

    # 提交按钮
    def pushButton_3_clicked(self):
        # 不允许重复提交
        if not len(self.g.output_list) or self.submitted:
            return
        self.timer.stop()
        self.submitted = True
        if self.line_answer.text() == str(self.ev.evaluate(self.g.output_list[-1])):
            self.correct = True
            self.label_3.setText('正确')
        else:
            self.correct = False
            self.label_3.setText('错误：应为 {}'.format(str(self.ev.evaluate(self.g.output_list[-1]))))


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # 启用HiDPI设置
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    # ui = mainwnd.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
