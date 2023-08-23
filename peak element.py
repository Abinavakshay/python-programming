a=[1,2,3,1]
m=max(a)
for i in range(0,len(a)):
    if a[i]==m:
        print("peak elementry index:",i)
        break
