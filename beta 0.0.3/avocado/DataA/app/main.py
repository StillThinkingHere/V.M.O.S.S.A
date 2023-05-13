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
        ignore_button.clicked.connect(ignore_button_clicked)

        msg.exec_()
        app.exec_()

    def ok_button_clicked():
        pass

    def ignore_button_clicked():
        root.quit

    if __name__ == '__main__':
        show_popup()


errortype2()
