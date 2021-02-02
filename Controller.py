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

        self.view.btn_open.configure(command=self.open_file)
        self.view.btn_save.configure(command=self.save_file)
        

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
                self.model.grid.addRow(row)

        self.view.window.title(f"Sausage Solver - {filepath}")
        self.gridChanged(self.model.grid)

    
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



    def gridChanged(self, grid):
        self.view.setGridView(grid)

