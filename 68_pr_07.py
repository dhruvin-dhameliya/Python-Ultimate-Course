this = "      Coding is a fun.      "

print(this)
print(this.strip())    # Strip usig the string is perfect line in print.

print('--------------------------')

def remove_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

st = "        Python is very easy laguage.        "
n = remove_split(st, "is")                  # is word remove in a string.
print(n)
