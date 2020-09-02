# coding=utf-8
from PyQt4.QtGui import QStyle, QStyledItemDelegate, QStyleOptionButton
from Wishlist import QtGui, QtCore

class CheckBoxDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        return None

    def paint(self, painter, option, index):
        checked = index.data().toBool()
        self.check_box_style_option = QStyleOptionButton()

        self.check_box_style_option.state |= QStyle.State_On if checked else QStyle.State_Off

        self.check_box_style_option.rect = self.getCheckBoxRect(option)
        self.check_box_style_option.state |= QtGui.QStyle.State_Enabled
        QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_CheckBox, self.check_box_style_option, painter)

    def editorEvent(self, event, model, option, index):
        if event.type() == QtCore.QEvent.MouseButtonRelease or event.type() == QtCore.QEvent.MouseButtonDblClick:
            if event.button() == QtCore.Qt.RightButton:
                return True
        else:
            return False

        self.setModelData(None, model, index)
        return True

    def setModelData(self, editor, model, index):
        newValue = not index.data().toBool()
        model.setData(index, newValue, QtCore.Qt.EditRole)

    def getCheckBoxRect(self, option):
        check_box_rect = QtGui.QApplication.style().subElementRect(QtGui.QStyle.SE_CheckBoxIndicator,
                                                                   self.check_box_style_option, None)
        check_box_point = QtCore.QPoint(option.rect.x() + option.rect.width() / 2 - check_box_rect.width() / 2,
                                        option.rect.y() + option.rect.height() / 2 - check_box_rect.height() / 2)
        return QtCore.QRect(check_box_point, check_box_rect.size())