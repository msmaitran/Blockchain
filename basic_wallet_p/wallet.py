import requests
import json

req = requests.get('http://localhost:5000/chain')

data = req.json()
chain = data['chain']

id = input("Please enter an id: ")

transactions = []
coins_mined = 0

for block in chain:
    for transaction in block.get('transactions'):
        if transaction['recipient'] == id:
            coins_mined += transaction['amount']
            transactions.append(transaction)

print(f"Total current balance for {id}: {coins_mined}\n")
print(f"List of all transactions for {id}: ")
for transaction in transactions:
    sender = transaction['sender']
    recipient = transaction['recipient']
    amount = transaction['amount']
    print(f"Sender: {sender}\nRecipient: {recipient}\nAmount: {amount}\n")