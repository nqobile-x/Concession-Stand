# Dictionary menu for a food cart
menu = {
    "pizza": 3.00,
    "burger": 2.50,
    "fries": 1.50,
    "kota": 17.00,
    "pap": 10.00
}

# Cart array for food items
cart = []

# Total price tracker
total = 0

# Display menu
print("----Food Menu----")
for key, value in menu.items():
    print(f"{key:10}: R{value:.2f}")
print("-----------------")

# Add items to cart
while True:
    food = input("Enter food item to add to cart (or q to finish): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found in menu. Please try again.")

# Display order summary
print("\n--------Your Order--------")
for food in cart:
    total += menu.get(food)
    print(f"{food}: R{menu.get(food):.2f}")

print(f"\nTotal: R{total:.2f}")
