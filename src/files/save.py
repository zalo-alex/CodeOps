from src.files.manager import Manager

class Save:
    
    IS_NEW_GAME = False
    SAVE_DATA = {}
    
    @staticmethod
    def init():
        Save.SAVE_DATA, Save.IS_NEW_GAME = Manager.read_or_default("game-save.json", {
            "level": 0
        })