from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.parentController import ParentController


from App.controller.parentController import ParentController 
 
class ReportCardUI(QDialog):
    def __init__(self, report, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/reportCard.ui", self)
        self.show()
        self.report = report
       
        self.dateLabel.setText(str(self.report.date.strftime("%d/%m/%Y")))
        self.descLabel.setText(self.report.description)
        parent = ParentController.findParentId(self.report.parentID)

        self.respLabel.setText(parent.name)
        
    # def getNameParent(se)
 

    
        


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ReportCardUI(3)
    app.exec_()