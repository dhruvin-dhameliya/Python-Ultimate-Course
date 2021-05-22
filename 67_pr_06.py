# Inch convert into Centimeters (cms) usind UDF function. 

def cms(inch):
    return (inch * 2.54)

in_ch = 30
f = cms(in_ch)

print("Centemeter is: " + str(f))
