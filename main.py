# coding=utf-8
from PyQt4.QtGui import QApplication, QMainWindow, QWidget
from PyQt4.QtSql import QSqlTableModel, QSqlDatabase
from Wishlist import Ui_MainWindow
from CheckBoxDelegate import CheckBoxDelegate
import sys

db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName("127.0.0.1")
db.setDatabaseName("wishlist")
db.setUserName("root")
db.setPassword("newrootpassword")
ok = db.open()

if not ok:
    print unicode(db.lastError().text())
else:
    print "connected"


class MyWin(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = QSqlTableModel()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setTable("Wishlist")
        self.model.setHeaderData(2, 1, "")
        self.model.select()

        self.table = self.ui.tableView
        self.table.setModel(self.model)
        self.table.hideColumn(0)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnWidth(1, 620)
        self.table.setColumnWidth(2, 29)
        self.table.setItemDelegateForColumn(2, CheckBoxDelegate())
        self.ui.addRowButton.clicked.connect(self.addRow)
        self.ui.deleteRowButton.clicked.connect(self.deleteRow)

        self.show()

    def addRow(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row, 1), "")
        self.model.submitAll()


    def deleteRow(self):
        row = self.table.currentIndex().row()
        self.model.removeRow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWin()
    w.setWindowTitle('Wishlist')
    sys.exit(app.exec_())
