import os
import sys

class Terminal:
    
    @staticmethod
    def get_width():
        return os.get_terminal_size().columns
    
    @staticmethod
    def get_height():
        return os.get_terminal_size().lines
    
    @staticmethod
    def enable_raw_mode():
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

    @staticmethod
    def disable_raw_mode():
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 4)
    
    @staticmethod
    def write_flush(text):
        Terminal.write(text)
        Terminal.flush()
        
    @staticmethod
    def write(text):
        sys.stdout.write(text)
        
    @staticmethod
    def flush():
        sys.stdout.flush()
        
    @staticmethod
    def write_at(x, y, text):
        Terminal.write("\x1b[" + str(y + 1) + ";" + str(x + 1) + "H" + text)
    
    @staticmethod
    def open_screen():
        Terminal.enable_raw_mode()
        Terminal.write_flush("\033[?1049h")
        Terminal.write_flush("\x1b[0;0H")
        
    @staticmethod
    def close_screen():
        Terminal.disable_raw_mode()
        Terminal.write_flush("\033[?1049l")
        Terminal.write_flush("\x1b[u")
        
    @staticmethod
    def clear():
        Terminal.write_flush("\x1b[0;0H")
        Terminal.write_flush("\033[2J")
        
    @staticmethod
    def init():
        Terminal.open_screen()