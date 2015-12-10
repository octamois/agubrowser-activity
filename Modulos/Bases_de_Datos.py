#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sqlite3
import shutil

from gi.repository import Gtk

from sugar3.activity import activity


datos = activity.get_activity_root() + "/data/datos/"

if not os.path.exists(datos + "Claves.py"):
    nuevo = open(datos + "Claves.py", "w")
    nuevo.write("primera=True")
    nuevo.close()


class Bases_de_Datos():

    def limpiar(self, entry, event):
        entry.set_text("")

    def aceptar(self, widget, entry, dialog, entry0):
        self.clave = entry.get_text()
        self.usuario = entry0.get_text()

        if self.usuario and self.clave:
            nuevo = open(datos+"Claves.py")
            nuevo.write("primera=%s \nusuario=%s \nclave=%s" % ("False", self.usuario, self.clave))
            nuevo.close()

            pos_anterior = os.getcwd() # Guardo la direccion actual
            os.chdir(datos) # Me muevo al directorio de datos para importar
            import Claves
            os.chdir(pos_anterior) # me muevo de vuelta a la posicion anterior (que deberia ser: /home/olpc/Activities/AguBrowser.activity/)

            dialog.destroy()

    def comprobar_datos(self, usuario, clave):
        if usuario == Claves.usuario and clave == Claves.clave:
            datos = "Coinciden"

        else:
            datos = "No coinciden"

        return datos

    def __init__(self):
        pass
