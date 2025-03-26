import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import workbench

flow_box = workbench.builder.get_object("flow_box")
word = workbench.builder.get_object("word")
overlay = workbench.builder.get_object("overlay")
drawing_area = workbench.builder.get_object("drawing_area")
