from src.terminal import Terminal

class Component:
    
    NAME = "DEFAULT_COMPONENT"
    SELECTABLE = False
    X_OFFSET = 0
    COMPONENTS = []
    CURRENT_SELECTED = 0
    
    @classmethod
    def keyboard_event(cls, key):     
        
        if cls.NAME != "DEFAULT_COMPONENT": return
        
        if key == b'\t' or key == b'\xe0P':
            Component.select(1)
        elif key == b'\xe0H':
            Component.select(-1)
        else:
            Component.COMPONENTS[Component.CURRENT_SELECTED].keyboard_event(key)
    
    @staticmethod
    def select(direction):
        
        while (not (component := Component.COMPONENTS[Component.CURRENT_SELECTED]).SELECTABLE) or component.selected:
            component.selected = False
            component.display()
            
            Component.CURRENT_SELECTED += direction
            Component.CURRENT_SELECTED %= len(Component.COMPONENTS)

        component.selected = True
        component.display()
    
    @staticmethod
    def clear():
        Component.COMPONENTS = []
        Component.CURRENT_SELECTED = 0
    
    @staticmethod
    def display_all(components):
        Component.COMPONENTS = components
        for component in components:
            component.display()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.selected = False
    
    def display(self):
        Terminal.write_at(self.x, self.y, f"Empty Component. ({self.NAME})")