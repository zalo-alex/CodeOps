from src.components.state import State
from src.components.component import Component
from src.terminal import Terminal

class ToggleButton(Component):
    
    NAME = "TOGGLE_BUTTON"
    SELECTABLE = True
    X_OFFSET = 3
    
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.text = text
        self.toggled = State(False).sub(self)
    
    def keyboard_event(self, key):
        if key == b' ':
            self.toggled.value = not self.toggled.value
    
    def display(self):
        text = "{}[{}] {}{}".format('\033[7m' * self.selected, "X" if self.toggled.value else " ", self.text, '\033[27m' * self.selected)
        Terminal.write_at(self.x, self.y, text)