sub1 = int(input("Enter subject 1 marks: ")) 
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail, Any subject in less marks 33.")
elif(sub1+sub2+sub3)/3 < 40 :
    print("You are Fail, Total parsantage less 40.")
else:
    print("Congratulations !!! ... You are pass.")