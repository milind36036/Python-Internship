age =int(input("ENTER YOUR AGE:"))
citizen = input("ARE YOU CITIZEN(INDIAN)?(YES/NO):")

if age>=18 and citizen.lower() =="yes":
    print("ELIGIBLE TO VOTE")
else:
    print("NOT ALLOWED")
         