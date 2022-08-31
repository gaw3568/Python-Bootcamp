print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_price = 0

S_pizza = 15
M_pizza = 20
L_pizza = 25

pep_s_pizza = 2
pep_m_l_pizza = 3
add_cheese = 1

if size == "S":
    print()
    if add_pepperoni == "Y":
        total_price = S_pizza + pep_s_pizza
    else:
        total_price = S_pizza
    if extra_cheese == "Y":
        total_price += add_cheese
    print(f"Total price is {total_price}")

elif size == "M":
    if add_pepperoni == "Y":
        total_price = M_pizza + pep_m_l_pizza
    else:
        total_price = M_pizza
    if extra_cheese == "Y":
        total_price += add_cheese
    print(f"Total price is {total_price}")

elif size == "L":
    if add_pepperoni == "Y":
        total_price = L_pizza + pep_m_l_pizza
    else:
        total_price = L_pizza
    if extra_cheese == "Y":
        total_price += add_cheese
    print(f"Total price is {total_price}")

else:
    print(f"Total price is {total_price}")