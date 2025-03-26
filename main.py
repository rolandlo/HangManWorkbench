import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import workbench
import math

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

def draw(_drawingarea, cr, width, height):
    width = min(width, 0.8 * height)
    cr.set_source_rgba(1, 0, 1, 1) # magenta

    # Horizontale am Boden
    cr.move_to(0, height)
    cr.line_to(width, height)

    # Pfosten
    cr.move_to(0.2 * width, height)
    cr.line_to(0.2 * width, 0)

    # Querbalken
    cr.line_to(0.7 * width, 0)

    # Seil
    cr.line_to(0.7 * width, 0.2 * height)

    # Kopf
    cr.arc(0.7 * width, 0.3 * height, 0.1 * height, 1.5 * math.pi, 3.5 * math.pi)

    # Körper
    cr.move_to(0.7 * width, 0.4 * height)
    cr.line_to(0.7 * width, 0.7 * height)

    # linker Arm
    cr.move_to(0.7 * width, 0.45 * height)
    cr.line_to(0.6 * width, 0.55 * height)

    # rechter Arm
    cr.move_to(0.7 * width, 0.45 * height)
    cr.line_to(0.8 * width, 0.55 * height)

    # linkes Bein
    cr.move_to(0.7 * width, 0.7 * height)
    cr.line_to(0.6 * width, 0.8 * height)

    # rechtes Bein
    cr.move_to(0.7 * width, 0.7 * height)
    cr.line_to(0.8 * width, 0.8 * height)

    cr.stroke()

append_letters()
drawing_area.set_draw_func(draw)
