amountOfTemperature = int(input())
temperatures = list(map(int, input().split()))
count = 0

for i in range(amountOfTemperature):
    if temperatures[i] < 0:
        count += 1

print(count)