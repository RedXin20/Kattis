userInput = str(input())

newAlphabet = {
    "A": "@", "a": "@",
    "B": "8", "b": "8",
    "C": "(", "c": "(",
    "D": "|)", "d": "|)",
    "E": "3", "e": "3",
    "F": "#", "f": "#",
    "G": "6", "g": "6",
    "H": "[-]", "h": "[-]",
    "I": "|", "i": "|",
    "J": "_|", "j": "_|",
    "K": "|<", "k": "|<",
    "L": "1", "l": "1",
    "M": "[]\\/[]", "m": "[]\\/[]",  
    "N": "[]\\[]", "n": "[]\\[]",   
    "O": "0", "o": "0",
    "P": "|D", "p": "|D",
    "Q": "(,)", "q": "(,)",
    "R": "|Z", "r": "|Z",
    "S": "$", "s": "$",
    "T": "']['", "t": "']['",
    "U": "|_|", "u": "|_|",
    "V": "\\/", "v": "\\/",         
    "W": "\\/\\/", "w": "\\/\\/",   
    "X": "}{", "x": "}{",
    "Y": "`/", "y": "`/",
    "Z": "2", "z": "2",
}


newSentence = ""


if len(userInput) > 10000:
    print("Input is too long")
else:
    for letter in userInput:
        if letter in newAlphabet:
            newSentence += newAlphabet[letter]
        else:
         newSentence += letter

print(newSentence)