import datetime

class Client:
  number_of_clients = 0

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.accounts = []
    Client.number_of_clients += 1

  def add_account(self, account):
    self.accounts.append(account)

class Account:
  def __init__(self, number, currency, balance = 0.0): # if we don't provide value for balance, it automatically assigns 0.0
    self.number = number
    self.currency = currency
    self.balance = balance
    self.transactions = []

  def make_deposit(self, amount, note):
    self.transactions.append(Transaction(self.currency, amount, note)) #we need to store previous transactions, as in bank
    self.balance += amount

  def make_withdrawal(self, amount, note):
    self.transactions.append(Transaction(self.currency, -amount, note)) # currency is taken from Account class (previously defined)
    self.balance -= amount

class Transaction:
  def __init__(self, currency, amount, note):
    self.currency = currency
    self.amount = amount
    self.note = note
    self.time_stamp = datetime.datetime.now() # in this case we don't allow to add time, because it is not defined it init methods parameters - for each transaction it is strictly assigned as this - datetime.datetime.now()

#adding clients
clients = []
clients.append(Client('1234', 'Anna'))
clients.append(Client('3513', 'Oscar'))
clients.append(Client('7442', 'Jenifer'))

#adding accounts
clients[0].add_account(Account('EE78655585465', 'EUR')) #New account (using class Account) is created and added to class Clients to object (client) Anna (accesses thru list clients[0]) using method add_account
clients[0].add_account(Account('US49526596564', 'USD'))
clients[0].add_account(Account('JP85522254500', 'JPY', 2000))
clients[1].add_account(Account('PL55584446226', 'PLN'))
clients[2].add_account(Account('SE63362184795', 'SEK', 51.23))

#making transactions
clients[0].accounts[0].make_deposit(1200, 'Salary')
clients[0].accounts[0].make_withdrawal(50, 'Grocery')


print(f'We have {Client.number_of_clients} clients in our bank:')

print(clients[1].id) #this is how we can access specific objects attribute - addint it to the list and then accessing it
print(clients[0].accounts[0].number) # accessing specific account parameter for specific client

for client in clients:
  print(f'Client {client.name} ({client.id}) has the following accounts:')
  for account in client.accounts:
    print(f'  {account.number} ({account.currency}) {account.balance}')
    for transaction in account.transactions:
      print(f'     {transaction.time_stamp} {transaction.amount}')
