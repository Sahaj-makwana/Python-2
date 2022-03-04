
a,b,c=int(input("Enter 1st number: ")),int(input("Enter 2nd number: ")),int(input("Enter 3rd number: "))
if (a<=b and a>=c) or (a<=c and a>=b):
    print("Second max number is ",a)
elif (b<=a and b>=c) or (b<=c and b>=a):
    print("Second max number is ",b)
elif (c<=b and c>=a) or (c<=a and c>=b):
    print("Second max number is ",c)