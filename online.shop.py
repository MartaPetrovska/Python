import datetime

class Client:
    def __init__(self, name, surname, money):
        self.name = name
        self.surname = surname
        self.money = money
        self.transactions = []

    def buy_items(self, items):
        total_cost = sum(item.price for item in items)
        if self.money >= total_cost:
            self.money -= total_cost
            transaction = Transaction(total_cost, items)
            self.transactions.append(transaction)
            print(f"{self.name} bought {[item.name for item in items]} for ${total_cost}")
        else:
            print(f"Not enough money to buy {[item.name for item in items]}")

class Items:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Transaction:
    transaction_counter = 0

    def __init__(self, amount, items):
        self.number = Transaction.transaction_counter
        Transaction.transaction_counter += 1
        self.amount = amount
        self.items = items
        self.time_stamp = datetime.datetime.now()

# Adding clients
clients = [
    Client('Maria', 'Jones', 200),
    Client('Laura', 'Miller', 100),
    Client('Eric', 'Smith', 50)
]

# Adding items
items = [
    Items(123, 'Kiwi', 2),
    Items(456, 'Apple', 1),
    Items(789, 'Orange', 3)
]

# Buying items
clients[0].buy_items([items[0], items[1], items[2]])  # Maria buys Banana, Apple, and Orange
clients[1].buy_items([items[1], items[2]])  # Laura buys Apple and Orange
clients[2].buy_items([items[0]])  # Eric buys Banana

# Printout of data
for client in clients:
    print(f'Client: {client.name} {client.surname}, Remaining Money: ${client.money}')
    for transaction in client.transactions:
        print(f'  Transaction {transaction.number}: -${transaction.amount}, Date: {transaction.time_stamp}')
        for item in transaction.items:
            print(f'    Item: {item.name}, Price: ${item.price}')
