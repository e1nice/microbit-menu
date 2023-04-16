import microbit as mb


class Menu:
    items = [[mb.Image.NO, None]]
    
    @classmethod
    def add(cls, image, function):
        cls.items.append([image, function])

    @classmethod
    def go(cls):
        mb.button_a.was_pressed()
        mb.button_b.was_pressed()
        max_index = len(cls.items) - 1
        end = False
        index = 0
        while not end:
            mb.display.show(cls.items[index][0])
            if mb.button_a.was_pressed():
                mb.button_b.was_pressed()
                if index < max_index:
                    index += 1
                else:
                    index = 0
            if mb.button_b.was_pressed():
                function = cls.items[index][1]
                if callable(function):
                    mb.display.clear()
                    function()
                    mb.button_a.was_pressed()
                    mb.button_b.was_pressed()
                else:
                    end = True
        mb.display.clear()
