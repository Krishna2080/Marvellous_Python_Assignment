#Q4. Find Largest Among Three Numbers Accept three numbers from the user and print the largest using nested if-else statements.
def Largest(a1,b1,c1):
    if(a1>b1) and (a1>c1):
        print("Largest number is : ",a1)
    elif(b1>a1) and(b1>c1):
        print("Largest number is : ",b1)
    else:
        print("Largest number is : ",c1)


def main():
    a=int(input("enter 1st number : "))
    b=int(input("enter 2nd number : "))
    c=int(input("enter 3rd number : "))
    ret=Largest(a,b,c)


if __name__=="__main__":
    main()
