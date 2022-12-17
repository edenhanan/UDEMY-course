# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L /N ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizza_price = 0

if size == "S":
    pizza_price = 15 
elif size == "M":
    pizza_price = 20
else:
    pizza_price = 25

if extra_cheese == "Y":
    pizza_price += 1


if add_pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    elif size == "M" or size == "L":
        pizza_price += 3
else:
    pizza_price += 0
    
print(f"your final bill is: ${pizza_price}.")