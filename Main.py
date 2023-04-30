from PySide2.QtWidgets import QApplication
import Member_Managing
import UI_Loading

#Data

#UI
app = QApplication([])
main_window=UI_Loading.Main_Window()
main_window.ui.show()
app.exec_()