#Q1. Write two lambda functions: 
#One to calculate square of a number 
#Another to calculate cube of a number 
square=lambda X:X*X
cube=lambda X:X*X*X


def main():
    a=int(input("Enter number : "))
    ans1=square(a)
    ans2=cube(a)
    print("Square : ",ans1)
    print("Cube : ",ans2)

    
if __name__=="__main__":
    main()