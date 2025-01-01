result = []

while True:
    try:
        userInput = input().split()
        if len(userInput) != 2:
            break
        else:
            a = int(userInput[0])
            b = int(userInput[1])
            if a < 0 or b < 0:
                break
            else:
                result.append(abs(a - b))
    except EOFError:
        break

for i in result:
    print(i)
