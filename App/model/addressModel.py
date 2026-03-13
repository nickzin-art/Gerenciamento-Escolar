from App.config.database import Database

class Address:

    id = None
    city = ""
    neighborhood = ""
    street = ""
    complement = ""
    responsible_id = None

    def __init__(self, id=None, city="", neighborhood="", street="", complement="", responsible_id=None ):
        
        self.id = id
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.complement = complement
        self.responsible_id = responsible_id

    def create(self):
        # INSERIR NOVO ENDEREÇO
        pass

    @classmethod
    def updateAddress(cls):

        try:
            DB = Database()
            sql = """
            UPDATE enderecos
            SET cidade = %s,
                bairro = %s,
                rua = %s,
                complemento = %s
                WHERE responsavel_id = %s
            """

            params = (
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.responsible_id
                )

            DB.execute(sql, params)
            print("Atualização feita!")
        
        except Exception as e:
            print("Não foi possível atualizar:", e)
            raise RuntimeError("Falha ao atualizar o endereço!") from e
      

        

        
        
        
    @classmethod
    def read(cls):
        # CONSULTAR ENDEREÇO ATRAVÉS DO RESPONSAVEL

        try:
            DB = Database()
            sql = """SELECT cidade, bairro, rua, complemento
                FROM enderecos
                WHERE responsavel_id = %s;
            """
            params = (address.responsible_id,)
            result = DB.fetchOne(sql, params)
            
            print("Seleção feita!")
            print(result)

        except Exception as e:
            print("Não foi possível selecionar:", e)
            raise RuntimeError("Falha ao selecionar o endereço!") from e

            
        

    def delete(self):
        #DELETAR ENDEREÇO
        pass

    def adressforResponsible(self, responsible):
        #CONSULTAR ENDEREÇO PELO RESPONSAVEL
        pass

    def adressforStudent(self, student):
        #CONSULTAR ENDEREÇO PELO ALUNO
        pass


if __name__ == "__main__":
    address = Address(
        responsible_id=1,     
        city="Toquio",
        neighborhood="Bairro Nada",
        street="Rua Sushi",
        complement="Nada"
    )

    address.read()