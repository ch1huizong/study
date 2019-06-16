#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 22:30:11
# @Author  : che
# @Email   : ch1huizong@gmail.com

import time

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SimpleButtonApp(object):
    def __init__(self):
        self.window = Gtk.Window()
        self.window.connect("destroy", self.quit)
        self.button = Gtk.Button("Click Me")
        self.button.connect("clicked", self.update_button_label, None)
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def update_button_label(self, widget, data=None):
        self.button.set_label(time.asctime())

    def quit(self, widget, data=None):
        Gtk.main_quit()

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    s = SimpleButtonApp()
    s.main()
