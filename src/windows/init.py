from src.components.button import Button
from src.components.toggle_button import ToggleButton
from src.display import Display
from src.windows.window import Window
from src.components.text import Text
from src.components.component import Component
from src.components.input import Input

class Init(Window):
    
    NAME = "INIT_GAME"
    COMPONENTS = [
        Text(2, 2, "CodeOps", ["underline", "bold"]),
        ToggleButton(2, 4, "VM ?"),
        ToggleButton(2, 5, "Cloud ?"),
        Text(2, 7, "RAM (Mo):"),
        (input := Input(2, 8)),
        Button(2, 10, "Start"),
        
        Text(30, 2, "Keys:", ["underline", "bold"]),
        Text(30, 4, "Select Next:      Down Arrow Key / Tab"),
        Text(30, 5, "Select Previous:  Up Arrow Key"),
        Text(30, 6, "Interract:        Space Bar"),
    ]
    
    @classmethod
    def display(cls):
        Component.display_all(cls.COMPONENTS)