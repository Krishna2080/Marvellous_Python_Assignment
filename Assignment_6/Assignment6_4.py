#Q4. Accept a number and print its factorial using a for loop. 
def factorial(v1):
        ans=1
        for i in range(1,v1+1):
          ans=ans*i
        print("Factorial of",v1,"is : ",ans)
    
def main():
    a=int(input("Enter number : "))
    factorial(a)
       
if __name__=="__main__":
    main()