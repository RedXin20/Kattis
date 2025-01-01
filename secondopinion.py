s = int(input()) # This will be in seconds 

# Basic method
def time(s):
    min = s // 60
    sec = s % 60
    hour = min // 60
    min = min % 60
    return f"{hour} : {min} : {sec}"

print(time(s))

# Mapping method

def time2(s):
    timeMap = {
        "hour": s // 3600,
        "min": (s % 3600) // 60,
        "sec": (s % 3600) % 60
    }
    return f"{timeMap['hour']} : {timeMap['min']} : {timeMap['sec']}" 
print(time2(s))


# Condition based, my original solution

def time3(s):
    if s < 60:
        return f"0 : 0 : {s}"
    elif s < 3600:
        min = s // 60
        sec = s % 60
        return f"0 : {min} : {sec}"
    else:
        hour = s // 3600
        min = (s % 3600) // 60
        sec = (s % 3600) % 60
        return f"{hour} : {min} : {sec}"
    
print(time3(s))