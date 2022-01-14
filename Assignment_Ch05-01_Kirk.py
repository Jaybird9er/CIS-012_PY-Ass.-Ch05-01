enterNums = True
while enterNums:
    print("Please enter 10 integers: ")
    totalInts = 0
    evenSum = 0
    oddSum = 0
    while totalInts < 10:
        userNum = int(input())
        if(userNum % 2 == 0):
            evenSum += userNum
        else:
            oddSum += userNum
        totalInts += 1
    print("\n")
    print("Even sum: ", evenSum)
    print("Odd sum: ", oddSum)
    print("\n")
    print("Do you wish to repeat this program? (y/n)")
    userAnswer = input()
    if(userAnswer == 'y' or userAnswer == 'Y'):
        enterNums = True
    else:
        enterNums = False
    print("\n")

print("Done!")
