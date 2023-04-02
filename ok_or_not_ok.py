import microbit as mb


def go():
    mb.button_b.was_pressed()
    while not mb.button_b.was_pressed():
        mb.display.show(mb.Image.YES)
        mb.sleep(500)
        mb.display.show(mb.Image.NO)
        mb.sleep(500)


if __name__ == '__main__':
    go()
