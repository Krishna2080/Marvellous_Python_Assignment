#1. Write a program which contains one lambda function which accepts one parameter and return power of two.
power=lambda x:x**2

def main():
    a=int(input("enter number : "))
    ans=power(a)
    print(ans)

if __name__=="__main__":
    main()
    
