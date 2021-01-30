from Model import Model
from View import View


class Controller:
    def __init__(self, window):

        self.model = Model()
        self.view = View(window)
        # self.model.myMoney.addCallback(self.MoneyChanged)
        # self.view1 = View(root)
        # self.view2 = ChangerWidget(self.view1)
        # self.view2.addButton.config(command=self.AddMoney)
        # self.view2.removeButton.config(command=self.RemoveMoney)
        # self.MoneyChanged(self.model.myMoney.get())
        self.view.btn_open.configure(command=self.open_file)
        self.view.btn_save.configure(command=self.save_file)

    def open_file(self):
        self.view.open_file()

    
    def save_file(self):
        self.view.save_file()


    # def AddMoney(self):
    #     self.model.addMoney(10)

    # def RemoveMoney(self):
    #     self.model.removeMoney(10)

    # def MoneyChanged(self, money):
    #     self.View.SetMoney(money)
