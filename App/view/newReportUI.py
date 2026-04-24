from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QComboBox, QCalendarWidget
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.uic import loadUi
from App.controller.reportController import ReportController
from App.controller.parentController import ParentController

class NewReportUI(QDialog):
    def __init__(self, studentID,**kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/newReport.ui", self)

        self.studentID = studentID
        self.listParents = ParentController.findParentForStudent(self.studentID)
        self.populateComboBox()

        self.dataOcorrencia.mousePressEvent = displayCalendar()
        self.dataOcorrencia.setCalendarPopup(True)
        self.dataOcorrencia.setDate(QDate.currentDate())

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
    
    def displayCalendar(self):
        self.dataOcorrencia.ShowPopup()
        
    
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
