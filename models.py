# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from datetime import date
from dateutil.relativedelta import relativedelta
import db


class Producto:
    def __init__(self, precio=None):
        db.cargar_todo()
        self.__codigo = db.cantidad_productos
        db.guardar(db.cantidad_productos+1, 'cantidad_productos')
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        string = 'Codigo: ' + str(self.get_codigo())
        string += ' Precio: ' + str(self.get_precio())
        return string


class Publicacion:
    def __init__(self, fecha_publicacion=None):
        self.__fecha_publicacion = fecha_publicacion

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion


class Persona:
    def __init__(self, codigo=None, nombre=None, direccion=None, telefono=None,
                 email=None, razon_social=None, ruc=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__razon_social = razon_social
        self.__ruc = ruc

    def get_codigo(self):
        return self.__codigo

    def set_(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_razon_social(self):
        return self.__razon_social

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_ruc(self):
        return self.__ruc

    def set_ruc(self, ruc):
        self.__ruc = ruc

    def __str__(self):
        string = ' Codigo: ' + str(self.get_codigo())
        string += ' Nombre: ' + str(self.get_nombre())
        string += ' Direccion: ' + str(self.get_direccion())
        string += ' Telefono: ' + str(self.get_telefono())
        string += ' Email: ' + str(self.get_email())
        string += ' Razon social: ' + str(self.get_razon_social())
        string += ' RUC: ' + str(self.get_ruc())
        return string

class Cliente(Persona):
    # __metaclass__ = ABCMeta

    def __init__(self, codigo=None, nombre=None, direccion=None,
                 telefono=None, email=None, razon_social=None, ruc=None):
        Persona.__init__(self, codigo, nombre, direccion, telefono, email, razon_social, ruc)

    @abstractmethod
    def realizar_reclamo(self, asunto, contenido):
        pass

class Aceptable:
    def __init__(self, aceptado=False):
        self.__aceptado = aceptado

    def get_aceptado(self):
        return self.__aceptado

    def set_aceptado(self, aceptado):
        self.__aceptado = aceptado


class Reclamo:
    def __init__(self, codigo=None, cliente=None, supervisor=None,
                 asunto=None, contenido=None, fecha_reclamo=None, fecha_atendido=None):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__supervisor = supervisor
        self.__asunto = asunto
        self.__contenido = contenido
        self.__fecha_reclamo = fecha_reclamo
        self.__fecha_atendido = fecha_atendido

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor

    def get_asunto(self):
        return self.__asunto

    def set_asunto(self, asunto):
        self.__asunto = asunto

    def get_contenido(self):
        return self.__contenido

    def set_contenido(self, contenido):
        self.__contenido = contenido

    def get_fecha_reclamo(self):
        return self.__fecha_reclamo

    def set_fecha_reclamo(self, fecha_reclamo):
        self.__fecha_reclamo = fecha_reclamo

    def get_fecha_atendido(self):
        return self.__fecha_atendido

    def set_fecha_atendido(self, fecha_atendido):
        self.__fecha_atendido = fecha_atendido


class Supervisor(Persona):
    def __init__(self, codigo=None, nombre=None, direccion=None, telefono=None, email=None,
                 razon_social=None, ruc=None):
        Persona.__init__(self, codigo, nombre, direccion, telefono, email, razon_social, ruc)

    @staticmethod
    def supervisar(aceptable, aceptado):
        aceptable.set_aceptado(aceptado)
        return aceptable

    @staticmethod
    def atender_reclamo(reclamo):
        reclamo.set_fecha_atendido(date.today())
        return reclamo

    def __str__(self):
        string = Persona.__str__(self)
        return string


class Supervisado:
    def __init__(self, supervisor=None):
        self.__supervisor = supervisor

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor


class Pedido(Aceptable):
    def __init__(self, aceptado=False, codigo=None, fecha_pedido=None, publicacion=None, cantidad=None,
                 distribuidor=None, supervisor=None, monto_total=None):
        Aceptable.__init__(self, aceptado)
        self.__codigo = codigo
        self.__fecha_pedido = fecha_pedido
        self.__publicacion = publicacion
        self.__cantidad = cantidad
        self.__distribuidor = distribuidor
        self.__supervisor = supervisor
        self.__monto_total = monto_total

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_fecha_pedido(self):
        return self.__fecha_pedido

    def set_fecha_pedido(self, fecha_pedido):
        self.__fecha_pedido = fecha_pedido

    def get_publicacion(self):
        return self.__publicacion

    def set_publicacion(self, publicacion):
        self.__publicacion = publicacion

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_distribuidor(self):
        return self.__distribuidor

    def set_distribuidor(self, distribuidor):
        self.__distribuidor = distribuidor

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor

    def get_monto_total(self):
        return self.__monto_total

    def set_monto_total(self, monto_total):
        self.__monto_total = monto_total


class Devolucion:
    def __init__(self, codigo, publicacion, fecha_devolucion, cantidad, distribuidor):
        self.__codigo = codigo
        self.__publicacion = publicacion
        self.__fecha_devolucion = fecha_devolucion
        self.__cantidad = cantidad
        self.__distribuidor = distribuidor

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_publicacion(self):
        return self.__publicacion

    def set_publicacion(self, publicacion):
        self.__publicacion = publicacion

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_distribuidor(self):
        return self.__distribuidor

    def set_distribuidor(self, distribuidor):
        self.__distribuidor = distribuidor


class ClienteDistribuidor(Cliente, Supervisado):
    def __init__(self, codigo=None, nombre=None, direccion=None, telefono=None, email=None, razon_social=None, ruc=None,
                 supervisor=None, antiguedad=None, descuento=None):
        Cliente.__init__(self, codigo, nombre, direccion, telefono, email, razon_social, ruc)
        Supervisado.__init__(self, supervisor)
        self.__antiguedad = antiguedad
        self.__descuento = descuento

    def get_antiguedad(self):
        return self.__antiguedad

    def set_antiguedad(self, antiguedad):
        self.__antiguedad = antiguedad

    def get_descuento(self):
        return self.__descuento

    def set_descuento(self, descuento):
        self.__descuento = descuento

    def realizar_pedido(self, publicacion, cantidad):
        db.cantidad_pedidos += 1
        nuevo_pedido = Pedido(codigo=db.cantidad_pedidos, fecha_pedido=1, publicacion=publicacion,
                              cantidad=cantidad, distribuidor=self, supervisor=self.get_supervisor())
        db.pedidos.append(nuevo_pedido)
        return nuevo_pedido

    def realizar_devolucion(self, publicacion, cantidad):
        db.cantidad_devoluciones += 1
        nueva_devolucion = Devolucion(distribuidor=self, codigo=db.cantidad_devoluciones, publicacion=publicacion,
                                      cantidad=cantidad, fecha_devolucion=date.today())
        db.devoluciones.append(nueva_devolucion)
        return nueva_devolucion

    def realizar_reclamo(self, asunto, contenido):
        db.cantidad_reclamos += 1
        nuevo_reclamo = Reclamo(codigo=db.cantidad_reclamos, cliente=self, supervisor=self.get_supervisor(),
                                asunto=asunto, contenido=contenido, fecha_reclamo=date.today())
        db.reclamos.append(nuevo_reclamo)
        return nuevo_reclamo

    def __str__(self):
        string = Persona.__str__(self)
        string += ' Supervisor: ' + str(self.get_supervisor())
        string += ' Antigüedad: ' + str(self.get_antiguedad())
        string += ' Descuento: ' + str(self.get_descuento())
        return string

class Suscripcion(Aceptable):
    MODALIDAD_MENSUAL = 0
    MODALIDAD_ANUAL = 1
    ESTADO_ACTIVO = 1
    ESTADO_INACTIVO = 0

    def __init__(self, aceptado=False, codigo=None, cliente=None, direccion_entrega=None, producto=None,
                 modalidad=None, monto_total=None, estado=None, fecha_inicio=None, fecha_fin=None):
        Aceptable.__init__(self, aceptado)
        self.__codigo = codigo
        self.__cliente = cliente
        self.__direccion_entrega = direccion_entrega
        self.__producto = producto
        self.__modalidad = modalidad
        self.__monto_total = monto_total
        self.__estado = estado
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_direccion_entrega(self):
        return self.__direccion_entrega

    def set_direccion_entrega(self, direccion_entrega):
        self.__direccion_entrega = direccion_entrega

    def get_producto(self):
        return self.__cliente

    def set_producto(self, producto):
        self.__producto = producto

    def get_modalidad(self):
        return self.__modalidad

    def set_modalidad(self, modalidad):
        self.__modalidad = modalidad

    def get_monto_total(self):
        return self.__monto_total

    def set_monto_total(self, monto_total):
        self.__monto_total = monto_total

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin

    def set_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin


class ClienteSuscriptor(Cliente, Supervisado):
    def __init__(self, codigo=None, nombre=None, direccion=None, telefono=None,
                 email=None, razon_social=None, ruc=None, supervisor=None):
        Cliente.__init__(self, codigo, nombre, direccion, telefono, email, razon_social, ruc)
        Supervisado.__init__(self, supervisor)

    def suscribirse(self, producto=None, modalidad=None, tiempo_meses=None):
        db.cantidad_suscripciones += 1
        fecha_inicio = date.today()
        fecha_fin = fecha_inicio + relativedelta(months=tiempo_meses)
        monto_total = 0 #calcular
        nueva_suscripcion = Suscripcion(codigo=db.cantidad_suscripciones, cliente=self,
                                        direccion_entrega=self.get_direccion(), producto=producto, modalidad=modalidad,
                                        monto_total=monto_total, estado=Suscripcion.ESTADO_ACTIVO,
                                        fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        db.suscripciones.append(nueva_suscripcion)
        return nueva_suscripcion

    def anular_suscripcion(self, suscripcion):
        suscripcion.set_estado(Suscripcion.ESTADO_INACTIVO)
        return suscripcion

    def realizar_reclamo(self, asunto, contenido):
        db.cantidad_reclamos += 1
        nuevo_reclamo = Reclamo(codigo=db.cantidad_reclamos, cliente=self, supervisor=self.get_supervisor(),
                                asunto=asunto, contenido=contenido, fecha_reclamo=date.today())
        db.reclamos.append(nuevo_reclamo)
        return nuevo_reclamo

    def __str__(self):
        string = Persona.__str__(self)
        string += ' Supervisor: (' + str(self.get_supervisor()) + ")"
        # string += ' Antigüedad: ' + str(self.get_antiguedad())
        # string += ' Descuento: ' + self.get_descuento()
        return string

class Periodico(Producto, Publicacion):
    def __init__(self, fecha_publicacion=None, precio=None,
                 titulo_portada=None, numero_secciones=None, pagina_especial=False):
        Producto.__init__(self, precio)
        Publicacion.__init__(self, fecha_publicacion)
        self.__titulo_portada = titulo_portada
        self.__numero_secciones = numero_secciones
        self.__pagina_especial = pagina_especial

    def get_titulo_portada(self):
        return self.__titulo_portada

    def set_titulo_portada(self,titulo_portada):
        self.__titulo_portada = titulo_portada

    def get_numero_secciones(self):
        return self.__numero_secciones

    def set_numero_secciones(self, numero_secciones):
        self.__numero_secciones = numero_secciones

    def get_pagina_especial(self):
        return self.__pagina_especial

    def set_pagina_especial(self, pagina_especial):
        self.__pagina_especial = pagina_especial

    def __str__(self):
        string = Producto.__str__(self)
        string += ' Fecha Publicacion: ' + str(self.get_fecha_publicacion())
        string += ' Titulo: ' + str(self.get_titulo_portada())
        string += ' Secciones: ' + str(self.get_numero_secciones())
        string += ' Especial: ' + str(self.get_pagina_especial())
        return string

class Publico:
    def __init__(self, publico=None):
        self.__publico = publico

    def get_publico(self):
        return self.__publico

    def set_publico(self, publico):
        self.__publico = publico


class Revista(Producto, Publicacion, Publico):
    def __init__(self, precio=None, fecha_publicacion=None, publico=None,
                 edicion=None, tema_portada=None,numero_publicacion=None, valor_agregado=False):
        Producto.__init__(self, precio)
        Publicacion.__init__(self, fecha_publicacion)
        Publico.__init__(self, publico)
        self.__edicion = edicion
        self.__tema_portada = tema_portada
        self.__numero_publicacion = numero_publicacion
        self.__valor_agregado = valor_agregado

    def get_edicion(self):
        return self.__edicion

    def set_edicion(self, edicion):
        self.__edicion = edicion

    def get_tema_portada(self):
        return self.__tema_portada

    def set_tema_portada(self, tema_portada):
        self.__tema_portada = tema_portada

    def get_numero_publicacion(self):
        return self.__numero_publicacion

    def set_numero_publicacion(self, numero_publicacion):
        self.__numero_publicacion = numero_publicacion

    def get_valor_agregado(self):
        return self.__valor_agregado

    def set_valor_agregado(self, valor_agregado):
        self.__valor_agregado = valor_agregado

    def __str__(self):
        string = Producto.__str__(self)
        string += ' Fecha Publicacion: ' + str(self.get_fecha_publicacion())
        string += ' Precio: ' + str(self.get_precio())
        string += ' Publico: ' + str(self.get_publico())
        string += ' Edicion: ' + str(self.get_edicion())
        string += ' Tema de Portada: ' + str(self.get_tema_portada())
        string += ' Numero de Publicacion: ' + str(self.get_numero_publicacion())
        string += ' Valor Agregado: ' + str(self.get_valor_agregado())
        return string


class Coleccion(Producto, Publicacion, Publico):
    def __init__(self, precio=None, fecha_publicacion=None, publico=None,
                 nombre_coleccion=None, descripcion=None):
        Producto.__init__(self, precio)
        Publicacion.__init__(self, fecha_publicacion)
        Publico.__init__(self, publico)
        self.__nombre_coleccion = nombre_coleccion
        self.__descripcion = descripcion

    def get_nombre_coleccion(self):
        return self.__nombre_coleccion

    def set_nombre_coleccion(self, nombre_coleccion):
        self.__nombre_coleccion = nombre_coleccion

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def __str__(self):
        string = Producto.__str__(self)
        string += ' Fecha Publicacion: ' + str(self.get_fecha_publicacion().__str__())
        string += ' Precio: ' + str(self.get_precio())
        string += ' Publico: ' + str(self.get_publico())
        string += ' Nombre de Coleccion: ' + str(self.get_nombre_coleccion())
        string += ' Descripcion: ' + str(self.get_descripcion())
        return string


db.cargar_todo()