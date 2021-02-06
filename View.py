import tkinter as tk
from tkinter import OptionMenu, StringVar
from TileType import TileType
from Observer import Observable


class View(Observable):


    SELECTED_TILE_COLOR = 'yellow'
    DEFAULT_TILE_COLOR = '#d9d9d9'
    TILE_WIDTH = 30

    def create_grid_view(self, grid):

        r = 0
        for row in grid:
            self.fr_map.columnconfigure(r, weight=1, minsize=View.TILE_WIDTH)
            self.fr_map.rowconfigure(r, weight=1, minsize=View.TILE_WIDTH)
            c = 0
            for tile in row:
                frame = tk.Frame(
                    master=self.fr_map,
                    relief=tk.RAISED,
                    borderwidth=1)


                
                canvas = tk.Canvas(master=frame)
                canvas.text = canvas.create_text(0, 0,text=tile.tile_type)
                canvas.row = r
                canvas.col = c
                canvas.bind("<Button-1>", self.on_tile_click)
                canvas.pack()


                # # Dropdown
                # variable = StringVar(frame)
                # variable.set(tile)  # default value


                # tileOptions = [tile.name for tile in TileType]
                # print (tileOptions)
                # tileOptionMenu = OptionMenu(frame, variable, variable.get(), *tileOptions)
                # tileOptionMenu.pack(fill='both', expand='true')

                # Set propagate to false to prevent frames from wrapping content
                frame.propagate(0)
                frame.grid(row=r, column=c, sticky="nsew")

                # label = tk.Label(master=frame, text=col)
                # label.pack()

                c += 1
            r += 1
        self.update_grid_view(grid)

    def update_grid_view(self, grid):
        tile_index = 0

        # Update frame size for use in for loop
        self.fr_map.update_idletasks()

        frame : tk.Frame
        for frame in self.fr_map.winfo_children():
            canvas : tk.Canvas
            for canvas in frame.winfo_children():

                # Center canvas
                canvas.coords(canvas.text, frame.winfo_width()/2, frame.winfo_height()/2)   
                if grid.tile_at_index(tile_index).is_selected:
                    canvas.configure(background=View.SELECTED_TILE_COLOR)
                else:
                    canvas.configure(background=View.DEFAULT_TILE_COLOR)


                tile_index += 1



    def __init__(self, window):
    
        super().__init__(['on_tile_click', 'on_resize', 'on_open_click', 'on_save_click'])

        self.window = window
        self.fr_map = tk.Frame(window)
        self.fr_options_panel = tk.Frame(window)
        self.fr_buttons = tk.Frame(self.fr_options_panel)
        self.fr_tile_editor = tk.Frame(self.fr_options_panel)


        # One row, which grows proportionally
        self.window.rowconfigure(0, weight=1, minsize=200)


        # The main window has two columns, the first of which has a fixed width:
        self.window.columnconfigure(0, minsize=200)

        # and this one, which will grow and shrink proportionally
        self.window.columnconfigure(1, weight=3, minsize=200)

        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=self.on_open_click)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=self.on_save_click)
        self.btn_open.grid(row=0, column=0, sticky='ew')
        self.btn_save.grid(row=1, column=0, sticky='ew')

        self.tile_listbox = tk.Listbox(self.fr_tile_editor, selectmode='multiple', height=len(TileType))
        self.populate_tile_listbox()
        self.tile_listbox.pack()

        self.fr_buttons.grid(row=0, column=0)
        self.fr_tile_editor.grid(row=1, column=0, sticky='ns')
        self.fr_options_panel.grid(row=0, column=0, sticky='ns')
        self.fr_map.grid(row=0, column=1, sticky="nsew")

        self.fr_map.bind(sequence='<Configure>', func=self.on_configure)
        

    def populate_tile_listbox(self):
        for x in TileType:
            self.tile_listbox.insert("end", x.name)

    def on_configure(self, event):
        self.dispatch("on_resize")

    def on_tile_click(self, event):
        self.dispatch("on_tile_click", 
                        widget=event.widget, 
                        row=event.widget.row, 
                        col=event.widget.col)

    def on_open_click(self):
        self.dispatch("on_open_click")

    def on_save_click(self):
        self.dispatch("on_save_click")