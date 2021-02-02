class EventEmitter:
    map = {}
    def on(self, event, handler):
        if not callable(handler):
            raise "TypeError: Handler must be function"
            
            
        if (self.map.get(event, None) != None):
            self.map[event].append(handler)
        else:
            self.map[event] = []
            self.map[event].append(handler)
    def emit(self, event, args):
        if not self.map[event]:
            return
        
        for i in self.map[event]:
            i(event, args)
        
    def remove(self, event, handler):
        if not handler:
            self.map[event] = []
        else:
            j = 0
            for i in self.map[event]:
                
                if i == handler:
                    self.map[event].pop(j)
                else:
                    pass
                j = j+1
        
    
