restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'
bill_subtotal = 148.58

# Greet User Function- Akib
def greet_user():
    print("Welcome to the NYC Tip Calculator! \n This calculator is for", restaurant_name, "at", restaurant_address, ".")
    print("--------------------------------------------------------------------------------")

# Get Bill Total- Akib
def get_bill_total():
    total = float(input("Enter your bill total: $))
    return total

# Calculate NY Tax- Stephanie
def calculate_ny_tax():
    print("pls complete")

# Get Tip Percentage- Arshia
def get_tip_percentage():
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

# Main Function: Calls all other functions- Arshia
def main():
    greet_user()
    subtotal = get_bill_total()
    ny_tax = calculate_ny_tax()
    tip, tip_value = get_tip_percentage()
    print("Calculating your total...")
    print("---------------------------------------- \n Here is your bill summary:")
    print("Subtotal: $", subtotal)
    print("NYC Tax (8.875%):", ny_tax)
    print("Tip (", tip_value, "):", tip)

main()
