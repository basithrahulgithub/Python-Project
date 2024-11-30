menu = {
    "Biryani": 220,
    "Pushka": 90,
    "Veg Biryani": 120,
    "Curd Rice": 60,
    "Lemon Rice": 80
}
print("Welcome To Cheap & Best Restaurant")
print("Biryani: Rs220\nPushka: Rs90\nVeg Biryani: Rs120\nCurd Rice: Rs60\nLemon Rice: Rs80")


item_1 = input("Enter the name of item you want to order: ")
order_total = 0

if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"Your {item_1} has been added to your order")
else:
    print(f"Ordered {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == 'Yes':
    item_2 = input("Enter the second item you want: ")
    if item_2 in menu:
        order_total = order_total + menu[item_2]
    else:
        print("Your Ordered item is not available yet!")
print(f"Total amount you want to pay {order_total}")