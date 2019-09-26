import classes
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def drink_decoder(obj):
    pass
