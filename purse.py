class Purse:

    def __init__(self, init_value):
        self.value = init_value
        self.wager = 0

    def collect(self, amount):
        self.value = self.value + amount
        return self.value

    def spend(self, amount):
        self.value = self.value - amount
        self.wager = self.wager + amount
        return self.value
