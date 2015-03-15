#!/usr/bin/env python3

import fstimer.timer
from gi.repository import Gtk

if __name__ == '__main__':
    pytimer = fstimer.timer.PyTimer()
    #These next two lines are to get icons on stock buttons in windows
    settings = Gtk.Settings.get_default()
    settings.props.gtk_button_images = True
    Gtk.main()


