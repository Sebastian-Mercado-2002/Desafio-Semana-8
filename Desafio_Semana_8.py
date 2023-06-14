from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono
        self._username = username
        self._email = email
        self._contraseña = contraseña
        self._fecha_registro = fecha_registro
        self._avatar = avatar
        self._estado = "Activo"
        self._online = False

    def login(self):
        self._online = True
        print(f"El usuario {self._username} ha iniciado sesión.")

    def registrar(self):
        print(f"El usuario {self._username} se ha registrado exitosamente.")

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, es_publico=True, avatar=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        self._es_publico = es_publico

    def comentar(self, id_articulo, contenido):
        print(f"El usuario {self._username} ha comentado en el artículo con ID {id_articulo}: {contenido}")

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, es_colaborador=True, avatar=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        self._es_colaborador = es_colaborador

    def comentar(self, id_articulo, contenido):
        print(f"El colaborador {self._username} ha comentado en el artículo con ID {id_articulo}: {contenido}")

    def publicar(self, titulo, resumen, contenido, imagen=None):
        fecha_publicacion = datetime.now()
        estado = "Publicado"
        articulo = Articulo(self._id, titulo, resumen, contenido, fecha_publicacion, imagen, estado)
        print(f"El colaborador {self._username} ha publicado el artículo con título '{titulo}'.")

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen=None, estado="Borrador"):
        self._id = id
        self._id_usuario = id_usuario
        self._titulo = titulo
        self._resumen = resumen
        self._contenido = contenido
        self._fecha_publicacion = fecha_publicacion
        self._imagen = imagen
        self._estado = estado

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado="Aprobado"):
        self._id = id
        self._id_articulo = id_articulo
        self._id_usuario = id_usuario
        self._contenido = contenido
        self._fecha_hora = fecha_hora
        self._estado = estado

opcion = input("¿Desea registrarse (R) o hacer login (L)? ")
if opcion.lower() == "r":
    id = 1
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    username = input("Username: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    fecha_registro = datetime.now()
    avatar = input("Avatar (opcional): ")
    usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
    usuario.registrar()
elif opcion.lower() == "l":
    id = 1
    nombre = "Sebastián"
    apellido = "Mercado"
    telefono = "36441666"
    username = "Seba"
    email = "seba@ejemplo.com"
    contraseña = "mercado2002"
    fecha_registro = datetime.now()
    avatar = "avatar.jpg"
    usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
    usuario.login()

    if isinstance(usuario, Publico):
        id_articulo = 1
        contenido = input("Ingresa tu comentario: ")
        usuario.comentar(id_articulo, contenido)
    elif isinstance(usuario, Colaborador):
        titulo = input("Título del artículo: ")
        resumen = input("Resumen del artículo: ")
        contenido = input("Contenido del artículo: ")
        imagen = input("Imagen (opcional): ")
        usuario.publicar(titulo, resumen, contenido, imagen)
