def isPalindrome(numberString):
    if len(numberString) < 2:
        return True
    elif numberString[0] == numberString[-1]:
        return isPalindrome(numberString[1:-1])
    else:
        return False

def main():
    allPalindromes = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            if isPalindrome(str(x * y)):
                allPalindromes.append(x * y)
    print(max(allPalindromes))


if __name__ == "__main__":
    main()
