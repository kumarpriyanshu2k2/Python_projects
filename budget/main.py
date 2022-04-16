import math


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def __str__(self):
        l1 = "*" * (15 - len(self.category) // 2) + self.category
        l1 += "*" * (30 - len(l1))
        content = l1 + "\n"
        for j in self.ledger:
            amount = str("{:.2f}".format(j["amount"]))
            description = j["description"]
            if len(description) > 23:
                description = description[:23]
            if len(amount) > 7:
                amount = amount[:7]
            content += description + " " * (30 - len(description) - len(amount)) + amount + "\n"
        content += f"Total: {self.balance}"
        return content

    def deposit(self, amount, description=""):
        self.ledger += [{"amount": amount, "description": description}]
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger += [{"amount": -1 * amount, "description": description}]
            self.balance -= amount
            self.spent += amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.category}"):
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount


def create_spend_chart(categories):
    total = 0
    bar = []
    name = []
    content = "Percentage spent by category\n"
    l1 = "100| "
    l2 = " 90| "
    l3 = " 80| "
    l4 = " 70| "
    l5 = " 60| "
    l6 = " 50| "
    l7 = " 40| "
    l8 = " 30| "
    l9 = " 20| "
    l10 = " 10| "
    l11 = "  0| "
    lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11]

    for cat in categories:
        total += cat.spent

    for category in categories:
        bar += [math.ceil(10 * category.spent / total)]
        name += [category.category]
    for i in bar:
        for k in range(len(lines)):
            if k < 11 - i:
                lines[k] += "   "
            else:
                lines[k] += "o  "

    for line in lines:
        line += "\n"
        content += line
    content += " " * 4 + "-" * (3 * len(name) + 1) + "\n"
    n = max([len(nm) for nm in name])
    name=[i+" "*(n-len(i)) for i in name]
    lc=[]
    for h in range(n):
        lc+=[" "*5]
        for m in name:
            lc[h]+=m[h]+" "*2
    for l in lc:
        content+=l+"\n"


    return content


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
