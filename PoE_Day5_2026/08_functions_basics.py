def place_order(item):
    print(f"Order placed: your order is {item}")
    
def get_order():
    print("Prepaqring order....")
    return "Collect your order"

def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    total_price = (base_price + len(item)) * VAT


my_food = input("What would you like?: ")
place_order(my_food)

print(get_order())

order_total = calculate_total(my_food)
print(f"Your order cost: R{round(order_total, 2)}")
