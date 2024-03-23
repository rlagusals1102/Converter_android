from PySide6.QtWidgets import QApplication
from converter import Converter

app = QApplication([])
window = Converter()
window.setFixedSize(500, 300)
window.show()
app.exec()
