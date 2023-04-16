"""Example how to use the menu on a micro:bit

* Upload the files menu.py, emotions.py, ok_or_not_ok.py and main.py to the micro:bit.
* Start the code by pressing the reset button.
* Use button A to select a menu option and button B to start this option.
* Selecting the X option will exit the menu program.
* The other two options repeat a sequence on the display, where button B exits to the menu.

"""

import microbit as mb
from menu import Menu
import ok_or_not_ok
import emotions


Menu.add(mb.Image.YES, ok_or_not_ok.go)
Menu.add(mb.Image.HAPPY, emotions.go)
Menu.go()
