import tkinter as tk
from tkinter import OptionMenu, StringVar
from TileType import TileType
from Observer import Observable


class View:

    def set_grid_view(self, grid):

    SELECTED_TILE_COLOR = 'yellow'
    DEFAULT_TILE_COLOR = '#d9d9d9'
    TILE_WIDTH = 30
        r = 0
        for row in grid:
            self.fr_map.columnconfigure(r, weight=1, minsize=View.TILE_WIDTH)
            c = 0
            for tile in row:
                frame = tk.Frame(
                    master=self.fr_map,
                    relief=tk.RAISED,
                    borderwidth=1
                )

                canvas = tk.Canvas(master=frame)
                canvas.text = canvas.create_text(0,
                                0,
                                text=tile)

                canvas.bind("<Button-1>", self.tile_clicked)

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
        self.update_grid_text_position()


    def update_grid_text_position(self):
        """ reposition text in frame map frames """
        
        self.fr_map.update_idletasks()
        frame : tk.Frame
        for frame in self.fr_map.winfo_children():
            canvas : tk.Canvas
            for canvas in frame.winfo_children():
                canvas.coords(canvas.text, frame.winfo_width()/2,
                                frame.winfo_height()/2)
                print (canvas.coords(canvas.text))
                canvas.pack()      


    # def save_file(self):
    #     """Save the current file as a new file."""

    #     filepath = asksaveasfilename(

    #         defaultextension="txt",
    #         filetypes=[("Sausage Files", "*.csv"), ("All Files", "*.*")],
    #     )

    #     if not filepath:
    #         return

    #     with open(filepath, "w") as output_file:
    #         text = self.txt_edit.get("1.0", tk.END)
    #         output_file.write(text)

    #     self.window.title(f"Sausage Solver - {filepath}")

    


    def __init__(self, window):
        self.events = Observable(["tileClicked"])

        self.window = window
        self.fr_map = tk.Frame(window)
        self.fr_buttons = tk.Frame(window)
        self.fr_tile_editor = tk.Frame(window)


        # One row, which grows proportionally
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)


        # The main window has two columns, the first of which has a fixed width,
        # and this one, which will grow and shrink proportionally
        self.window.columnconfigure(1, weight=3, minsize=200)

        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=self.open_button_clicked)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=self.save_button_clicked)
        self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=1, column=0, sticky="ew", padx=5)

        self.tile_listbox = tk.Listbox(self.fr_tile_editor, selectmode='multiple')
        self.populate_tile_listbox()
        self.tile_listbox.pack()

        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        # self.fr_tile_editor.grid(row=1, column=0)
        self.fr_map.grid(row=0, column=1, sticky="nsew")

        self.fr_map.bind(sequence='<Configure>', func=self.on_configure)
        

    def populate_tile_listbox(self):
        for x in TileType:
            self.tile_listbox.insert("end", x.name)

    def on_configure(self, event):
        print("onConfigure")
        self.update_grid_text_position()
        # print(str(fr_map.winfo_children()))

    def tile_clicked(self, event):
        self.events.dispatch("tileClicked", event.widget)
        # tile : tk.Canvas
        # tile = event.widget
        # print(tile.configure())
        # tile.configure(bg='red')
    
    def open_button_clicked(self):
        pass

    def save_button_clicked(self):
        pass

