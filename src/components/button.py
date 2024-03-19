from src.components.state import State
from src.components.component import Component
from src.terminal import Terminal

class Button(Component):
    
    NAME = "BUTTON"
    SELECTABLE = True
    X_OFFSET = 1
    
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.text = text
    
    def keyboard_event(self, key):
        if key == b' ':
            print("CLICKED")
    
    def display(self):
        text = "{}[{}]{}".format('\033[7m' * self.selected, self.text, '\033[27m' * self.selected)
        Terminal.write_at(self.x, self.y, text)