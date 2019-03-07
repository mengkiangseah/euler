from p3 import isPrime

def main():
    allNumbers = [x for x in range(1, 21)]
    allFactors = []
    while(len(set(allNumbers)) > 1):
        print(allNumbers)
        print(allFactors)
        print("---------")
        counter = 2
        changed = False
        while not changed:
            modsAll = [x%counter for x in allNumbers]
            if 0 in modsAll:
                allNumbers = [x/counter if x%counter == 0 else x for x in allNumbers]
                changed = True
                allFactors.append(counter)
            else:
                counter = counter + 1

    print(allFactors)
    productTotal = 1
    for each in allFactors:
        productTotal = productTotal * each
    print(productTotal)
if __name__ == "__main__":
    main()
