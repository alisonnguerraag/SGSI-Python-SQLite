import sqlite3

class Database:
    def __init__(self):
        self.nombre_db = "sgsi.db"
        self.crear_tablas()
        
    def conectar(self):
        return sqlite3.connect(self.nombre_db)
    
    def crear_tablas(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        rol TEXT NOT NULL)
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidentes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        nivel TEXT NOT NULL,
        usuario_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
        """)
        
        conexion.commit()
        conexion.close()
        
    def insertar_usuario(self, username, password, rol):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        try:
            cursor.execute("""
            INSERT INTO usuarios(username, password, rol)
            VALUES (?, ?, ?)
            """, (username, password, rol))
            
            conexion.commit()
            return cursor.lastrowid # aqui esta el id
        
        except:
            print("Error: el usuario ya existe en la base de datos.")
            return None
        
        finally:
            conexion.close()
    
    def buscar_usuario(self, username):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
        SELECT id, username, password, rol
        FROM usuarios
        WHERE username = ?
        """, (username,))
        
        usuario = cursor.fetchone()
        conexion.close()
        
        return usuario
    
    def actualizar_password(self, username, nuevo_password_hash):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
        UPDATE usuarios
        SET password = ?
        WHERE username = ?
        """, (nuevo_password_hash, username))
        
        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()
        
        return filas_afectadas > 0
    
    def insertar_incidente(self, titulo, descripcion, nivel, usuario_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
        INSERT INTO incidentes (titulo, descripcion, nivel, usuario_id)
        VALUES(?, ?, ?, ?)               
        """, (titulo, descripcion, nivel, usuario_id))
        
        conexion.commit()
        id_incidente = cursor.lastrowid
        conexion.close()
        
        return id_incidente
    
    def obtener_incidentes(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
        SELECT i1.id, i1.titulo, i1.descripcion, i1.nivel, u1.username
        FROM incidentes i1
        INNER JOIN usuarios u1 ON i1.usuario_id = u1.id
        """)
        
        incidentes = cursor.fetchall()
        conexion.close()
        
        return incidentes