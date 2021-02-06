from Observer import Observable
from TileType import TileType


class Model(Observable):

    def __init__(self):
        self.grid = self.Grid()

    class Grid:
        def __init__(self):
            self.rows = []


        def __iter__(self):
            return (row for row in self.rows)

        def tile_at_coordinates(self, row, col):
            return self.rows[row][col]
        
        def tile_at_index(self, tileIndex):
            row_count = self.rows.__len__()
            # col_count = self.rows[0]__len__()

            row = int (tileIndex / row_count)
            col = tileIndex % row_count
            return self.rows[row][col]
            

        def add_row(self, row):
            tileList = []
            colCount = 0
            for tile in row:
                tileObject = self.Tile(self.rows.__len__(), colCount, tile)
                tileList.append(tileObject)
                colCount += 1

            self.rows.append(tileList)

        def toggle_tile_selected(self, row, col):
            self.tile_at_coordinates(row, col).is_selected = not self.tile_at_coordinates(row, col).is_selected

            

        class Tile:
            def __init__(self, row, col, TileType):
                self.row = row
                self.col = col
                self.tile_type = TileType
                self.is_selected = False

    

    

    