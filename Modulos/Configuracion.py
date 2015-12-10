#!/usr/bin/env python

#   Configuracion.py por:
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

import os
import sys

from gi.repository import Gtk
from gi.repository import Pango

datos = os.path.join(os.getenv("HOME"), ".AguBrowse/")
if not os.path.exists(datos):
    os.mkdir(datos)

if not os.path.exists(os.path.join(datos, "Web_Home")):
    f = open(os.path.join(datos, "Web_Home"), "w")
    f.write("")
    f.close()


class Configuracion(Gtk.Window):

    def delete_event(self, window, data):
        self.destroy()
        home_web = open(os.path.join(datos, "Web_Home"), "w")
        home_web.write(self.entry.get_text())
        home_web.close()
        self.browser.update_configuracion()

    def boton_home_cb(self, boton):
        bool = boton.get_active()
        home = open(datos+"Boton_Home", "w")
        if bool:
            home.write("Si")

        else:
            home.write("No")

        home.close()

    def set_buscador(self, nombre, direccion):
        buscador = open(datos + "Buscador", "w")
        buscador.write(nombre + "!" + direccion)
        buscador.close()

    def menu_busquedas(self, boton1, event):
        boton = event.button
        tiempo = event.time
        pos = (event.x, event.y)
        self.menu(boton1, boton, pos, tiempo)
        return

    def posicionar_menu(self, a, b):
        pass

    def set_home_web(self, entry):
        home_web = open(datos+"Web_Home", "w")
        home_web.write(entry.get_text())
        home_web.close()
        self.browser.update_configuracion()

    def __init__(self, browser):
        Gtk.Window.__init__(self)

        self.set_title("Configuracion - AguBrowse 2.0")
        self.resize(600, 300)

        self.buscadores = {"Google":           "http://www.google.com.uy/#hl=es&biw=1280&bih=534&q=palabra_clave&aq=f&aqi=&aql=&oq=&fp=1e07aebe9596e838",
                           "Bing":             "http://www.bing.com/search?setmkt=es-XL&q=palabra_clave",
                           "Yahoo!":           "http://search.yahoo.com/search?ei=UTF-8&fr=crmas&p=palabra_clave",
                           "Wikipedia":        "http://es.wikipedia.org/wiki/Special:Search?search=palabra_clave",
                           "eBay":             "http://rover.ebay.com/rover/1/711-47294-18009-3/4?satitle=palabra_clave",
                           "Creative Commons": "http://search.creativecommons.org/?q=palabra_clave"}

        # ***** Obtenemos la clase AguBrowse:
        self.browser = browser

        # ***** Contenedor
        main = Gtk.VBox()
        self.add(main)

        # ***** NOTEBOOK
        pestanias = Gtk.Notebook()
        main.add(pestanias)

        # ***** Basicas *****
        basicas = Gtk.VBox()
        pestanias.append_page(basicas, Gtk.Label("Basicas"))

        principal = Gtk.Label()
        principal.set_markup("<b>Pagina principal</b>")
        basicas.add(Gtk.Label("Abrir esta pagina web: "))

        entry = Gtk.Entry()
        entry.set_text("http://www.google.com")
        entry.connect("activate", self.set_home_web)
        basicas.add(entry)
        self.entry = entry

        boton_home = Gtk.CheckButton(label='Motrar el boton "Pagina de Inicio" en la barra de herramientas')
        boton_home.connect("toggled", self.boton_home_cb)
        boton_home.set_active(True)
        ##boton_home.modify_bg(Gtk.StateType.PRELIGHT, Gtk.gdk.color_parse("skyblue"))
        ##boton_home.modify_bg(Gtk.StateType.SELECTED, Gtk.gdk.color_parse("yellow"))
        #basicas.add(boton_home)

        buscar = Gtk.Label()
        buscar.set_markup("<b>Buscar</b>")
        basicas.add(buscar)

        combo = Gtk.ComboBoxText()
        combo.connect("changed", self.combo_changed)
        basicas.add(combo)

        for key in self.buscadores:
            combo.append_text(key)

        def boton_notify(widget):
            bool = boton.get_active()
            home = open(datos+"Notificaciones", "w")
            if bool:
                home.write("Si")

            else:
                home.write("No")

            home.close()

        notify = Gtk.CheckButton(label="Deseas que aparezca una notificacion cada vez \n que se termine de cargar una pagina")
        ##notify.modify_bg(Gtk.StateType.PRELIGHT, Gtk.gdk.color_parse("skyblue"))
        ##notify.modify_bg(Gtk.StateType.SELECTED, Gtk.gdk.color_parse("yellow"))
        notify.set_active(True)
        notify.connect("toggled", boton_notify)

        quitbox = Gtk.HButtonBox()
        quitbox.set_layout(Gtk.ButtonBoxStyle.END)

        cerrar = Gtk.Button("Cerrar")
        cerrar.connect("clicked", self.delete_event, None)
        quitbox.add(cerrar)
        main.add(quitbox)
        self.show_all()

    def combo_changed(self, combo):
        self.set_buscador(combo.get_active_text(), self.buscadores[combo.get_active_text()])


if __name__ == "__main__":
    Configuracion()
    Gtk.main()

