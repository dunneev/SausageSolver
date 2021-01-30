from Model import Model
from View import View
from Observer import Observer, Observable


class Controller:
    def __init__(self, window):

        self.model = Model()
        self.view = View(window)

                
        self.model.money.add_observer("moneyChanged", Observer("controllerObserver"), self.onMoneyChanged())
        self.model.changeMoney()

        self.view.btn_open.configure(command=self.open_file)
        self.view.btn_save.configure(command=self.save_file)
        

    def open_file(self):
        self.view.open_file()

    
    def save_file(self):
        self.view.save_file()

    def onMoneyChanged(self):
        print ("Alert: Money changed")
    # def AddMoney(self):
    #     self.model.addMoney(10)

    # def RemoveMoney(self):
    #     self.model.removeMoney(10)

    # def MoneyChanged(self, money):
    #     self.View.SetMoney(money)
