from servicios import *


class Controller:
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def menu(self, titulo, acciones, numero_menu=0, max_menu=100):
        opt = None
        while opt != 0:
            print titulo
            self.mostrar_menu(numero_menu, max_menu)
            try:
                opt = int(input())
            except:
                print ("Por favor introduzca el numero del item.")
            if len(acciones) >= opt > 0:
                acciones[opt - 1]()

    def mostrar_menu(self, num=0, max=100):
        print "0 - Salir"
        c = 0
        for item in self.menu_items[num]:
            c += 1
            if c >= max:
                break
            print c, '-', item


class AdminController(Controller):
    def __init__(self):
        items = [["Productos", "Supervisores", "Clientes", "Pedidos", "Suscripciones", "Reclamos"],
                 ["Listar", "Crear", "Eliminar", "Modificar"]]
        Controller.__init__(self, menu_items=items)

    def menu_principal(self):
        acciones = [self.menu_productos]
        self.menu(titulo='Menu Principal', acciones=acciones)

    def menu_productos(self):
        acciones = [ProductoService.listar, ProductoService.crear, ProductoService.eliminar]
        self.menu(titulo='Producto', acciones=acciones, numero_menu=1)


AdminController().menu_principal()