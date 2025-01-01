name = int(input()) # usually one
peopleInput = int(input())

classOrder = {"upper": 1, "middle": 2, "lower": 3}

def order(peopleInput):
    peopleList = []
    for i in range(peopleInput):
        peopleList.append(input())

    person = []
    for p in peopleList:
        name, classInfo = p.split(":")
        classInfo = classInfo.replace("class", "").strip()
        classLevel = classInfo.split("-")
        classPrio = [classOrder.get(c, 4) for c in classLevel]
        person.append((name, classPrio))


    person.sort(key=lambda x: x[1])

    return [p[0] for p in person]

result = order(peopleInput)

for name in result:
    print(name)

print("==============================")