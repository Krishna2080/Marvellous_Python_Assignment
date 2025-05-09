#3. Write a program which contains one function named as Add() 
# which accepts two numbers from user and return addition of that two numbers.
def Add(Vaule1,Value2):
   ans=Vaule1+Value2
   return ans

def main():
    print("Enter First Number")
    No1=int(input())
    print("Enter Second Number")
    No2=int(input())

    result=Add(No1,No2)
    print("Your Addition is : ",result)

if __name__=="__main__":
    main()