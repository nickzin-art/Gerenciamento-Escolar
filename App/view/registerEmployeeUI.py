from PyQt5.QtWidgets import QDialog, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.userController import UserController

class RegisterEmployeeUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/registerEmployee.ui", self)
        self.funcionario: QComboBox

    def clearText(self):
        self.nome.clear()
        self.login.clear()
        self.senha.clear()
        self.confirmar_senha.clear()
        self.funcionario.setCurrentIndex(0)

    def validarCampos(self):
        nome = self.nome.text()
        login = self.login.text()
        senha = self.senha.text()
        confirmar_senha = self.confirmar_senha.text()
        funcionario = self.funcionario.currentText()


        if not nome and not login and not senha:
            print(f'Preencha os campos!')
            return

        if senha != confirmar_senha:
            print(f'As senhas são diferentes!')
            return
        return {
            "name": nome,
            "email": login,
            "password": senha,
            "type": funcionario
        }

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        user = self.validarCampos()

        if user:
            print(user)
            try:
                UserController.createUser(user)
                self.clearText()
            except Exception as e:
                print(f"Erro: \n{e}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterEmployeeUI()
    app.exec_()