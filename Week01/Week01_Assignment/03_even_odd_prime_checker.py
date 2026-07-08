print("===== Even/Odd and Prime Checker =====")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

if number <= 1:
    print(number, "is Not Prime")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is Prime")
    else:
        print(number, "is Not Prime")