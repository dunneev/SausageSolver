from Model import Model
from View import View
from Observer import Observer, Observable
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv



class Controller:
    def __init__(self, window):

        self.model = Model()
        self.view = View(window)

                
        # self.model.events.add_observer("modelChanged", Observer("controllerObserver"), self.onModelChanged())
        # self.model.changeModel() 
            
        self.addViewObservers()

        
    def addViewObservers(self):
        self.view.add_observer("on_tile_click", Observer("tile_observer"), self.on_tile_click)
        self.view.add_observer("on_resize", Observer("resize_observer"), self.on_resize)
        self.view.add_observer("on_open_click", Observer("open_observer"), self.open_file)
        self.view.add_observer("on_save_click", Observer("save_observer"), self.save_file)


    def open_file(self):
        """Open a file for editing & solving."""
        filepath = askopenfilename(
            filetypes=[("Sausage Files", "*.ssg"), ("All Files", "*.*")]
        )

        if not filepath:
            return

        with open(filepath, newline="") as file:
            
            reader = csv.reader(file, )

            for row in reader:
                row = [tile.upper() for tile in row] 
                self.model.grid.add_row(row)

        self.view.window.title(f"Sausage Solver - {filepath}")
        self.view.create_grid_view(self.model.grid)

    
    def save_file(self):
        """Save the current file as a new file."""

        filepath = asksaveasfilename(

            defaultextension=".ssg",
            filetypes=[("Sausage Files", "*.ssg"), ("All Files", "*.*")],
        )
        

        with open(filepath, "w") as output_file:
            # text = self.txt_edit.get("1.0", tk.END)
            csvWriter = csv.writer(output_file)
            for row in self.model.grid:
                csvWriter.writerow(row)
            

        self.view.window.title(f"Sausage Solver - {filepath}")

    

    def on_tile_click(self, *data, **kwdata):
        print ("tile clicked")
        self.model.grid.toggle_tile_selected(kwdata.get("row"), kwdata.get("col"))    
        self.view.update_grid_view(self.model.grid)

    def on_resize(self):
        self.view.update_grid_view(self.model.grid)

