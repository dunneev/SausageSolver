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
            self.rows.append(row)
                

