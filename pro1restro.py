print("Welcome To RestroShubh")  #greeting
menu = { 
    'Pizza':100,
    'Burger':40,
    'Tea':10,
    'Coffee':90,
    'Meggi':50,

}
print("Here Is The Menu--")

print("Pizza:  100 Rs\nBurger: 40 Rs\nTea:    10 Rs\nCoffee: 90 Rs\nMeggi:  50 Rs")

order_total=0

item_1 = input("Enter Your Order From Menu --")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} is added in cart you want to add more :)")
else:
    print("Please order from the Menu :( ")


another_item = input("Do you want to add Another item ? (yes/no)")
if another_item == "yes":
    item_2= input("Enter the name of another item--")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print("Please order from the Menu :( ")    

print(f"The totle amount to be paid is {order_total}")
