from src.components.state import State
from src.components.component import Component
from src.terminal import Terminal

class Input(Component):
    
    NAME = "INPUT"
    SELECTABLE = True
    X_OFFSET = 3
    
    def __init__(self, x, y, value = ""):
        super().__init__(x, y)
        self.value = State(value).sub(self)
    
    def keyboard_event(self, key):
        if key == b'\x08':
            self.value.value = self.value.value[:-1]
        else:
            self.value.value += key.decode()
    
    def display(self):
        text = "{}[>] {}{} ".format('\033[7m' * self.selected, self.value.value, '\033[27m' * self.selected)
        Terminal.write_at(self.x, self.y, text)