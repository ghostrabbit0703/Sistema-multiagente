import mysql.connector


class Basevidauni:
    def __init__(self):
        self.connecion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="vidauni"
        )
        self.cursor=self.connecion.cursor()