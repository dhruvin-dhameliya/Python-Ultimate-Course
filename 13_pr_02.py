letter = '''Dear <|NAME|>,
Greeting from CodeWithDhruvin coding house. I am happy to tell you about your selection .
You are selected !
Have a great day ahead !
Thanks and regards,
DHRUVIN

Date : <|DATE|>'''

name = input("Enter your Name : ")
date = input("Enter the Date : ")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)


print(letter)