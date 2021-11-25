import sqlite3
import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect('banco.db') # cria o banco de dados
cursor = connection.cursor() # eele seleciona alguma coisa

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY, \
                nome text, estrela real, diaria real, cidade text)"

criar_hotel = "INSERT INTO hoteis VALUES ('Alpha', 'Alpha Hotel', 4.3, 345.65, 'Rio De Janeiro')"

cursor.execute(criar_tabela)
cursor.execute(criar_hotel)

connection.commit()
connection.close()

