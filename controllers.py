def g():
    print("Item")


class AdminController:
    def __init__(self):
        self.menu_items = ("Productos", "Supervisores", "Clientes", "Pedidos", "Suscripciones", "Reclamos", "Atras")
        self.submenu_items = ("Listar", "Crear", "Eliminar", "Modificar", "Atras", "")
        self.disponible = ((1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 0, 0, 0, 1),
                           (1, 0, 0, 0, 1), (1, 0, 0, 0, 1), (1, 0, 0, 0, 1))

    def verificar_menu(self, menu_seleccionado):
        # verifica si es numero
        num = 0
        try:
            num = int(menu_seleccionado)
        except:
            return False

        # verifica si esta en rango
        return 0 <= num < len(self.menu_items)

    def verificar_submenu(self, menu_seleccionado, submenu_seleccionado):
        # verifica si es numero
        num = 0
        try:
            num = int(submenu_seleccionado)
        except:
            return False

        # verifica si esta en rango
        if 0 <= num < len(self.menu_items):
            if self.disponible[menu_seleccionado][num] == 1:
                return True
        return False

    def menu(self):
        menu_item = None
        submenu_item = None
        # menu
        while menu_item is None:
            for i in range(len(self.menu_items)):
                print(u"{}-{}".format(i, self.menu_items[i]))
            menu_item = input()
            if not self.verificar_menu(menu_item):
                menu_item = None
                print("Opcion invalida")

        menu_item = int(menu_item)

        print("Elegiste {}".format(self.menu_items[menu_item]))
        #submenu
        while submenu_item is None:
            for i in range(len(self.submenu_items)):
                if self.disponible[menu_item][i] == 1:
                    print(u"{}-{}".format(i, self.submenu_items[i]))
            submenu_item = input()
            if not self.verificar_submenu(menu_item, submenu_item):
                submenu_item = None
                print("Opcion invalida")

        print("Elegiste {}".format(self.submenu_items[submenu_item]))


AdminController().menu()