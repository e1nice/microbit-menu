import microbit as mb


def go():
    mb.button_b.was_pressed()
    while not mb.button_b.was_pressed():
        mb.display.show(mb.Image.HAPPY)
        mb.sleep(1000)
        mb.display.show(mb.Image.SAD)
        mb.sleep(1000)
        mb.display.show(mb.Image.ANGRY)
        mb.sleep(1000)


if __name__ == '__main__':
    go()
