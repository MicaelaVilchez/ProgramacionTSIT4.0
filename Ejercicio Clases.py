
class Curso:
    def __init__(self, fecha_inicio, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado):
        self.fecha_inicio = fecha_inicio
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado
        self.clases = []

class Categoria:
    def __init__(self, inicial, intermedio, avanzado):
        self.inicial = inicial
        self.intermedio = intermedio
        self.avanzado = avanzado

class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive

        def get_fecha(self):
            return self.__fecha
        def set_fecha(self, fecha):
            self.__fecha = fecha
        def get_titulo(self):
            return self.__titulo
        def set_titulo(self, titulo):
            self.__titulo = titulo
        def get_contenido(self):
            return self.__contenido
        def set_contenido(self, contenido):
            self.__contenido= contenido
        def get_url_drive(self):
            return self.__url_drive
        def set_url_drive(self, url_drive):
            self.__url_drive = url_drive

    def imprimir_datos(self):
        print(f"Fecha: {self.get_fecha()}")
        print(f"Título: {self.get_titulo()}")
        print(f"Contenido: {self.get_contenido()}")
        print(f"URLDrive: {self.get_url_drive()}")

class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.cursos_dictados = []
        self.clases_dictadas = []

class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave = clave
        self.estado = "Inactivo"  
        self.cursos_inscriptos = []


class Administrador(UsuarioFinal):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave)
        self.estado = "Activo"

class MedioPago:
    def __init__(self, tipo, datos):
        self.tipo = tipo
        self.datos = datos

class Compra:
    def __init__(self, usuario, cursos, medio_pago, monto_total):
        self.usuario = usuario
        self.cursos = cursos
        self.medio_pago = medio_pago
        self.monto_total = monto_total
        self.fecha_compra = None  

print(Curso, Categoria)