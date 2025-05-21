#Q1. Arithmetic Operations on Two Numbers 
#Write a program to accept two integers from the user and display their: 
#Sum ,Difference ,Product ,Division 
def Add(v1,v2):
    return v1+v2
def Minus(v1,v2):
    return(v1-v2)
def Pro(v1,v2):
    return v1*v2
def Div(v1,v2):
    return(v1/v2)

def main():
    a=int(input("Enter 1st number  : "))
    b=int(input("Enter 2nd number : "))
    ret1=Add(a,b)
    ret2=Minus(a,b)
    ret3=Pro(a,b)
    ret4=Div(a,b)
    print("SUM  : ",ret1)
    print("Difference  : ",ret2)
    print("Product : ",ret3)
    print("Division is ",ret4)

if __name__=="__main__":
    main()
