VAT = 0.25 # Standard swedish tax rate
DELIVERY_FEE = 50 # Foodoora delivery fee
MAX_PIZZA_ORDER = 10
PIZZA_PRICE = 99

customer_name = str(input("What is your name: "))

while True:
    number_of_pizzas = int(input("How many pizzas?: "))
    if number_of_pizzas > MAX_PIZZA_ORDER:
        print(f"Sorry, you can only order a maximum of {MAX_PIZZA_ORDER} pizzas.")
        print("Please try again with a valid number of pizzas.")
    else:
        break

pizza_subtotal = number_of_pizzas * PIZZA_PRICE
vat_amount = pizza_subtotal * VAT
total_prize = pizza_subtotal + vat_amount + DELIVERY_FEE

print(f"Customer: {customer_name}")
print(f"Pizzas: {number_of_pizzas} x {PIZZA_PRICE} kr")
print(f"Delivery fee: {DELIVERY_FEE} kr")
print(f"VAT (25%): {vat_amount} kr")
print(f"Total price: {total_prize} kr")
print("Your order will be done in 10-15 minutes! Thank you for your order :)")
