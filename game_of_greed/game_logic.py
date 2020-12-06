from collections import Counter

class Banker:
    def __init__(self):
        self.shelved=0
        self.balance=0

    def shelf(self,value):
        self.shelved = value

    def bank(self):
        self.balance += self.shelved
        self.shelved =0
            
    def clear_shelf(self):
        self.shelved =0