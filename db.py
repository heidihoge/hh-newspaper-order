import shelve
database = shelve.open('hh.data')
productos = None
cantidad_productos = None
cantidad_pedidos = None
pedidos = None
cantidad_devoluciones = None
devoluciones = None
cantidad_reclamos = None
reclamos = None
cantidad_suscripciones = None
suscripciones = None

def guardar(obj, key):
    """
    Guarda un objeto en la base de datos
    :param obj: el objeto a guardar
    :param key: la clave para identificar el objeto
    :return:
    """
    # dumps convierte un objecto a string
    database[key] = obj

def cargar(key, default=None):
    """
    Carga un objeto de la base de datos
    :param key: la clave para identificar el objeto
    :return: el objeto
    """

    # pregunta si existe la clave en la base de datos
    if key in database:
        return database[key]
    return default


def cargar_todo():
    global productos
    productos = cargar('productos', [])
    global cantidad_productos
    cantidad_productos = cargar('cantidad_productos', 0)
    global cantidad_pedidos
    cantidad_pedidos = cargar('cantidad_pedidos', 0)
    global pedidos
    pedidos = cargar('pedidos', [])
    global cantidad_devoluciones
    cantidad_devoluciones = cargar('cantidad_devoluciones', 0)
    global devoluciones
    devoluciones = cargar('devoluciones', [])
    global cantidad_reclamos
    cantidad_reclamos = cargar('cantidad_reclamos', 0)
    global reclamos
    reclamos = cargar('reclamos', [])
    global cantidad_suscripciones
    cantidad_suscripciones = cargar('cantidad_suscripciones', 0)
    global suscripciones
    suscripciones = cargar('suscripciones', [])