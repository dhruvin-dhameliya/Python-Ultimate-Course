s = set()

s.add(20)
s.add(20.0)    # 20 and 20.0 is same value --> print the only one time print 20
s.add("20")

print(s)

print(type(s))

print(len(s))

a = { }
print(type(a))  # It is represent the empty Dictionary .