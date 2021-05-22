# Celsius convert into Fahrenheit usind UDF function.

def farh(cel):
    return (cel * (9/5)) + 32

c = 15
f = farh(c)

print("Fahreheit Temperature is: " + str(f))
