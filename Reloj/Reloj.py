#!/usr/bin/env python

import time

from gi.repository import Gtk
from gi.repository import GObject


class Reloj(Gtk.HBox):

    def actualizar(self, imagenes, cantidad):
        for x in time.strftime("%H:%M:%S"):
            imagenes[cantidad].set_from_file("Reloj/" + x + ".gif")
            cantidad += 1

        return True

    def __init__(self):
        Gtk.HBox.__init__(self, False, 1)

        imagenes = [Gtk.Image(), Gtk.Image(), Gtk.Image(), Gtk.Image(), Gtk.Image(), Gtk.Image(), Gtk.Image(), Gtk.Image()]
        cantidad = 0

        for x in imagenes:
            self.add(x)

        self.show_all()

        GObject.timeout_add_seconds(1, self.actualizar, imagenes, cantidad)
