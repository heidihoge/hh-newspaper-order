# -*- coding: utf-8 -*-
"""
Este archivo crea la ventana principal de la aplicacion.
"""
import ventanas
import Tkinter as Tk

# Inicia la ventana principal
ventana_principal = Tk.Tk()
ventana_principal.title('HH Newspaper')

# Agrega el menu de opciones de administrador
menu = ventanas.AdminMenu(ventana_principal)
menu.grid(column=0, row=0)

# Loop de la aplicacion para que la ventana se mantenga abierta
ventana_principal.mainloop()
