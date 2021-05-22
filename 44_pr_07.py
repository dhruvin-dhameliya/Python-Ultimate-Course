post = input("Enter a post: ")

if ("LAPTOP" in post):
    find = True
elif ("Laptop" in post):
    find = True
elif ("laptop" in post):
    find = True
elif ("LaptoP" in post):
    find = True
elif ("LaPtOp" in post):
    find = True
else:
    find = False

if (find):
    print("Yes! the post is laptop.")
else:
    print("No! the post is not laptop.")