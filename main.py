print("Welcome to the Fiber Optic Installation Program!")
company_name = input("ENTER YOUR COMPANY NAME. ")
feet_of_fiber = float(input("Enter the number of feet of fiber optic to be installed: "))
cost_per_feet = 0.87
total_cost = feet_of_fiber * cost_per_feet
print ("")
print("CALCULATED INFORMATION")
print("Company Name:", company_name)
print("Feet of Fiber Optic to be Installed:", feet_of_fiber)
print("Total Cost: $", total_cost)