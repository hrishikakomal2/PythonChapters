sub1 = int(input("Enter your marks : "))
sub2 = int(input("Enter your marks : "))
sub3 = int(input("Enter your marks : "))

if(sub1 <33 or sub2<33 or sub3<33):
    print("fail")
elif((sub1+sub2+sub3)/3 < 40):
    print("fail")
else:
    print("passed")
