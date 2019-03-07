
def main():
    sumOfSquares = 0
    theSum = 0

    for x in range (1, 101):
        sumOfSquares = sumOfSquares + (x * x)
        theSum = theSum + x

    print(sumOfSquares - (theSum * theSum))

if __name__ == "__main__":
    main()
