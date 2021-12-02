from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import uic
import sys
import os

sys.path.insert(0, os.path.realpath(os.path.join(os.getcwd(), "Tools")))
from cvsTool.csvtool import csvReader
from dbTool.dbtool import DBTool


class App(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUI(self):
        uic.loadUi('screens/screen.ui', self)
        self.setWindowTitle('csv2DB')
        self.btDosyaAc.clicked.connect(self.openFilecsv)
        self.btDBAc.clicked.connect(self.openDBFile)
        self.show()

    def openFilecsv(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File',
                                            'CSV Files (*.csv)')
        if fname[0]:
            self.txtAdres.setText(fname[0])
        else:
            QMessageBox.warning(self, 'Uyarı', 'Dosya Seçilmedi')

    def openDBFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File',
                                            'DB Files (*.db)')
        if fname[0]:
            self.txtDbAdres.setText(fname[0])
        else:
            QMessageBox.warning(self, 'Uyarı', 'Dosya Seçilmedi')

    def startDB(self):
        csvRd = csvReader(self.txtAdres.text())
        csvRd.read()
        dbRd = DBTool(self.txtDbAdres.text(),
                      table=csvRd.tableName,
                      columns=csvRd.columns)
        dbRd.createTable()
        dbRd.insertData(csvRd.data)
        QMessageBox.information(self, 'Bilgi', 'İşlem Tamamlandı')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.initUI()
    sys.exit(app.exec_())
