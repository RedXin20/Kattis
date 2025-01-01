# We start with 1 printer
# We would like to produce n statues
# Printing n statues with 1 printer takes too long, so use same printer to print a new printer
# The new printer can be used to print statues too or it can be used to print more printers, each printing process takes a full day

statues = int(input())

if statues < 1 or statues > 10000:
    exit()
else: 
    days = 0
    printedStatue = 0
    printers = 1

    while printedStatue < statues:
        if statues == 1:
            days += 1
            break
        elif printers < statues:
            printers *= 2
            days += 1
        else:
            printedStatue += printers    
            days += 1  
        
    print(days)