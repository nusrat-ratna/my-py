def eta_KI_prime_number(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

def prime_will_be(n):
    primes_are = []
    for num in range(2, n+1):
        if eta_KI_prime_number(num):
            primes_are.append(num)
    return primes_are

# User input
while True:
    try:
        user_input = int(input("Prime numbers up to: "))
        if user_input < 2:
            print("Please enter a number 2 or greater.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

prime_list = prime_will_be(user_input)
print("Prime numbers are:", prime_list)
print("Total prime numbers found:", len(prime_list))