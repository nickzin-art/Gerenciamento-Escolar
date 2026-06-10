from App.model.studentModel import Student
from datetime import datetime
class StudentController:
 
    @classmethod
    def validateRequiredFields(cls, data):
 
        campos_necessarios = ['nome', 'CPF', 'data_nasc', 'RA', 'RM']
        for campo in campos_necessarios:
            if not data.get(campo):
                print(f"Erro: O campo '{campo}' é obrigatório e não pode estar vazio.")
                return False
        return True
 
    @classmethod
    def create(cls, data: dict):
        try:
            data_nasc=data.get("data_nasc")
            data_nasc= datetime.strptime(data_nasc, "%d/%m/%Y")
            if not cls.validateRequiredFields(data):
                return False
           
 
            student = Student(
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data_nasc,
                RA=data.get("RA"),
                RM=data.get("RM"),
                obs=data.get("observacao"),
            )
           
            novo_id = Student.Create(student)
            if novo_id:
                return novo_id
            return False
           
        except Exception as e:
            print(f"Erro no controller ao tentar criar aluno: {e}")
            return False
 
    @classmethod
    def update(cls, id: int, data: dict):
        try:

            data_nasc=data.get("data_nasc")
            data_nasc= datetime.strptime(data_nasc, "%d/%m/%Y")
            student = Student(
                id=id,
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data_nasc,
                RA=data.get("RA"),
                RM=data.get("RM"),
                obs=data.get("observacao"),
                status=data.get("status", True)
            )
 
            result = Student.Update(student)
            return result
           
        except Exception as e:
            print(f"Erro ao atualizar os dados do aluno: {e}")
            return False
 
    @classmethod
    def delete(cls, id: int):
        try:
            return Student.delete(id)
        except Exception as e:
            print(f"Erro no controller ao desativar aluno: {e}")
            return False
    
    @classmethod
    def deleteListStudent(cls , list:list[Student]):
        if not list:
            raise ValueError("A lista deve conter valores validos!")
        for student in list:
            cls.delete(student.id)

    @classmethod
    def activate(cls, id: int):
        try:
            return Student.activate(id)
        except Exception as e:
            print(f"Erro ao ativar aluno: {e}")
            return False
 
    @classmethod
    def getById(cls, id: int):
        try:
            return Student.findById(id)
        except Exception as e:
            print(f"Erro ao buscar aluno por ID: {e}")
            return None
 
    @classmethod
    def getAll(cls):
        try:
            return Student.findAll()
        except Exception as e:
            print(f"Erro ao listar todos os alunos: {e}")
            return []
 
    @classmethod
    def getActive(cls):
        try:
            return Student.findActive()
        except Exception as e:
            print(f"Erro ao listar todos os alunos: {e}")
            return []
        
    @classmethod
    def validateID(cls, value):
        if not isinstance(value, int): raise TypeError(f"ID incorreto")
        if value <= 0: raise ValueError("Id invalido")
        return value
        
    @classmethod
    def getByRoomID(cls, roomID):
        try:
            roomID = StudentController.validateID(roomID)
            lista = Student.findByRoomID(roomID)
            return lista
        except Exception as e:
            raise e
    
    @classmethod
    def linkStudentToClassroom(cls, student_id, room_id):
        try:
            if not student_id or not room_id:
                return {" PREENCHA TODOS CAMPOS OBRIGATÓRIOS "}
            Student.linkStudentInClassroom(student_id, room_id)

        except Exception as e:
            print(f"Erro ao inserir aluno: {e}")
            return []
        
    @classmethod
    def linkListStudentsToClassroom(cls, students:Student , roomId):
        if not students or roomId < 1:
            return ("Preencha os dados necessários")
        for student in students:
            Student.linkStudentInClassroom(student.id , roomId)
    
    @classmethod
    def deleteListStudent(cls , list:list[Student]):
        if not list:
            raise ValueError("A lista deve conter valores validos!")
        for student in list:
            cls.delete(student.id)

    @classmethod
    def searchStudent(cls, search):
        try:
            if not search:
                return ("Insira uma informação valida!")
            lista = Student.searchStudent(search)
            return lista
        except Exception as e:
            print(f"Erro ao buscar Aluno: ")
            raise e

        
if __name__ == "__main__":
    # aluno = StudentController.getById(5)
    # print(aluno.nome)
    # print('-'*50)

    # alunos = StudentController.getAll()
    # print(alunos[4].nome)

    # print('-'*50)
    alunos_sala = StudentController.getByRoomID(3)
    StudentController.deleteListStudent(alunos_sala[:3])



    # print('-'*50)
    # alunos_ativos = StudentController.getActive()
    # print(alunos_ativos[5].nome)

    # u = StudentController.searchStudent("ana")
    # print(u)