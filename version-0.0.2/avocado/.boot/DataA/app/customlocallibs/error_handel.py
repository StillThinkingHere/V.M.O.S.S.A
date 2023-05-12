from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

def errortype2():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("Something went wrong!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program is moving critical data from memory to cash if you continue the program might be corrupted and not work properly")

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)

    def ok_button_clicked():
        pass
    show_popup()


def errortype3():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("Something went wrong!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program is not finding the json files!")

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)

    def ok_button_clicked():
        pass

    show_popup()


def errortype4():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("Something went wrong!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program is not finding the cashe files!")

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)

    def ok_button_clicked():
        pass

    show_popup()


def errortypecustom(title: str = "default", text: str = "default", details: str = "default"):
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(details)

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)

    def ok_button_clicked():
        pass
    show_popup()