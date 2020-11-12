class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

adrian = Worker('Adrian Wloszynski', 50000)

anna = Worker('Anna Red', 500000)

print(adrian.lastName())

print(anna.lastName())

anna.giveRaise(.10)
print(anna.pay)