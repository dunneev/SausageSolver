from Observer import Observable

class Model:
    def __init__(self):
        self.events = Observable([])
        self.grid = []

    def addGridRow(self, row):
        self.grid.append(row)



        
