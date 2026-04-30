import hashlib
from usuario import Usuario
from incidente import Incidente
from database import Database

class SistemaSGSI:
    def __init__(self):
        self.incidentes = []
        self.usuario_actual = None
        self.contador_incidentes = 1
        self.db = Database()
        
    def generar_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validar_password(self, password):
        tiene_letra = any(caracter.isalpha() for caracter in password)
        tiene_numero = any(caracter.isdigit() for caracter in password)
        
        if len(password) < 8 :
            print("El password debe de tener minimo 8 caracteres")
            return False
          
        if not tiene_letra:
            print("El password debe incluir al menos una letra")
            return False
        
        if not tiene_numero:
            print("El password debe incluir al menos un numero")
            return False
        
        return True
    
    def registrar_usuario(self):
        print("\nCreacion tu usuario.")
        
        username = input("Username: ")
        if username == "":
            print("El username no puede estar vacio")
            return None
        
        password = input("Password: ")
        
        if not self.validar_password(password):
            return None
        
        rol = input("Rol: ")
                
        password_hash = self.generar_hash(password)
                
        id_usuario = self.db.insertar_usuario(username, password_hash, rol)
        
        if id_usuario is None:
            return None
        
        print("Usuario creado exitosamente")
        
        usuario = Usuario(username, password_hash, rol, id_usuario)
        return usuario
    
    def iniciar_sesion(self):
        print("\nInicio de sesion.")
        username = input("Username: ")
        password = input("Password: ")
        
        password_hash = self.generar_hash(password)
        
        usuario_db = self.db.buscar_usuario(username)
        
        if usuario_db is not None:
            id_usuario, username_db, password_db, rol_db = usuario_db
            
            if password_hash == password_db:
                print("Inicio de sesion exitoso")
        
                self.usuario_actual = Usuario(username_db, password_db, rol_db, id_usuario)
                return self.usuario_actual
        
        print("Usuario y/o contrasenia incorrectos")
        return None
    
    def cambio_contrasena(self):
        print("\nCambio de contraseña.")
        username = input("Username: ")
        password_actual = input("Ingresa password actual: ")
        
        password_actual_hash = self.generar_hash(password_actual)
        
        usuario_db = self.db.buscar_usuario(username)
        
        if usuario_db is None:
            print("Usuario o password incorrecto.")
            return None
            
        id_usuario, username_db, password_db, rol_db = usuario_db
        
        password_actual_hash = self.generar_hash(password_actual)
        
        if password_actual_hash != password_db:
            print("Usuario o password incorrecto.")
            return None
        
        password_nueva = input("Ingresa nuevo password: ")
        
        if not self.validar_password(password_nueva):
            return None
        
        nuevo_password_hash = self.generar_hash(password_nueva)
        
        actualizado = self.db.actualizar_password(username, nuevo_password_hash)
        
        if actualizado:
            print("Password actualizado correctamente")
            return True
        
        print("No se pudo actualizar el password")
        return None
    
    def registrar_incidente(self):
        if self.usuario_actual is None:
            print("Primero debes iniciar sesión.")
            return None
        
        print("\nRegistro de incidente.")
        
        titulo = input("Titulo: \n")
        descripcion = input("Descripcion: \n")
        nivel = input("Nivel de riesgo: (Alto, Medio, Bajo): ")
        
        id_incidente = self.db.insertar_incidente(titulo, descripcion, nivel, self.usuario_actual.id)
        
        incidente = Incidente(id_incidente, titulo, descripcion, nivel, self.usuario_actual)
        
        print("\nIncidente registrado correctamente")
        return incidente
    
    def ver_reporte(self):
        if self.usuario_actual is None:
            print("Primero debes iniciar sesion para ver reportes")
            return None
        
        incidentes = self.db.obtener_incidentes()
        
        if len(incidentes) == 0:
            print("No hay incidentes registrados")
            return None
        
        print("\nReporte de incidentes:")
        for incidente in incidentes:
            id_incidente, titulo, descripcion, nivel, username = incidente
            
            print("\n---------------------------")
            print(f"ID: {id_incidente}")
            print(f"Titulo: {titulo}")
            print(f"Descripcion: {descripcion}")
            print(f"Nivel: {nivel}")
            print(f"Reportado por: {username}")  
            
    def menu(self):
        while True:
            print("\nMenu de opciones:")
            print("1. Registrar")
            print("2. Iniciar sesion")
            print("3. Cambiar contraseña")
            print("4. Registrar incidente")
            print("5. Ver reporte de incidentes")
            print("6. Salir")
            opcion = input("Seleccione una opcion: ")
            
            match opcion:
                case "1":
                    self.registrar_usuario()
                case "2":
                    self.iniciar_sesion()
                case "3":
                    self.cambio_contrasena()
                case "4":
                    self.registrar_incidente()
                case "5":
                    self.ver_reporte()
                case "6":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opcion invalida")
