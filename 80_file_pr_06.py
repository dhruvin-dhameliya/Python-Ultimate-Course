with open("log_file.txt") as f:
    content = f.read()

# log_file.txt in line number 21 & 85 include python word.

if 'python' in content.lower():
    print("Yes python is present")    
else:                                   
    print("No python is not present")