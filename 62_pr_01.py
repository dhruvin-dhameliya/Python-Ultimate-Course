def maximum(n1, n2, n3):
    if (n1>n2):
        print("The maximum number is: " + str(n1))
    elif (n2>n3):
        print("The maximum number is: " + str(n2))
    else:
        print("The maximum number is: " + str(n3))

    return maximum 

maximum(5, 8, 1)

print("----------------------------------")

def maximum(n1, n2, n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = maximum(7, 22, 80)
print("The maximum number is: " + str(m))