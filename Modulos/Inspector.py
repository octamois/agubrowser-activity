# Copyright (C) 2008 Jan Alonzo <jmalonzo@unpluggable.com>
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

from gi.repository import Gtk
from gi.repository import WebKit


class Inspector(Gtk.Window):

    def __init__(self, inspector):
        Gtk.Window.__init__(self)

        self.set_default_size(600, 480)

        self._web_inspector = inspector
        self._web_inspector.connect("inspect-web-view", self._inspect_web_view_cb)
        self._web_inspector.connect("show-window", self._show_window_cb)
        self._web_inspector.connect("attach-window", self._attach_window_cb)
        self._web_inspector.connect("detach-window", self._detach_window_cb)
        self._web_inspector.connect("close-window", self._close_window_cb)
        self._web_inspector.connect("finished", self._finished_cb)

        self.connect("delete-event", self._close_window_cb)

    def _inspect_web_view_cb(self, inspector, web_view):
        """Called when the 'inspect' menu item is activated"""
        scroll = Gtk.ScrolledWindow()
        ##scrolled_window.props.hscrollbar_policy = Gtk.PolicyType.AUTOMATIC
        ##scrolled_window.props.vscrollbar_policy = Gtk.PolicyType.AUTOMATIC
        self.add(scroll)

        view = WebKit.WebView()
        scroll.add(view)
        scroll.show_all()

        return webview

    def _show_window_cb(self, inspector):
        """Called when the inspector window should be displayed"""
        self.present()

        return True

    def _attach_window_cb(self, inspector):
        """Called when the inspector should displayed in the same
        window as the WebView being inspected
        """
        return False

    def _detach_window_cb(self, inspector):
        """Called when the inspector should appear in a separate window"""

        return False

    def _close_window_cb(self, inspector, view):
        """Called when the inspector window should be closed"""
        self.hide()

        return True

    def _finished_cb(self, inspector):
        """Called when inspection is done"""
        self._web_inspector = 0
        self.destroy()

        return False

