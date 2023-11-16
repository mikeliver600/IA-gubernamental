import sqlite3
import datetime

class RecolectorDatos:
    def __init__(self):
        self.datos_recolectados = []

    def recolectar_datos(self, modulo, detalles):
        # Recolecta datos de diferentes módulos
        datos = {
            'modulo': modulo,
            'detalles': detalles,
            'timestamp': str(datetime.datetime.now())
        }
        self.datos_recolectados.append(datos)

    def guardar_datos_en_base_de_datos(self):
        # Crea una conexión a la base de datos SQLite
        connection = sqlite3.connect('datos_ia_supervivencia.db')

        # Crea una tabla para almacenar los datos recolectados
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS datos_recolectados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modulo TEXT,
                detalles TEXT,
                timestamp TEXT
            )
        ''')

        # Inserta los datos recolectados en la base de datos
        for datos in self.datos_recolectados:
            cursor.execute('''
                INSERT INTO datos_recolectados (modulo, detalles, timestamp)
                VALUES (?, ?, ?)
            ''', (datos['modulo'], str(datos['detalles']), datos['timestamp']))

        # Guarda los cambios y cierra la conexión
        connection.commit()
        connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    ia_supervivencia = IASupervivencia()
    recolector = RecolectorDatos()

    # Simulación de módulo de economía
    modulo_economia = ModuloEconomia()
    modulo_economia.gestionar_recursos_financieros()
    modulo_economia.desarrollar_estrategias_economicas()
    modulo_economia.comerciar_con_otras_naciones()
    recolector.recolectar_datos('Economía', modulo_economia)

    # Simulación de módulo de tecnología
    modulo_tecnologia = ModuloTecnologia()
    modulo_tecnologia.investigar_desarrollar_tecnologia()
    modulo_tecnologia.mejorar_capacidades()
    modulo_tecnologia.gestionar_infraestructura_tecnologica()
    recolector.recolectar_datos('Tecnología', modulo_tecnologia)

    # Guardar los datos recolectados en la base de datos
    recolector.guardar_datos_en_base_de_datos()
