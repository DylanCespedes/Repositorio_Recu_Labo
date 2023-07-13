import sqlite3

conectar = sqlite3.connect('puntaje_jugadores.db')
cursor = conectar.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS puntaje_jugadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    jugador TEXT,
                    puntaje INTEGER
                )''')


def insertar_puntaje(jugador, puntaje):
    cursor.execute("INSERT INTO puntaje_jugadores (jugador, puntaje) VALUES (?, ?)", (jugador, puntaje))
    conectar.commit()

def obtener_puntaje():
    conexion = sqlite3.connect('puntaje_jugadores.db')
    cursor = conexion.cursor()
    
    cursor.execute("SELECT jugador, puntaje FROM puntaje_jugadores ORDER BY puntaje DESC LIMIT 5")
    puntajes = cursor.fetchall()

    conexion.close()

    return puntajes

puntajes = obtener_puntaje()