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

    # def AddMoney(self):
    #     self.model.addMoney(10)

    # def RemoveMoney(self):
    #     self.model.removeMoney(10)

    # def MoneyChanged(self, money):
    #     self.View.SetMoney(money)
