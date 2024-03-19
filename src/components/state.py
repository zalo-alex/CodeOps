class State:
    
    def __init__(self, value) -> None:
        self._value = value
        self.subs = []
    
    def sub(self, component):
        self.subs.append(component)
        return self
    
    def display_subs(self):
        for sub in self.subs:
            sub.display()
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        self.display_subs()