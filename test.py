
# Test file
from main import *
App = EventEmitter()

def handler1(event, arg):
    print("Handler one got:", event, arg)
    
    
App.on('message', handler1)
App.emit('message', "Hello event World")