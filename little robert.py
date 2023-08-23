def can_divide(prod,summ):
    if prod%summ==0:
        return "YEAH"
    else:
        return "NAH"
num_test_cases=int(input("enter the number of test cases:"))
for _ in range(num_test_cases):
    prod,summ=map(int,input("enter prod & summ:").split())
    r=can_divide(prod,summ)
    print(r)
    
