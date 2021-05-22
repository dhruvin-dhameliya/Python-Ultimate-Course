def mul_table(num):
    for i in range(1, 11):
        print(f"{num}X{i}={num*i}")
    return

no = 3
mul = mul_table(no)
print(mul)             # Both are valid print statement.

print('-----------------------')

mul_table(6)
print(mul_table)
