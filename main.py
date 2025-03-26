import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import workbench

flow_box = workbench.builder.get_object("flow_box")
word = workbench.builder.get_object("word")
overlay = workbench.builder.get_object("overlay")
drawing_area = workbench.builder.get_object("drawing_area")

def append_letters():
    for ascii in range(65, 65 + 26):
        letter = chr(ascii)
        button = Gtk.Button(label=letter)
        button.add_css_class("pill")
        button.add_css_class("circular")
        flow_box.append(button)

append_letters()
