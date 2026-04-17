# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not found!")

print("Total Investment Value: $", total_investment)

# Save to file (optional)
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total_investment}")

print("Data saved to portfolio.txt")