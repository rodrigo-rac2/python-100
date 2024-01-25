bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
percent = int(input("What percentage would you like to tip? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))
print(f"Each person should pay ${(bill + bill*percent/100)/num_of_people:.2f}")
