from src.events import Events
from src.files.manager import Manager as FilesManager
from src.files.save import Save
from src.keyboard import Keyboard
from src.terminal import Terminal
from src.windows.window import Window
from src.components.component import Component

class Game:
    
    def __init__(self) -> None:
        Terminal.init()
        FilesManager.init()
        Save.init()
        Window.init()
        
        Keyboard.ON_KEY_PRESSED = self.on_key_pressed
        Keyboard.ON_LISTENER_EXIT = self.on_listener_exit

        Keyboard.thread_listener()
    
    def on_key_pressed(self, key):
        Component.keyboard_event(key)
        #Terminal.write_at(0, 0, str(key))
        Terminal.flush() # Force flush to get keys
        return Events.keyboard(key)
    
    def on_listener_exit(self):
        Terminal.close_screen()
    
    def run(self):
        if Save.IS_NEW_GAME:
            Window.show("INIT_GAME")