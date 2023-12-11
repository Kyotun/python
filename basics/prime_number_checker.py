def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


print("Welcome to the prime checker!")
number = int(input("Please enter the number that should be checked: "))
prime_check(number=number)
