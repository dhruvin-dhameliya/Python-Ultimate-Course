# Using File I/O:
f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present.")
else:
    print("Twinkle is not present.")
f.close()

print("---------------------------")

# Using a with statement:
with open('another.txt', 'r') as f:
    a = f.read()
    if 'twinkle' in t:
        print("Twinkle is present.")
    else:
        print("Twinkle is not present.")
    