#2.Write a program which contains one function named as ChkNum() which accept one parameter as number. 
# If number is even then it should display "Even number" otherwise display "Odd number" on console. 


def ChkNum(Num):
     if (Num%2 ==0):
          print("Even Number")
     else:
          print("odd Number")
          
def main():
     print("Enter Number to check even or odd")
     no=int(input())
     ChkNum(no)

if __name__=="__main__":
    main()

