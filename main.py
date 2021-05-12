import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("capston.ui")[0]

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LogStringHandler(logging.Handler):
    def __init__(self, target_widget):
        super(LogStringHandler, self).__init__()
        self.target_widget = target_widget

    def emit(self, record):
        self.target_widget.append(record.asctime + ' -- ' + record.getMessage())

"""class TestWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUI(self)

        logger = logging.getLogger()
        logger.addHandler(LogStringHandler(self.testTextBrowser))

        self.testButton.clicked.connect(self.clicked_test_button)

    def clicked_test_button(self):
        message_alter = self.test_logging()
        QMessageBox.about(self, 'testButton 눌림 알람', message_alter)

    def test_logging(self):
        total_repeat_count = int(self.countTempDummy.test() if self.countTempDummt.text() != '' else 0)
        if total_repeat_count <=0:
            return '출력대상없음'
        for i in range(0, total_repeat_count):
            logging.error('Error %s ' % i)
            logging.info('Info %s ' % i)
            logging.warning('Warning %s ' % i)
            logging.debug('Debug %s ' % i)
        return '출력'
"""

class Ui_MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.btn_clicked1)
        self.btn_2.clicked.connect(self.btn_clicked2)
        self.btn_3.clicked.connect(self.btn_clicked3)
        self.btn_4.clicked.connect(self.btn_clicked4)
        self.btn_5.clicked.connect(self.btn_clicked5)
    def btn_clicked1(self):
        #filename = QFileDialog.getOpenFileName()
        #self.label_5.setText(filename[0])

        exec(open('capture.py').read())

    def btn_clicked2(self):
        #filename = QFileDialog.getOpenFileName()
        #self.label_6.setText(filename[0])

        exec(open('training.py').read())

    def btn_clicked3(self):
        import play

        play.player = play.VideoPlayer()
        play.player.setWindowTitle("Player")
        play.player.resize(600, 400)
        play.player.show()


    def btn_clicked4(self):
        exec(open('masking.py').read())

    def btn_clicked5(self):
        filename = QFileDialog.getOpenFileName()
        self.label.setText(filename[0])

    def btn_clicked6(self):
        filename = QFileDialog.getOpenFileName()
        self.label_2.setText(filename[0])


    def textEdit(self):
        self.textEdit=QTextEdit(self)

    def filedialog_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                'All File(*)')
        if fname[0]:
             # 튜플 데이터에서 첫 번째 인자 값이 주소이다.
            self.pathLabel.setText(fname[0])
            print('filepath : ', fname[0])
            print('filesort : ', fname[1])

            # 텍스트 파일 내용 읽기
            f = open(fname[0], 'r', encoding='UTF8')  # Path 정보로 파일을 읽는다.
            with f:
                data = f.read()
            self.textEdit.setText(data)
        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Ui_MainWindow()
    myWindow.show()
    app.exec_()

