stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

# Create a simple list of blocks of stock. Make them tuples with ticker symbols, number of shares, dates and price.

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 ),
    ( 'EK', 150, '5-jul-1997', 59 )
]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# Example output for one block: I purchased General Electric stock for $4800

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

"""------ GE ------
100 shares at 48 dollars each on 01-jul-1998
200 shares at 56 dollars each on 10-sep-2001

Total value of stock in portfolio: $16000
"""

for purchase in purchases:
    shares = purchase[1]
    ticker = purchase[0]
    companyName = stockDict[ticker]
    price = purchase[-1]
    total =+ shares * price
    sentence = f"I purchased {companyName} stock for ${total}"
    print(sentence)

total = 0

for ticker, companyName in stockDict.items():
    print(f"------ {ticker} ------")
    for purchase in purchases:
        if purchase[0] == ticker:
            shares = purchase[1]
            date = purchase[2]
            price = purchase[-1]
            total += price * shares
            sentence = f"{shares} shares at ${price} each on {date}"
            print(sentence)
print(f"Total value of stock in portfolio: ${total}")