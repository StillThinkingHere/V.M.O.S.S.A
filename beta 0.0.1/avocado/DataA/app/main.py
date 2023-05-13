from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import shutil


def show_popup():
    app = QtWidgets.QApplication([])
    msg = QMessageBox()
    msg.setWindowTitle("Avocado")
    msg.setText("This is the main text!")
    msg.setIcon(QMessageBox.Question)

    # Set the buttons and their values
    uninstall_button = msg.addButton("Uninstall", QMessageBox.DestructiveRole)
    ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

    msg.setDefaultButton(uninstall_button)
    msg.setInformativeText("Please press the details button!")
    msg.setDetailedText(
        "The program was not successful, please try again. Please try to uninstall the package using the uninstall button below, and reinstall the package")

    # Connect the buttons to their corresponding functions
    uninstall_button.clicked.connect(uninstall_button_clicked)
    ignore_button.clicked.connect(ignore_button_clicked)

    msg.exec_()
    app.exec_()


file_path1 = 'file-handel.py'
file_path2 = 'starter.py'
folder_path1 = 'Pits'
folder_path2 = 'poper'
folder_path3 = 'SF'


def uninstall_button_clicked():
    shutil.rmtree(folder_path1)
    shutil.rmtree(folder_path2)
    shutil.rmtree(folder_path3)
    os.remove(file_path1)
    os.remove(file_path2)


def ignore_button_clicked():
    print("Ignore button clicked")


def details_button_clicked():
    print("Details button clicked")


if __name__ == '__main__':
    show_popup()
