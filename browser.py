import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the web view
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl('https://www.duckduckgo.com'))

        # Set up the layout
        layout = QHBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        # Set up the window
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('AZOS Browser')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
