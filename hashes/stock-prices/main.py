"""
Stock Prices Calculator
"""

hashset = set()

print('Size', len(hashset))

stock_prices = []
with open('stock_prices.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day, price])

print(stock_prices)
print(stock_prices[0])

# Find stock price on Marh 9
for item in stock_prices:
    if item[0] == 'march 9':
        print(item[1])

# Implement hash table
def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

print(get_hash('march 9'))