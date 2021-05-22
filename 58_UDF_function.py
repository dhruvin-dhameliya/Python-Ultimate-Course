def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400 )*100
    return p

marks1 = [70, 58, 96, 66, 78]
percent1 = percent(marks1)

marks2 = [77, 48, 84, 53, 98]
percent2 = percent(marks2)

print("Persantage 1: " + str(percent1))
print("Persantage 2: " + str(percent2))