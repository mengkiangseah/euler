import math

def main():
    allPrimes = []
    number = 2

    while len(allPrimes) < 10001:

        limit = math.ceil(math.sqrt(number))

        allPrimesDivide = [x for x in allPrimes if x <= limit]

        allOutput = [x for x in allPrimesDivide if number%x == 0]

        if len(allOutput) == 0:
            allPrimes.append(number)

        number = number + 1

    print(max(allPrimes))

if __name__ == "__main__":
    main()
