import msvcrt
import sys
import threading

class Keyboard:
    
    ON_KEY_PRESSED = None
    ON_LISTENER_EXIT = None
    BUFFER = b""
    
    @staticmethod
    def thread_listener():
        threading.Thread(target=Keyboard.listener).start()
        
    @staticmethod
    def listener():
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                
                Keyboard.BUFFER += key
                
                if Keyboard.ON_KEY_PRESSED is not None:
                    if (key == b"\xe0"):
                        key += msvcrt.getch()
                    
                    result = Keyboard.ON_KEY_PRESSED(key)
                    
                    if result == 1:
                        if Keyboard.ON_LISTENER_EXIT is not None: 
                            Keyboard.ON_LISTENER_EXIT()
                        break
                    
    @staticmethod
    def clear_buffer():
        Keyboard.BUFFER = ""