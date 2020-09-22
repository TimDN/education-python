def main():
    piggy_bank = PiggyBank()
    for i in range(10):
        coin = Coin(10, "sek")
        piggy_bank.add_coin(coin)
    for i in range(5):
        coin = Coin(5, "euro")
        piggy_bank.add_coin(coin)
    piggy_bank.display_content()

class Coin:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def change_currency(self, currency):
        self.currency = currency

    def print(self):
        print("{} {}".format(self.value, self.currency))

class PiggyBank:
    def __init__(self):
        self.storage = []

    def add_coin(self, coin):
        self.storage.append(coin)

    def display_content(self):
        print("Piggy bank contains these coins:")
        for coin in self.storage:
            coin.change_currency("dk")
            coin.print()

if __name__ == "__main__":
    main()
