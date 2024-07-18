import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('games.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar la consulta
cursor.execute("SELECT * FROM location")

# Obtener todas las filas
rows = cursor.fetchall()

# Iterar y mostrar las filas
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
