full_name = input("Provide your Full Name: ")
staff_number = input("Provide your Staff Number: ")
level = input("provide your Level: ")

full_name = full_name.title()

if full_name == "":
    print("Full Name Cannot Be Empty!")
else:
    print("Full Name Entry: ",full_name)
    
    
if staff_number.isdigit():
    print("Staff Number Captured: ",staff_number)
else:
    print("Staff Number Must Be Numerical!")
    
