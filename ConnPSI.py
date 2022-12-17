import mysql.connector


class BasePsico:
    def __init__(self):
        self.connecion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="psicouni_v2"
        )
        self.cursor=self.connecion.cursor()