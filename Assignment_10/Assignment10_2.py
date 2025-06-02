#2. Write a program which contains one lambda function which accepts two parameters and return its multiplication

Multi=lambda X,Y:X*Y

def main():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    c=Multi(a,b)
    print("Your Multiplication is : ",c)

if __name__=="__main__":
    main()