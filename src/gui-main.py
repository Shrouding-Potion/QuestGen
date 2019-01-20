import sys
import mainwnd
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import QuestGenerator as Qg
import Evaluator


class MyWindow(QMainWindow, mainwnd.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)

        self.g = Qg.QuestGenerator()
        self.ev = Evaluator.Evaluator()

    def pushButton_clicked(self):
        self.g.generate(quantity=1, operators=3, enable_power=False)
        self.line_quest.setText(self.g.output_list[-1].to_string())
        self.line_answer.setText('')

    def pushButton_2_clicked(self):
        self.line_answer.setText(str(self.ev.evaluate(self.g.output_list[-1])))


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # 启用HiDPI设置
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    # ui = mainwnd.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
