import microbit as mb
from menu import Menu
import ok_or_not_ok
import emotions


Menu.add(mb.Image.YES, ok_or_not_ok.go)
Menu.add(mb.Image.HAPPY, emotions.go)
Menu.go()
