userInput = str(input())

word = []

def f():
    if len(userInput) > 100000 or len(userInput) <= 0: 
        return
    else:
        for i in range(len(userInput) - 1): 
            if userInput[i] != userInput[i + 1]:
                word.append(userInput[i])

        word.append(userInput[-1])

        print("".join(word))

f()
