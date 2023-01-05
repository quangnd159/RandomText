import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QComboBox, QInputDialog
import json

# Load the JSON data from the file
with open('texts.json', 'r') as f:
    data = json.load(f)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Text edit to input the text
        self.textEdit = QLineEdit(self)

        # Combo box to select a set of data
        self.setComboBox = QComboBox(self)
        self.setComboBox.addItems(data.keys())
        # Button to add a new set of data
        self.newSetButton = QPushButton('New Set', self)
        self.newSetButton.clicked.connect(self.addSet)

        # Button to add the text to the selected set
        self.addButton = QPushButton('Add', self)
        self.addButton.clicked.connect(self.addText)

        # Layout to arrange the widgets
        layout = QHBoxLayout(self)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.setComboBox)
        layout.addWidget(self.newSetButton)
        layout.addWidget(self.addButton)

    def addSet(self):
        # Show an input dialog to enter the name of the new set
        setName, ok = QInputDialog.getText(self, 'New Set', 'Enter set name:')
        if ok:
            # Add the new set to the JSON data
            data[setName] = []
            # Update the combo box
            self.setComboBox.addItem(setName)
            # Save the JSON data to the file
            with open('texts.json', 'w') as f:
                json.dump(data, f, indent=2)

    def addText(self):
        # Get the input text and the selected set of data
        text = self.textEdit.text()
        textSet = data[self.setComboBox.currentText()]
        # Add the text to the set
        textSet.append(text)
        # Update the JSON data
        data[self.setComboBox.currentText()] = textSet
        # Save the JSON data to the file
        with open('texts.json', 'w') as f:
            json.dump(data, f, indent=2)
        # Clear the text edit
        self.textEdit.clear()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
