inputAmount = int(input())

operations = ["+", "-", "*", "//"]

def calc():
    numList = []
    for i in range(inputAmount):
        userInput = int(input())
        if userInput < -1000000:
            print("invalid")
        elif userInput > 1000000:
            print("invalid")
        else:
            numList.append(userInput)


    for number in numList:
        answers = []
        for op1 in operations:
             for op2 in operations:
                for op3 in operations:
                    expression = f"4 {op1} 4 {op2} 4 {op3} 4"
                    if eval(expression) == number:
                        expression = expression.replace("//", "/")
                        answers.append(expression)

        if answers:
             print(f"{answers[0]} = {number}")
        else:
             print("no solution")

calc()