import math

def isPrime(number):
    limit = math.ceil(math.sqrt(number))
    if number < 4:
        return True
    for x in range(2, limit):
        if number%x == 0:
            return False
    return True

def primeFactor(number):
    print("Called: " + str(number))
    if isPrime(number):
        return [number]
    else:
        limit = math.ceil(math.sqrt(number))
        for x in range(2, limit):
            if number%x == 0:
                return [x] + primeFactor(number/x)
        return [number]

def main():
    print(max(primeFactor(600851475143)))

if __name__ == "__main__":
    main()
