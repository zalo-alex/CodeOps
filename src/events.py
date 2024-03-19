class Events:
    
    KEYBOARD_EXIT = 1
    KEYBOARD_UNDO = 2
    
    @staticmethod
    def keyboard(key):
        if key == b"\x03":
            print("Exit !")
            return Events.KEYBOARD_EXIT
        
        elif key == b'\x1a':
            print("Ctrl+Z")
            return Events.KEYBOARD_UNDO