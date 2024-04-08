"""
PowerOfTen
"""
# Provide your solution here
num = int(input("Enter a max 3 digit number: "))

if num > 999:
    print("Number has more than 3 digits.")
elif num < 1:
    print("Number cannot be negative.")
else:
    print(f"{num} = {num // 100} * 100 + {num % 100 // 10} * 10 + {num % 10} * 1")


"""
Cash Box
"""
# Provide your solution here

while True:
    owed = int(input("To be paid: "))
    paid = int(input("Received: "))
    change = paid - owed
    if change > 0:
        print(f"Your change is {change}.")
        break
    if paid < 0:
        print("We dont accept negative amounts.")
        continue
    if change < 0:
        print("You do not have enough money to pay.")
        continue
print("Thank you for your purchase.")