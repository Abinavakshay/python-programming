a=int(input("enter the no of class"))
b=int(input("attended classes"))
c=b/a*100
print("attendance% is",c)
if(c>75):
    print("eligible for voting")
else:
    print("unfit for exam")
d=(input("any medical issues(1/2):")
    if(d=="1"):
    print("Eligible")
    else(d=="2"):
    print("Not Eligible")
