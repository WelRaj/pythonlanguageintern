stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 140
}

my_stocks = {}

print("Hey! Let's track your stock money \n")

while True:
    stock_name = input("Type a stock name (like AAPL, TSLA): ").upper()

    if stock_name not in stock_prices:
        print("Oops! I don’t know that stock.\n")
        continue

    quantity = input(f"How many of {stock_name} do you have? ")

    if not quantity.isdigit():
        print("Please type a number!\n")
        continue

    quantity = int(quantity)
    my_stocks[stock_name] = quantity

    more = input("Wanna add more? (yes/no): ").lower()
    if more != 'yes':
        break

total = 0
print("\nHere's your stock stuff:")
for name, qty in my_stocks.items():
    price = stock_prices[name]
    value = price * qty
    print(f"{name}: {qty} x ${price} = ${value}")
    total += value

print("\nAll together, your stocks are worth: $", total)

save = input("Should I save this in a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio.txt", "w") as file:
        file.write("Your stock stuff:\n")
        for name, qty in my_stocks.items():
            price = stock_prices[name]
            value = price * qty
            file.write(f"{name}: {qty} x ${price} = ${value}\n")
        file.write(f"\nTotal: ${total}")
    print("Done! I saved it as portfolio.txt 😊")
