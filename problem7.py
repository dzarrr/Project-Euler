## Dzar Bela Hanifa
## Project Euler no 7
## Written in Python 3.7

def generate_prime_sieve(n):
  sieve = []
  for i in range (0, n + 1):
    sieve.append(True)
  prime_sieve = []

  for i in range (2, n + 1) :
    if sieve[i] :
      prime_sieve.append(i)
      for j in range (i + i, n + 1, i) :
        sieve[j] = False

  return prime_sieve


max_number = int(input("Bilangan maksimum : "))
n = int(input("Bilangan prima ke berapa yang anda cari ? : "))

prime_list = generate_prime_sieve(max_number)
print (prime_list[n-1])

