import Tkinter as Tk
import inspect
import models
import db


def obtener_campos(model):
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
                    if hasattr(fn, '__call__'):
                        fn(seleccion)

                btn = Tk.Button(master=self, text=accion[0], command=_accion)
                btn.grid(row=first_row, column=i, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))

            first_row += 1

        # Crea la tabla con el listado
        crear_tabla(self, self.fields, self.data, self.selected, first_row)


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
            _class = obj
        else:
            _class = obj.__class__

        # Obtiene los campos del modelo
        self.campos = obtener_campos(_class)

        # Agrega el titulo
        titulo_label = Tk.Label(self)
        titulo_label['text'] = titulo
        titulo_label['font'] = ('Arial', 12, 'bold')
        titulo_label.grid(row=0, columnspan=len(self.campos), column=0, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))

        # Agrega el par <label | <entry> por cada campo (ej Codigo [      ] )
        row_num = 1
        for campo in self.campos:
            label = Tk.Label(self)
            label['text'] = str(campo).capitalize().replace('_', ' ')
            label.grid(column=0, row=row_num)
            entry = Tk.Entry(self)
            entry.grid(column=1, row=row_num, sticky=(Tk.N, Tk.S, Tk.E, Tk.W))
            entry.campo = campo
            row_num += 1

        # Agrega los botones de accion (ej [Guardar] )
        acciones_frame = Tk.Frame(self)
        acciones_frame.grid(row=row_num, column=0, columnspan=len(self.campos))
        for accion in acciones:
            button = Tk.Button(acciones_frame, text=accion[0], command=accion[1])
            button.pack()


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
        :param master:
        :return:
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
        if self._content is not None:
            self._content.grid_forget()
            self._content.destroy()
            self._content = None

    def seleccionar_tipo(self, tipos):
        """
        Muestra una lista de botones, que llaman a _nuevo(tipo) con el tipo correspondiente
        Para crear un nuevo elemento, se debe elegir antes su tipo
        (ej para crear nuevo Producto, tipos disponibles son [Periodico, Revista, Coleccion])
        :param tipos: <list> lista de <class>modelos
        """
        self.destroy_content()
        self._content = Menu(self.master)
        self._content.grid(row=0, column=1)
        for row_num, tipo in enumerate(tipos):
            self._content.agregar_boton(tipo.__name__, lambda tipo=tipo: self._nuevo(tipo))

    def _nuevo(self, _class):
        """
        Muestra el formulario para crear un nuevo objeto de tipo _class
        :param _class: <class> tipo de objeto a ser creado
        """
        self.destroy_content()
        self._content = Tk.Frame(self.master)
        Formulario(self._content, _class, titulo=_class.__name__).pack()
        button = Tk.Button(self._content, text='Guardar')
        self._content.grid(row=0, column=2)

    def productos(self):
        self.destroy_content()
        tipos = [models.Periodico, models.Revista, models.Coleccion]
        self._content = Listar(master=self.master,
                               model=models.Producto,
                               list_function=(lambda: db.cargar('productos', [])),
                               acciones=[['Nuevo', (lambda seleccion: self.seleccionar_tipo(tipos))]],
                               title='Productos')
        self._content.grid(column=1, row=0)

    def supervisores(self):
        self.destroy_content()
        self._content = Listar(master=self.master,
                               model=models.Persona,
                               list_function=(lambda: db.cargar('supervisores', [])),
                               acciones=[],
                               title='Supervisores')
        self._content.grid(column=1, row=0)

    def clientes(self):
        self.destroy_content()
        self._content = Listar(master=self.master,
                               model=models.Persona,
                               list_function=(lambda: db.cargar('clientes', [])),
                               acciones=[],
                               title='Clientes')
        self._content.grid(column=1, row=0)

    def pedidos(self):
        self.destroy_content()
        self._content = Listar(master=self.master,
                               model=models.Pedido,
                               list_function=(lambda: db.cargar('pedidos', [])),
                               acciones=[],
                               title='Pedidos')
        self._content.grid(column=1, row=0)

    def suscripciones(self):
        self.destroy_content()
        self._content = Listar(master=self.master,
                               model=models.Suscripcion,
                               list_function=(lambda: db.cargar('suscripciones', [])),
                               acciones=[],
                               title='Suscripciones')
        self._content.grid(column=1, row=0)

    def reclamos(self):
        self.destroy_content()
        self._content = Listar(master=self.master,
                               model=models.Reclamo,
                               list_function=(lambda: db.cargar('reclamos', [])),
                               acciones=[],
                               title='Reclamos')
        self._content.grid(column=1, row=0)
