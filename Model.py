from Observer import Observable
from TileType import TileType


class Model:

    def __init__(self):
        self.events = Observable([])
        self.grid = self.Grid()

    class Grid:
        def __init__(self):
            self.rows = []

        def __iter__(self):
            return (row for row in self.rows)

        def addRow(self, row):
            for tile in row:
                tile = self.Tile(TileType.GROUND, TileType.SAUSAGE)
            self.rows.append(row)
                
        class Tile:
            
            def __init__(self, *tileTypes):
                self.type = tileTypes   

