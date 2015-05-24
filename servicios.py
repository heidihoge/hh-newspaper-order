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

            db.productos.append(periodico)
            db.guardar(db.productos, 'productos')
        if opt == 2:
            fecha_publicacion = date.today()
            precio = input("Precio: ")
            publico = input("Publico: ")
            edicion = input("Edicion: ")
            tema_portada = input("Tema de Portada: ")
            numero_publicacion = input("Numero de Publicacion: ")
            valor_agregado = input("Valor agregado: ")

            revista = Revista(fecha_publicacion=fecha_publicacion, precio=precio, publico=publico, edicion=edicion,
                                  tema_portada=tema_portada, numero_publicacion=numero_publicacion,
                                  valor_agregado=valor_agregado)

            db.productos.append(revista)
            db.guardar(db.productos, 'productos')

        if opt == 3:
            fecha_publicacion = date.today()
            precio = input("Precio: ")
            publico = input("Publico: ")
            nombre_coleccion = input("Nombre coleccion: ")
            descripcion = input("Descripcion: ")

            coleccion = Coleccion(fecha_publicacion=fecha_publicacion, precio=precio, publico=publico,
                                  nombre_coleccion=nombre_coleccion, descripcion=descripcion)

            db.productos.append(coleccion)
            db.guardar(db.productos, 'productos')
    db.cargar_todo()


class SupervisorService:
    @staticmethod
    def listar():
        db.cargar_todo()
        pass

    @staticmethod
    def eliminar():
        codigo = input("Ingrese el codigo de supervisor a eliminar: ")
        db.cargar_todo()
        eliminado = False
        lista_nueva = filter(lambda x: x.get_codigo() != codigo, db.supervisor)
        if lista_nueva != db.supervisor:
            print('Se ha eliminado el Supervisor.')
        else:
            print('El supervisor no existe.')
        db.guardar(lista_nueva, 'supervisores')


    @staticmethod
    def crear():
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        razon_social = input("Raon Social: ")
        ruc = input("Ruc: ")

        supervisor = Supervisor(codigo=codigo, nombre=nombre, direccion=direccion, telefono=telefono, email=email,
                                razon_social=razon_social, ruc=ruc)

        db.cargar_todo()
