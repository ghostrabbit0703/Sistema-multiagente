import mysql.connector


class BaseAntecedentes:
    def __init__(self):
        self.connecion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="universitariosantecedentes"
        )
        self.cursor=self.connecion.cursor()