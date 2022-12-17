import mysql.connector

class BaseAcademico:
    def __init__(self):
        self.connecion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="base_academico"
        )
        self.cursor=self.connecion.cursor()

