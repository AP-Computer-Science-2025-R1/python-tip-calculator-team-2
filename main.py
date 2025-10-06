restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'

import math

# Greet User Function- Akib
def greet_user():
    print("Welcome to the NYC Tip Calculator! \n This calculator is for", restaurant_name, "at", restaurant_address, ".")
    print("--------------------------------------------------------------------------------")

# Get Bill Total- Akib
def get_bill_total():
    global bill_subtotal
    total = float(input("Enter your bill total: $"))
    bill_subtotal = total
    if total > 0:
        return total
    else:
        print("Invalid input, please try again and put in a proper bill amount.")
        return get_bill_total()
    return total
    return bill_subtotal

# Calculate NY Tax- Stephanie
def calculate_ny_tax():
    global bill_subtotal
    ny_tax = bill_subtotal * 0.08875
    return ny_tax

# Get Tip Percentage- Arshia
def get_tip_percentage():
    global bill_subtotal
    global total_tip
    tip_amount = input("How much would you like to tip? \n 1) 15% \n 2) 18% \n 3) 20% \n 4) Custom Amount \n Enter your choice: ")
    if tip_amount == "1":
        tip_value = "15%"
        total_tip = bill_subtotal * 0.15
    elif tip_amount == "2":
        tip_value = "18%"
        total_tip = bill_subtotal * 0.18
    elif tip_amount == "3":
        tip_value = "20%"
        total_tip = bill_subtotal * 0.20
    elif tip_amount == "4":
        custom_tip_amount = float(input("Please input your specific custom tip amount: "))
        tip_value = custom_tip_amount
        total_tip = bill_subtotal * custom_tip_amount / 100
    else:
        print("Incorrect option provided. Please pick a number given.")
        return get_tip_percentage()
    return total_tip, tip_value

# Additional Challenge- Arshia
def split_bill():
    global bill_subtotal
    global total_tip
    split_q = input("Would you like to split the bill? Please answer in 'yes' or 'no': ")
    split_q_a = split_q.lower()
    if split_q_a == "yes":
        split_no = int(input("How many people are you splitting it amongst?: "))
        if split_no > 0:
            split_number = split_no
            split_total = bill_subtotal / split_number
        else:
            print("Invalid input, please try again.")
            return split_bill()
    elif split_q_a == "no":
        split_total = bill_subtotal
        split_number = 1
    else:
        print("Invalid input, please answer in yes or no!")
        return split_bill()
    return split_number, split_total

def rounding():
    global bill_subtotal
    round_q = input("Would you like to round up to the nearest dollar? Please type 'yes' or 'no': ")
    round_final = round_q.lower()
    if round_final == "yes":
        bill_subtotal = math.ceil(bill_subtotal)
    elif round_final == "no":
        bill_subtotal = bill_subtotal
    else:
        print("Invalid input, try again.")
        return rounding()

# Main Function: Calls all other functions- Arshia
def main():
    global bill_subtotal
    global total_tip
    greet_user()
    subtotal = get_bill_total()
    ny_tax = calculate_ny_tax()
    tip, tip_value = get_tip_percentage()
    split_number, split_total = split_bill()
    rounding()
    print("Calculating your total...")
    print("---------------------------------------- \n Here is your bill summary:")
    print("Subtotal: $", subtotal)
    print("NYC Tax (8.875%):", ny_tax)
    print("Tip (", tip_value, "):", tip)
    print("You will be splitting your bill amongst", split_number, "person/people. Your total for each person without tip will be $", split_total)
    print("Your absolute total without division will be:", bill_subtotal + total_tip + ny_tax)

main()
