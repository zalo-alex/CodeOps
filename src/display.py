from src.windows.window import Window

class Display:
    
    @staticmethod
    def center_x(text, y, component):
        return component(Display.center_with(text + " " * component.X_OFFSET, Window.W), y, text)
    
    @staticmethod
    def center_with(text, width):
        return (width - len(text)) // 2