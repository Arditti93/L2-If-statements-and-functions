
# Activity 2
# -------------------------

age = 16
country = "Italy"

if age > 17 and country == "UK":
    print("Yes I can serve you")
elif age > 17 and country != "UK":
    print("Where are you?")
else:
    print("You aren't old enough")
# ----------------------------- 

#  OR 
day = "Saturday"
# When using or only one of the conditions has to be met 
if day == "Saturday" or day == "Sunday":
    print("Its the weekend")
else:
    print("When is the weekend?")


# --------------------------------
# Functions
# Some functions are built into python for us to use

print("Hello world")
user_name = input("Please enter you name ")
print(f"Hello Alex {user_name}")

# ------------------------------------ 
# defining our own function
def press_grind_beans():
    print("grinding beans for 20 seconds")

press_grind_beans()

def withdraw_cash(amount, account_number):
    print(f"withdrawing {amount} from {account_number}.")

withdraw_cash(300, 4512896)
withdraw_cash(20, 6754728)

def take_order(size, type_of_drink):
    print(f"I would like a {size} {type_of_drink} please")

take_order("small", "flat white")
take_order("large", "latte")


