#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Arma una pantalla completa con la ventana de AguBrowse

#   Pantalla_Completa.py por:
#   Agustin Zuiaga <aguszs97@gmail.com>
#   Python Joven - Utu Rafael Peraza 
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA 

__author__ = "Agustin Zubiaga"
__date__ = "8 de marzo del 2011, 16:48"

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject


class Armar_Pantalla_Completa():

    def conteo_cb(self):
        self.window.hide()
        return self.continuar

    def mostrar_boton1(self, event, other): # Cuando se mueve el mouse
        if self.show_window:
            self.continuar = False # Desactivar conteo
            self.window.show_all() # Mostrar ventana emergente

            self.continuar = True # Volver a activar conteo

    def salir(self, widget):
        self.bar.show_all() # Mostrar barras
        self.show_window = False # Nos aseguramos de que la ventana no se mostrara mas
        self.window.hide() # Ocultar la Ventana
        self.abrowse.unfullscreen() # Salir de pantalla completa

        # Nota: Cuando se destruye una ventana emergente esta luego aparece como un cuadrado gris
                # y por eso nunca la destruyo si no que no la muestro

    def show_bars(self, widget):
        if not self.st:
            self.bar.show_all()
            widget.set_label("No mostrar barra de herramientas")
            self.st = True

        else:
            self.bar.hide()
            widget.set_label("Mostrar barra de herramientas")
            self.st = False

    def __init__(self, abrowse):

        self.show_window = True

        abrowse.fullscreen()
        abrowse.add_events(Gdk.EventMask.POINTER_MOTION_MASK) # Agregamos eventos
        abrowse.connect("motion_notify_event", self.mostrar_boton1) # Cuando se mueve el puntero del mouse

        self.abrowse = abrowse
        self.st = False

        bar = abrowse.main.get_child1()
        bar.hide()

        self.bar = bar


        boton_mostrar = Gtk.Button("Mostrar barra de herramientas")
        boton_mostrar.connect("clicked", self.show_bars)
        boton_salir = Gtk.Button(None, stock=Gtk.STOCK_LEAVE_FULLSCREEN)
        boton_salir.connect("clicked", self.salir)

        hbox = Gtk.HBox(False, 10)
        hbox.add(boton_mostrar)
        hbox.add(boton_salir)
        ##hbox.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0,0,0,1))

        self.window = Gtk.Window(Gtk.WindowType.POPUP)
        self.window.add(hbox)
        ##self.window.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 0, 1))
        hbox.show_all()

        self.continuar = False
        self.conteo = GObject.timeout_add_seconds(6, self.conteo_cb)

