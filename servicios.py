import db
from models import *


class ProductoService:
    @staticmethod
    def listar():
        db.cargar_todo()
        print 'Tipo', '\t\t', 'Codigo', '\t\t', 'Precio'
        for producto in db.productos:
            print producto.__class__.__name__, producto
        print ''

    @staticmethod
    def eliminar():
        codigo = input("Ingrese el codigo a eliminar: ")
        db.cargar_todo()
        eliminado = False
        lista_nueva = filter(lambda x: x.get_codigo() != codigo, db.productos)
        if lista_nueva != db.productos:
            print('Se ha eliminado el Producto.')
        else:
            print('El producto no existe.')
        db.guardar(lista_nueva, 'productos')

    @staticmethod
    def crear():
        print ('Elija el producto a agregar')
        tipos = ['Periodico', 'Revista', 'Coleccion']
        c = 0
        for tipo in tipos:
            c += 1
            print c, '-', tipo
        opt = input()
        if opt == 1:
            # fecha_publicacion = input("Fecha publicacion: ")
            fecha_publicacion = date.today()
            precio = input("Precio: ")
            titulo_portada = input("Titulo Portada: ")
            numero_secciones = input("Numero secciones: ")
            pagina_especial = input("Pagina Especial: ")

            periodico = Periodico(fecha_publicacion=fecha_publicacion, precio=precio,
                                  titulo_portada=titulo_portada, numero_secciones=numero_secciones,
                                  pagina_especial=pagina_especial)

            db.cargar_todo()
            db.productos.append(periodico)
            db.guardar(db.productos, 'productos')

