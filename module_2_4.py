numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue
    is_prime = True  # установка флага
    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break
    if is_prime is True:
        primes.append(number)
    elif is_prime is False:
        not_primes.append(number)

print('Primes: ', primes)
print('Not Primes: ', not_primes)
