def collatzListRecursive(number):
    if number == 1:
        return [int(number)]
    else:
        if number%2 == 0:
            return [int(number)] + collatzListRecursive(number/2)
        else:
            return [int(number)] + collatzListRecursive((3 * number) + 1)

def collatzLength(number):
    count = 1
    tempNumber = number
    while tempNumber != 1:
        if tempNumber%2 == 0:
            tempNumber = tempNumber/2
        else:
            tempNumber = (3 * tempNumber) + 1
        count = count + 1
    return count

def collatzClever():
    lengthPairs = {"1" : 1}

    for x in range(2, 1000000):
        count = 0

        tempX = x

        found = False

        while tempX != 1 and not found:
            if tempX%2 == 0:
                tempX = tempX/2
            else:
                tempX = (3 * tempX) + 1
            count = count + 1

            if tempX < x:
                found = True
                count = count + lengthPairs[str(int(tempX))]

        lengthPairs[str(x)] = count
    return lengthPairs


def naiveWays():
    maxLength = 0
    number = 0
    for x in range(1, 1000000):
        if x%10000 == 0:
            print(x)
        # tempLength = len(collatzListRecursive(x))
        tempLength = collatzLength(x)

        if tempLength > maxLength:
            maxLength = tempLength
            number = x

    print(maxLength)
    print(number)

def main():
    theList = collatzClever()
    maxValue = 0
    number = 0
    for key, value in theList.items():
        if value > maxValue:
            maxValue = value
            number = key
    print(maxValue)
    print(number)

if __name__ == "__main__":
    main()
