def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


number = int(input("Enter a number: "))

print(f'{number} is prime' if is_prime(number) else f'{number} is not prime')