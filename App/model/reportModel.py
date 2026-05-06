from __future__ import annotations
from dataclasses import dataclass
from App.config.database import Database
from datetime import datetime
@dataclass
class Report:
    id: int = None
    date: str = datetime.now()
    description: str = ""
    studentID: int = ""  
    parentID: int = ""
    
    @classmethod
    def create(cls, report:Report):
        try:
            DB = Database()
            sql = "INSERT INTO `relatorios`(`data`, `descricao`, `aluno_id`, `responsavel_id`) VALUES (%s,%s,%s, %s)"
            params = (report.date, report.description, report.studentID, report.parentID)
            DB.insert(sql, params)
            print("Relatório criado com sucesso")
        except Exception as e:
            print(f'Erro relatorio: {e}')
            raise RuntimeError
 
    @classmethod
    def edit(cls, report: Report) -> Report:
        try:
            DB = Database()
            sql = "UPDATE relatorios SET descricao = %s WHERE id = %s"
            params = (report.description, report.id)
            sucesso = DB.execute(sql, params)
            
            if not sucesso:
                raise Exception(f"Relatório com ID {report.id} não encontrado.")
            return cls.searchUnique(report.id)
            
        except Exception as e:
            print(f"Erro ao editar e retornar: {e}")
            raise e

        
    @classmethod
    def searchUnique(cls, id):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql, params)
            if result: 
                return cls._getObjectList([result])[0]
            return cls()
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError
        
    @classmethod
    def searchDate(cls, date):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE data = %s"
            params= (date,)
            result = DB.fetchAll(sql, params)
            return cls._getObjectList(result)
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError
        
    @classmethod
    def searchParentID(cls, parentID):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE responsavel_id = %s"
            params = (parentID,)
            result = DB.fetchAll(sql, params)
            if result: 
                return cls._getObjectList(result)
            return cls()
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError
    
    @classmethod
    def searchStudentID(cls, studentID):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE aluno_id = %s"
            params = (studentID,)
            result = DB.fetchAll(sql, params)
            if result: 
                return cls._getObjectList(result)
            return cls()
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError
       
    @classmethod
    def searchIntervalDate(cls, initialDate, lastDate):
        try:
            DB = Database()
            sql = "SELECT id, data, descricao, aluno_id, responsavel_id FROM relatorios WHERE data BETWEEN %s AND %s"
            params = (initialDate, lastDate)
            result = DB.fetchAll(sql, params)
            return cls._getObjectList(result)
        except Exception as e:
            print(f'Erro ao buscar relatorios')
            raise RuntimeError

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*item.values()) for item in lista]
    
    @classmethod
    def getAll(cls):
        DB = Database()
        sql = "SELECT * FROM relatorios"
        result = DB.fetchAll(sql)
        return cls._getObjectList(result)
 
if __name__ == "__main__":

    c = Report.searchStudentID(3)

    print(c)
    #relatorio_para_editar = Report(id=7, description="Descrição atualizada com sucesso")
    #Report.edit(relatorio_para_editar)
    #print(relatorio_para_editar)
