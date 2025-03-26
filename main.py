import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import workbench
import math
import random

flow_box = workbench.builder.get_object("flow_box")
word = workbench.builder.get_object("word")
overlay = workbench.builder.get_object("overlay")
drawing_area = workbench.builder.get_object("drawing_area")

word_list = ["KLAUS", "HEINO", "ANNA", "SUSANNE", "GERTRUD", "HELGA", "HANS", "FRANZ", "KUNO", "KATHARINA"]
deactivated_list = []

def reset():
    global step
    global secret
    step = 0
    secret = random.choice(word_list)
    word.set_label("_" * len(secret))

    for button in deactivated_list:
        button.set_sensitive(True)

    drawing_area.queue_draw()


def append_letters():
    for ascii in range(65, 65 + 26):
        letter = chr(ascii)
        button = Gtk.Button(label=letter)
        button.connect("clicked", on_clicked)
        button.add_css_class("pill")
        button.add_css_class("circular")
        flow_box.append(button)

def draw(_drawingarea, cr, width, height):
    width = min(width, 0.8 * height)
    cr.set_source_rgba(1, 0, 1, 1) # magenta

    if step>=1: # Horizontale am Boden
      cr.move_to(0, height)
      cr.line_to(width, height)

    if step>=2: # Pfosten
      cr.move_to(0.2 * width, height)
      cr.line_to(0.2 * width, 0)

    if step>=3: # Querbalken
      cr.line_to(0.7 * width, 0)

    if step>=4: # Seil
      cr.line_to(0.7 * width, 0.2 * height)

    if step>=5: # Kopf
      cr.arc(0.7 * width, 0.3 * height, 0.1 * height, 1.5 * math.pi, 3.5 * math.pi)

    if step>=6: # Körper
      cr.move_to(0.7 * width, 0.4 * height)
      cr.line_to(0.7 * width, 0.7 * height)

    if step>=7: # linker Arm
      cr.move_to(0.7 * width, 0.45 * height)
      cr.line_to(0.6 * width, 0.55 * height)

    if step>=8: # rechter Arm
      cr.move_to(0.7 * width, 0.45 * height)
      cr.line_to(0.8 * width, 0.55 * height)

    if step>=9: # linkes Bein
      cr.move_to(0.7 * width, 0.7 * height)
      cr.line_to(0.6 * width, 0.8 * height)

    if step>=10: # rechtes Bein
      cr.move_to(0.7 * width, 0.7 * height)
      cr.line_to(0.8 * width, 0.8 * height)

    cr.stroke()

def on_clicked(button):
    text = word.get_label()
    guess = button.get_label()
    deactivated_list.append(button)
    button.set_sensitive(False)
    correct = False
    for i in range(len(secret)):
        if secret[i] == guess:
            correct = True
            text = text[:i] + guess + text[i + 1 :]

    word.set_label(text)
    if not correct:
        global step
        step += 1

    drawing_area.queue_draw()


reset()
append_letters()
drawing_area.set_draw_func(draw)
