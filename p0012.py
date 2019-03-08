import math


def divisors(number):
    limit = math.ceil(math.sqrt(number))
    divisorList = [1, number]
    divisor = 2
    for divisor in range(2, limit+1):
        if number%divisor == 0:
            divisorList.append(divisor)
            divisorList.append(int(number/divisor))
    divisorList = list(set(divisorList))
    divisorList.sort()
    return divisorList


def main():
    counter = 1
    numberTriangle = 0
    while len(divisors(numberTriangle)) <= 500:
        numberTriangle = numberTriangle + counter
        print(str(numberTriangle) + " : " + str(divisors(numberTriangle)))
        counter = counter + 1

if __name__ == "__main__":
    main()
