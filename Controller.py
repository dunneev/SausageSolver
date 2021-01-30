from Model import Model
from View import View
from Observer import Observer, Observable


class Controller:
    def __init__(self, window):

        self.model = Model()
        self.view = View(window)

                
        # self.model.events.add_observer("modelChanged", Observer("controllerObserver"), self.onModelChanged())
        # self.model.changeModel()

        self.view.btn_open.configure(command=self.open_file)
        self.view.btn_save.configure(command=self.save_file)
        

    def open_file(self):
        self.view.open_file()

    
    def save_file(self):
        self.view.save_file()

