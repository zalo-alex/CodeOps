from src.components.state import State
from src.components.component import Component
from src.terminal import Terminal

class Text(Component):
    
    NAME = "TEXT"
    SELECTABLE = False
    
    __OPTIONS = {
        "underline": "\033[4m",
        "bold": "\033[1m",
    }
    
    def __init__(self, x, y, text, options = []):
        super().__init__(x, y)
        
        if type(text) is not str:
            self.text = text.sub(self)
        else:
            self.text = State(text).sub(self)
        
        self.options = options
    
    def display(self):
        prefix = "".join([self.__OPTIONS.get(option) for option in self.options if option in self.__OPTIONS])
        Terminal.write_at(self.x, self.y, prefix + self.text.value + "\033[0m")