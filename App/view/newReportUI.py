from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.uic import loadUi
from App.controller.reportController import ReportController
from App.controller.parentController import ParentController
from App.view.ui.imagens import imagens

class NewReportUI(QDialog):
    def __init__(self, studentID,**kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/newReport.ui", self)

        self.studentID = studentID
        self.listParents = ParentController.findParentForStudent(self.studentID)
        self.populateComboBox()

        self.dataOcorrencia.setCalendarPopup(True)
        self.dataOcorrencia.setDate(QDate.currentDate())

        try:
            cal = self.dataOcorrencia.calendarWidget()

            cal.setStyleSheet("""
                QCalendarWidget {
                    background-color: #F7F9FF;
                    border: 1px solid #D6DCF5;
                    border-radius: 12px;
                    padding: 6px;
                }

                QCalendarWidget QWidget {
                    background-color: #5B6EE9;
                }

                QCalendarWidget QToolButton {
                    background-color: transparent;
                    color: white;
                    border: none;
                    font-weight: 600;
                    padding: 6px;
                }

                QCalendarWidget QToolButton:hover {
                    background-color: rgba(255, 255, 255, 0.15);
                    border-radius: 6px;
                }

                QCalendarWidget QToolButton::menu-indicator {
                    image: none;
                }

                QCalendarWidget QAbstractItemView {
                    background-color: white;
                    color: #2c3e50;  /* <<< ISSO FAZ OS NÚMEROS APARECEREM */
                    selection-background-color: #5B6EE9;
                    selection-color: white;
                    gridline-color: #E6EAF5;
                    outline: 0;
                }

                QCalendarWidget QHeaderView::section {
                    background-color: #EEF2FF;
                    color: #2c3e50;  /* <<< ISSO FAZ APARECER OS NOMES */
                    padding: 6px;
                    border: none;
                    font-weight: 600;
                }

                QCalendarWidget QAbstractItemView::item {
                    color: #2c3e50; /* reforço de legibilidade */
                }

                QCalendarWidget QAbstractItemView::item:hover {
                    background-color: #E9EDFF;
                    border-radius: 6px;
                }
                """)
        except Exception:
            pass

        self.btnSaveReport.clicked.connect(self.sendReport)
        
        self.show()
    
    def getInfo(self):
        info = []
        desc = self.descricaoOcorrencia.toPlainText()
        indexResp = self.responsavelCombo.currentIndex()
        parentID = self.listParents[indexResp].id

        name = self.nomeOcorrencia.text()
        date = self.dataOcorrencia.text()
        
        return {
            "description": desc, 
            "parentID": parentID, 
            "name": name,
            "date": date
        }
    
    def sendReport(self):
        try:
            info = self.getInfo()
            ReportController.create(info['description'], self.studentID, info['parentID']) 
        except Exception as e:
            print(f"Erro ao criar o relatório! {e}")

    def populateComboBox(self):
        try:
            for parent in self.listParents:
                self.responsavelCombo.addItem(parent.name)
        except Exception as e:
            print(f"{e}")

    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = NewReportUI(studentID=10)
    app.exec_()
