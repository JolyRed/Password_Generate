from PyQt5 import QtWidgets
from main_qt import Ui_MainWindow
from window_generate import Ui_Form
from PyQt5.QtWidgets import QMessageBox
import sys
from random import choice
import pyperclip

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click_window_generate)

    def on_click_window_generate(self):
        self.hide()
        self.win_gen = WindowGenerate()
        self.win_gen.show()



class WindowGenerate(QtWidgets.QWidget):
    def __init__(self):
        super(WindowGenerate, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MainFunc)
        self.ui.btn_check_strong.clicked.connect(self.check_strong)
        self.ui.pushButton_2.clicked.connect(self.copy_password)
        self.ui.pushButton_3.clicked.connect(self.save_password)
        self.ui.btn_reload.clicked.connect(self.reload)

    def MainFunc(self):
        self.len_pass = self.ui.lineEdit.text()
        self.simvols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&*+-=?@^_'
        password = ''

        if self.len_pass == '':
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Поле не может быть пустым')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return


        if self.len_pass.isnumeric() == False:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Длинна пароля должна быть указана только числом больше нуля и не иметь буквенных символов')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return

        if int(self.len_pass) <= 0:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Длинна пароля должна быть больше нуля')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return

        else:
            self.ui.main_edit.clear()
            for x in range(int(self.len_pass)):
                password += choice(self.simvols)

            self.ui.main_edit.setText(self.ui.main_edit.text() + password)


    def check_strong(self):
        if 1 < len(self.ui.main_edit.text()) <= 6:
            self.ui.label_strong.setText('Пароль: слабый')

        if 6 < len(self.ui.main_edit.text()) <= 10:
            self.ui.label_strong.setText('Пароль: средний')

        if 11 <= len(self.ui.main_edit.text()):
            self.ui.label_strong.setText('Пароль: сильный')


    def copy_password(self):
        if len(self.ui.main_edit.text()) == 0:
            msg = QMessageBox()
            msg.setWindowTitle('Внимание')
            msg.setText('Нельзя скопировать пустой пароль')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        else:
            pyperclip.copy(self.ui.main_edit.text())
            msg = QMessageBox()
            msg.setWindowTitle('Внимание')
            msg.setText('Пароль скопирован')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return


    def save_password(self):
        if len(self.ui.main_edit.text()) == 0:
            msg = QMessageBox()
            msg.setWindowTitle('Внимание')
            msg.setText('Нельзя сохранить пустой пароль')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        else:
            my_file = open('Save_password.txt', 'a+')
            my_file.write(self.ui.main_edit.text() + '\n')
            my_file.close()
            msg = QMessageBox()
            msg.setWindowTitle('Внимание')
            msg.setText('Пароль сохранён')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return

    def reload(self):
        self.ui.lineEdit.setText('')
        self.ui.label_strong.setText('')
        self.ui.main_edit.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec_())
