from Observer import Observable

class Model:
    def __init__(self):
        self.money = Observable(['moneyChanged'])

    def changeMoney(self):
        self.money.dispatch("moneyChanged", "money changed in model")
        
