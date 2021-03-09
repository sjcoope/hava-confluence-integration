
class HavaSources:
    def __init__(self, array):
        self.items = []
        
        for item in array:
            self.items.append(HavaSource(item))
    
    def __iter__(self):
        return self.items.__iter__()

class HavaSource:
    def __init__(self, hava_source):
        self.id = hava_source["id"]
        self.name = hava_source["display_name"]
        self.last_sync = hava_source["last_sync"]
        self.environments = []
