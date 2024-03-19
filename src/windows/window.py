from src.terminal import Terminal
from src.components.component import Component

class Window:
    
    NAME = "DEFAULT_WINDOW"
    COMPONENTS = []
    
    CURRENT = None
    H = 1
    W = 1
    CENTER_X = 0
    CENTER_Y = 0
    
    @staticmethod
    def init():
        Window.W = Terminal.get_width()
        Window.H = Terminal.get_height()
        Window.CENTER_X = int(Window.W / 2)
        Window.CENTER_Y = int(Window.H / 2)
        Window.__import_windows()
    
    @staticmethod
    def __import_windows():
        import src.windows.init as _
    
    @staticmethod
    def show(name):
        for w in Window.__subclasses__():
            if w.NAME == name:
                w.display()
                Window.CURRENT = w
                return
        raise Exception(f"Window {name} not found.")
    
    @classmethod
    def display(cls):
        Terminal.clear()
        Terminal.write_flush(f"Empty Window. ({cls.NAME})")
        Component(2, 2).display()