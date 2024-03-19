import json
import os

class Manager:
    
    BASE_DIR = os.path.join(os.path.expanduser("~"), ".htterm")
    
    @staticmethod
    def file_path(filename):
        return os.path.join(Manager.BASE_DIR, filename)
            
    @staticmethod
    def read_json(filename):
        return json.loads(open(Manager.file_path(filename), "r").read())
    
    @staticmethod
    def write_json(filename, data):
        return open(Manager.file_path(filename), "w").write(json.dumps(data))
    
    @staticmethod
    def create_file(filename):
        os.makedirs(os.path.dirname(Manager.file_path(filename)), exist_ok=True)
        return open(Manager.file_path(filename), "w")
    
    @staticmethod
    def read_or_default(filename, default):
        try:
            return Manager.read_json(filename), False
        except:
            Manager.create_file(filename)
            return default, True
    
    @staticmethod
    def init():
        os.makedirs(Manager.BASE_DIR, exist_ok=True)