import math

def main():
    allPrimes = []
    number = 2

    while number < 2000000:
        if number%1000 == 0:
            print(number)

        limit = math.ceil(math.sqrt(number))

        x = 0
        foundDivisor = False
        while x < len(allPrimes) and allPrimes[x] <= limit and not foundDivisor:
            if number%allPrimes[x] == 0:
                foundDivisor = True
            x = x + 1

        if not foundDivisor:
            allPrimes.append(number)

        number = number + 1

    print(sum(allPrimes))

if __name__ == "__main__":
    main()
