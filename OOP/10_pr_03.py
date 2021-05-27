class Sample:
    a = "Dhruvin"

obj = Sample()
obj.a = "Ravi"   # Can not change class atributes.

print(Sample.a)
print(obj.a)

Sample.a = "Dharm"  # But this prosses can change class atributes.
print(Sample.a)