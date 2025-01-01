flightAmount = int(input())

def reimbursement(flightAmount):
    maxFlight = 0
    minFlight = 100000

    for i in range(flightAmount):
        flight = int(input())
        if flight > maxFlight:
            maxFlight = flight
        if flight < minFlight:
            minFlight = flight

    half = maxFlight // 2
    price = minFlight - half 
    if price < 0:
        price = 0
    print(price)

reimbursement(flightAmount)




