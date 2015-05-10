# -*- coding: utf-8 -*-

# x pedidos.
# x devoluciones.
# x distribuidores.
# x supervisores.
# x producto.
# x reclamos.


class Distribuidor:
    def __init__(self, cod=None, ruc=None, nombre=None, direccion=None, supervisor=None):
        self.__cod = cod
        self.__ruc = ruc
        self.__nombre = nombre
        self.__direccion = direccion
        self.__supervisor = supervisor

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_ruc(self):
        return self.__ruc

    def set_ruc(self, ruc):
        self.__ruc = ruc

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor


class Pedido:
    def __init__(self, cod=None, fecha_publicacion=None, producto=None, cantidad=None):
        self.__cod = cod
        self.__fecha_publicacion = fecha_publicacion
        self.__producto = producto
        self.__cantidad = cantidad

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def get_producto(self):
        return self.__producto

    def set_producto(self, producto):
        self.__producto = producto

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad


class Supervisor:
    def __init__(self, cod, nombre):
        self.__cod = cod
        self.__nombre = nombre

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


class Producto:
    def __init__(self, cod=None, fecha_publicacion=None, nombre=None, descripcion=None, precio_venta=None):
        self.__cod = cod
        self.__fecha_publicacion = fecha_publicacion
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_venta = precio_venta

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_precio_venta(self):
        return self.__precio_venta

    def set_precio_venta(self, precio_venta):
        self.__precio_venta = precio_venta


class Devoluciones:
    def __init__(self, pedido=None, cantidad=None, fecha_devolucion=None, cod=None):
        self.__pedido = pedido
        self.__cantidad = cantidad
        self.__fecha_devolucion = fecha_devolucion
        self.__cod = cod

    def get_pedido(self):
        return self.__pedido

    def set_pedido(self, pedido):
        self.__pedido = pedido

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod


class Reclamos:
    def __init__(self, fecha_reclamo=None, asunto=None, distribuidor=None, respuesta=None, supervisor=None):
        self.__fecha_reclamo = fecha_reclamo
        self.__asunto = asunto
        self.__respuesta = respuesta
        self.__distribuidor = distribuidor
        self.__supervisor = supervisor

    def get_fecha_reclamo(self):
        return self.__fecha_reclamo

    def set_fecha_reclamo(self, fecha_reclamo):
        self.__fecha_reclamo = fecha_reclamo

    def get_asunto(self):
        return self.__asunto

    def set_asunto(self, asunto):
        self.__asunto = asunto

    def get_distribuidor(self):
        return self.__distribuidor

    def set_distribuidor(self, distribuidor):
        self.__distribuidor = distribuidor

    def get_respuesta(self):
        return self.__respuesta

    def set_respuesta(self, respuesta):
        self.__respuesta = respuesta

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor


class ProductoRevista(Producto):
    def __init__(self, cod=None, fecha_publicacion=None, nombre=None, descripcion=None,  valor_agregado=None):
        Producto.__init__(self, cod=cod, fecha_publicacion=fecha_publicacion, nombre=nombre, descripcion=descripcion)
        self.__valor_agregado = valor_agregado
  
    def get_valor_agregado(self):
        return self.__valor_agregado

    def set_valor_agregado(self, valor_agregado):
        self.__valor_agregado = valor_agregado
