import db
from models import *

def eliminar(codigos, tabla):
    """
    Elimina objetos de la tabla
    :param codigos: <list> lista de codigos a eliminar
    :param tabla: <str> nombre de la tabla
    :return:
    """
    lista = db.cargar(tabla, [])
    lista_nueva = filter(lambda obj: obj.get_codigo() not in codigos, lista)
    db.guardar(lista_nueva, tabla)


def guardar(obj, tabla):
    """
    Guarda un objeto a la tabla.
    Si ya existe, lo reemplaza
    :param obj: <model> objeto a guardar
    :param tabla: <str> nombre de la tabla
    :return: True en caso de exito, False en caso de Falla
    """
    try:
        codigo = int(obj.get_codigo())
    except:
        return False

    lista = db.cargar(tabla, [])
    objetos = filter(lambda obj: obj.get_codigo() == codigo, lista)
    if len(objetos) >= 1:
        # el objeto ya existe. Modificar
        objeto = objetos[0]
        # Quita el objeto desactualizado
        lista.remove(objeto)

    # Agrega objeto a la lista
    lista.append(obj)

    db.guardar(lista, tabla)
    return True
