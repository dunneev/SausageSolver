class Observer:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Observable:
    def __init__(self, events):
        # maps event names to observers
        # str -> dict
        self.events = { event : dict()
                          for event in events }

    def get_observers(self, event):
        return self.events[event]
    def add_observer(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_observers(event)[who] = callback
    def remove_observer(self, event, who):
        del self.get_observers(event)[who]
    def dispatch(self, event, *data, **kwdata):
        for observer, callback in self.get_observers(event).items():
            callback(*data, **kwdata)