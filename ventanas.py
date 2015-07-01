# -*- coding: utf-8 -*-
"""
En este archivo se encuentra todas las funciones utilizadas para la interfaz grafica en TKinter
"""
import Tkinter as Tk
import tkMessageBox as Message
import inspect
import models
import db
import servicios


def obtener_campos(model):
    """
    dada una clase, obtiene la lista de campos
    :param model: <class> clase del modelo
    :return: <list> lista de campost (ej ['codigo', 'precio'])
    """
    return [name[4:] for name in dir(model) if name.startswith('get_')]


def crear_tabla(contenedor, columnas, filas, seleccion, primera_fila=0):
    """
    Crea tablas del tipo:
    _________________________________________________________
    |     | <column1> | <column2> | <columnN> | tipo      | |
    | [x] [__<data>__][__<data>__][__<data>__][__<class>__] |
    | [x] [__<data>__][__<data>__][__<data>__][__<class>__] |
    | [x] [__<data>__][__<data>__][__<data>__][__<class>__] |
    |_______________________________________________________|

    :param contenedor: <Frame> Corresponde al Frame que contendra la tabla
    :param columnas: <list> Los nombres de las columnas
    :param filas: <list> Lista de filas, cada fila es un array con los datos correspondientes
    :param seleccion: <list> Lista vacia. al crear la tabla se almacenaran en ella los Codigos de las filas seleccionadas
    :param primera_fila: <int> Posicion de inicio de la tabla
    """
    # Inicia la grilla
    contenedor.grid(column=0, row=primera_fila, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))

    # Agrega los Labels con los nombres de las columnas
    col = 1
    for column in columnas:
        label = Tk.Label(contenedor, font=("Arial", 12, 'bold'))
        label['text'] = str(column).capitalize().replace('_', ' ')
        label.grid(column=col, row=primera_fila)
        col += 1

    # Fila de datos

    row_num = primera_fila + 1
    columna_codigo = columnas.index('codigo')
    for index, row in enumerate(filas):
        col = 1

        # Un Checkbutton para la seleccion de la fila
        def __check_press(event, codigo=filas[index][columna_codigo]):
            # Si el checkbutton no esta marcado
            if event.widget.var.get() == 0:
                # Agrego el codigo a mi lista de seleccion
                seleccion.append(codigo)
            # Si el checkbutton esta marcado
            elif codigo in seleccion:
                # Quito de mi lista
                seleccion.remove(codigo)

        var = Tk.IntVar()
        check_btn = Tk.Checkbutton(contenedor, variable=var)
        check_btn.var = var
        check_btn.grid(column=0, row=row_num)
        # click izquierdo
        check_btn.bind('<Button-1>', __check_press)

        # Agrega Campos por cada dato
        for field in row:
            if field is None:
                field = ''
            entry = Tk.Entry(contenedor)
            entry.insert(0, field)
            entry.config(state='readonly')
            entry.grid(column=col, row=row_num, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))
            col += 1

        row_num += 1


class Listar(Tk.Frame):
    """
    Esta clase crea lista los elementos de cualquier modelo
    ________________________________________
    |              <titulo>                |
    |--------------------------------------|
    |             <acciones>               |
    |--------------------------------------|
    |              <tabla>                 |
    |______________________________________|
    """

    def __init__(self, master, model, list_function, acciones=(), title=None):
        Tk.Frame.__init__(self, master)
        self.__model = model

        # Obtiene los nombres de los campos
        self.fields = obtener_campos(self.__model)

        # Agrega el campo 'Tipo'
        self.fields.append('Tipo')
        self.selected = []

        first_row = 0

        def obj_array(obj):
            """
            Obtiene los valores del objeto como una lista
            :param obj: <self.__model> una instancia de self.__model (ej un objeto de tipo producto)
            :return: <list> lista de valores del objeto (ej [0, 11000] -> [<codigo>, <precio>])
            """
            result = []
            for field in self.fields:
                key = '_%s__%s' % (self.__model.__name__, field)
                if key in obj.__dict__:
                    result.append(obj.__dict__.get(key))
            result.append(obj.__class__.__name__)
            return result

        # Convierte la lista de objetos en una matriz (lista de listas)
        self.data = map(obj_array, list_function())

        # Agrega el titulo
        if title:
            label = Tk.Label(self, font=("Arial", 12, 'bold'))
            label['text'] = title
            label.grid(column=0, columnspan=len(self.fields) + 2, row=first_row)
            first_row += 1

        # Agrega los botones de accion
        if acciones:
            num_columnas = len(self.fields)
            i = 0
            for accion in acciones:

                i += 1
                i %= (num_columnas + 1)
                # Si ya no hay espacio, agrega los botones en la siguiente linea
                if i == 0:
                    i += 1
                    first_row += 1

                def _accion(fn=accion[1], seleccion=self.selected):
                    """
                    Ejecuta la accion si 'fn' es una funcion, le manda seleccion como parametro
                    """
                    if hasattr(fn, '__call__'):
                        fn(seleccion)

                btn = Tk.Button(master=self, text=accion[0], command=_accion)
                btn.grid(row=first_row, column=i, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))

            first_row += 1

        # En caso de que haya elementos
        if len(self.data) > 0:
            # Crea la tabla con el listado
            crear_tabla(self, self.fields, self.data, self.selected, first_row)
        else:
            # Caso contrario mostrar mensaje
            Tk.Label(self, text="No hay datos").grid(row=first_row, column=1)


class Formulario(Tk.Frame):
    """
    Formulario utilizado para crear y modificar objetos
    ___________________________
    |        <titulo>         |
    |-------------------------|
    | <label>     | <Entry>   |
    |-------------------------|
    | <label>     | <Entry>   |
    |-------------------------|
    | <label>     | <Entry>   |
    |-------------------------|
    |        <acciones>       |
    |_________________________|
    """

    def __init__(self, master, obj, titulo='', acciones=()):
        Tk.Frame.__init__(self, master)

        # Obtiene la clase del modelo a utilizar
        if inspect.isclass(obj):
            self._class = obj
            es_obj = False
        else:
            self._class = obj.__class__
            es_obj = True

        # Obtiene los campos del modelo
        self.campos = obtener_campos(self._class)

        # Agrega el titulo
        titulo_label = Tk.Label(self)
        titulo_label['text'] = titulo
        titulo_label['font'] = ('Arial', 12, 'bold')
        titulo_label.grid(row=0, columnspan=len(self.campos), column=0, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))

        # Agrega el par <label | <entry> por cada campo (ej Codigo [      ] )
        row_num = 1

        # lista de campos de texto
        self.entries = []
        for campo in self.campos:
            # Label
            label = Tk.Label(self)
            label['text'] = str(campo).capitalize().replace('_', ' ')
            label.grid(column=0, row=row_num)
            # Entry
            valor = Tk.StringVar()
            # Si es un objeto, carga el valor original
            if es_obj:
                getter = "get_%s" % campo
                if getter in dir(obj):
                    get_valor = getattr(obj, getter)
                    valor.set(get_valor())
            entry = Tk.Entry(self)
            entry.grid(column=1, row=row_num, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))
            if es_obj and campo == 'codigo':
                entry['state'] = 'readonly'
            entry['textvariable'] = valor
            # Guarda los valores importantes
            entry.valor = valor
            entry.campo = campo
            # Guarda en la lista de campos
            self.entries.append(entry)
            row_num += 1

        # Agrega los botones de accion (ej [Guardar] )
        acciones_frame = Tk.Frame(self)
        acciones_frame.grid(row=row_num, column=0, columnspan=len(self.campos))
        for accion in acciones:
            button = Tk.Button(acciones_frame, text=accion[0], command=accion[1])
            button.pack()

    def get_obj(self):
        """
        Convierte el Formulario en un objeto del tipo correspondiente
        :return: <model> obj
        """
        obj = self._class()
        for entry in self.entries:
            campo = entry.campo
            valor = entry.valor.get()
            if campo == 'codigo':
                try:
                    valor = int(valor)
                except:
                    return None
            setter = "set_%s" % campo
            if setter in dir(obj):
                set_valor = getattr(obj, setter)
                set_valor(valor)
        return obj


class Menu(Tk.Frame):
    """
    Menu de botones
    |----------|
    |[<button>]|
    |----------|
    |[<button>]|
    |----------|
    |[<button>]|
    |----------|
    |[<button>]|
    |----------|
    """

    def __init__(self, master=None):
        """
        Constructor del Menu
        :param master: <Frame|TK> contenedor
        """
        Tk.Frame.__init__(self, master)

    def agregar_botones(self, lista_texto_accion):
        """
        Dada una lista de [nombre, accion]
        genera los botones del menu
        :param lista_texto_accion: <list> lista de pares nombre, accion
        """
        map(lambda obj: self.agregar_boton(obj[0], obj[1]), lista_texto_accion)

    def agregar_boton(self, nombre, accion):
        """
        Agrega un boton al menu
        :param nombre: <str> Nombre del boton
        :param accion: <function> Funcion a ser llamada cuando el boton se oprima
        """
        # if accion is not None:
        btn = Tk.Button(self)
        btn['text'] = nombre
        btn['command'] = accion
        btn.pack({"fill": "x"})

    def agregar_categoria(self, nombre):
        """
        Agrega un label entre los botones
        Utilizado para separar los botones en categorias
        :param nombre: <str> texto del label (nombre de categoria)
        """
        label = Tk.Label(self)
        label['text'] = nombre
        label['font'] = ('Arial', 10, 'bold')
        label.pack({"fill": "x"})


class AdminMenu(Menu):
    """
    <menu> compuesto de una serie de botones, cuyas acciones se ven reflejadas en <content>
    __________________________
    |<menu> | <content>      |
    |       |                |
    --------------------------
    """

    def __init__(self, master=None):
        """
        Constructor del menu de admin
        :param master: <Frame|TK> contenedor
        """
        Menu.__init__(self, master=master)

        # Opciones disponibles
        # par nombre | accion
        menus = [
            ["Productos", self.productos],
            ["Supervisores", self.supervisores],
            ["Clientes", self.clientes],
            ["Pedidos", self.pedidos],
            ["Suscripciones", self.suscripciones],
            ["Reclamos", self.reclamos]
        ]

        # Agrega los botones disponibles
        self.agregar_botones(menus)

        # Inicializa _content a None
        self._content = None

    def destroy_content(self):
        """
        Quita el contenido de <content>
        """
        # Si hay _content
        if self._content is not None:
            # olvida la grilla
            self._content.grid_forget()
            # destruye
            self._content.destroy()
            self._content = None

    def seleccionar_tipo(self, tipos, tabla, _fn):
        """
        Muestra una lista de botones, que llaman a _nuevo(tipo) con el tipo correspondiente
        Para crear un nuevo elemento, se debe elegir antes su tipo
        (ej para crear nuevo Producto, tipos disponibles son [Periodico, Revista, Coleccion])
        |-----------|
        |[Periodico]|
        |-----------|
        |[Revista  ]|
        |-----------|
        |[Coleccion]|
        |-----------|
        :param tipos: <list> lista de <class>modelos
        :param tabla: <str> el nombre de la tabla en la bd
        :param _fn: <function> funcion que dibuja el frame de listar correspondiente una vez guardado
        """
        self.destroy_content()
        self._content = Menu(self.master)
        self._content.grid(row=0, column=1)
        for row_num, tipo in enumerate(tipos):
            self._content.agregar_boton(tipo.__name__, lambda tipo=tipo: self._nuevo(tipo, tabla, _fn))

    def _eliminar(self, elementos, tabla, _fn):
        """
        Dada una lista de elementos seleccionados, los elimina de la base de datos
        :param elementos: <list> lista de codigos (ej [1,2,3,4])
        :param tabla: <str> Nombre de la tabla de la bd
        :param _fn: <funcion> Funcion que vuelve a dibujar la lista una vez eliminado
        :return:
        """
        if len(elementos) == 0:
            Message.showinfo("No hay nada que borrar", "No ha seleccionado nada que eliminar.")
            return
        if Message.askokcancel("Confirmar", "Estas seguro que deseas borrar estos elementos?"):
            servicios.eliminar(elementos, tabla)
            _fn()

    def _modificar(self, selected, tabla, _fn):
        if len(selected) == 0:
            Message.showerror("Error", "Seleccione al menos un elemento.")
            return
        elif len(selected) > 1:
            Message.showerror("Error", "Seleccione solo un elemento.")
            return
        elementos = filter(lambda obj: obj.get_codigo() == int(selected[0]), db.cargar(tabla, []))
        if len(elementos) == 0:
            Message.showerror("Error", "El elemento no existe en la base de datos.")
            return

        self._nuevo(elementos[0], tabla, _fn)

    def _nuevo(self, obj, tabla, _fn):
        """
        Muestra el formulario para crear un nuevo objeto de tipo _class
        :param _class: <class> tipo de objeto a ser creado
        """
        if not inspect.isclass(obj):
            _class = obj.__class__
        else:
            _class = obj
        self.destroy_content()
        self._content = Tk.Frame(self.master)
        formulario = Formulario(self._content, obj, titulo=_class.__name__)
        formulario.pack()
        button = Tk.Button(self._content, text='Guardar',
                           command=lambda: ((Message.showinfo("Exito!", "Guardado Correctamente"), _fn())
                                            if servicios.guardar(formulario.get_obj(), tabla)
                                            else Message.showerror("Error",
                                                                   "No se puede guardar. Verifique los campos.")))
        button.pack()
        self._content.grid(row=0, column=1)

    def productos(self):
        """
        Funcion especifica
        Dibuja la lista de productos
        """
        self.destroy_content()
        tipos = [models.Periodico, models.Revista, models.Coleccion]
        tabla = 'productos'
        self._content = Listar(master=self.master,
                               model=models.Producto,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self.seleccionar_tipo(tipos, tabla, self.productos))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.productos))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.productos))],
                               ],
                               title='Productos')
        self._content.grid(column=1, row=0)

    def supervisores(self):
        """
        Funcion especifica
        Dibuja la lista de supervisores
        """
        self.destroy_content()
        tabla = 'supervisores'
        self._content = Listar(master=self.master,
                               model=models.Persona,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self._nuevo(models.Supervisor, tabla, self.supervisores))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.supervisores))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.supervisores))],
                               ],
                               title='Supervisores')
        self._content.grid(column=1, row=0)

    def clientes(self):
        """
        Funcion especifica
        Dibuja la lista de clientes
        """
        self.destroy_content()
        tabla = 'clientes'
        self._content = Listar(master=self.master,
                               model=models.Persona,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self._nuevo(models.Cliente, tabla, self.clientes))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.clientes))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.clientes))],
                               ],
                               title='Clientes')
        self._content.grid(column=1, row=0)

    def pedidos(self):
        """
        Funcion especifica
        Dibuja la lista de pedidos
        """
        self.destroy_content()
        tabla = 'pedidos'
        self._content = Listar(master=self.master,
                               model=models.Pedido,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self._nuevo(models.Pedido, tabla, self.pedidos))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.pedidos))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.pedidos))],
                               ],
                               title='Pedidos')
        self._content.grid(column=1, row=0)

    def suscripciones(self):
        """
        Funcion especifica
        Dibuja la lista de suscripciones
        """
        self.destroy_content()
        tabla = 'suscripciones'
        self._content = Listar(master=self.master,
                               model=models.Suscripcion,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self._nuevo(models.Suscripcion, tabla, self.suscripciones))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.suscripciones))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.suscripciones))],
                               ],
                               title='Suscripciones')
        self._content.grid(column=1, row=0)

    def reclamos(self):
        """
        Funcion especifica
        Dibuja la lista de reclamos
        """
        self.destroy_content()
        tabla = 'reclamos'
        self._content = Listar(master=self.master,
                               model=models.Reclamo,
                               list_function=(lambda: db.cargar(tabla, [])),
                               acciones=[
                                   ['Nuevo', (lambda seleccion: self._nuevo(models.Reclamo, tabla, self.reclamos))],
                                   ['Eliminar', (lambda seleccion: self._eliminar(seleccion, tabla, self.reclamos))],
                                   ['Modificar', (lambda seleccion: self._modificar(seleccion, tabla, self.reclamos))],
                               ],
                               title='Reclamos')
        self._content.grid(column=1, row=0)
