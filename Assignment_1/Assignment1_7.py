#7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def divisiblity(Value1):
    if(Value1%5==0):
        return True
    else:
        return False
        
def main():
    print("Enter number")
    No1=int(input())
    result=divisiblity(No1)
    print(result)

if __name__=="__main__":
    main()