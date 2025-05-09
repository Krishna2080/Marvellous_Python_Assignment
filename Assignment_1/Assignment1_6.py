#6. Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkNum(Value1):
    if(Value1>0):
      
      print("Positive Number")

    elif(Value1==0):
       print("Zero")
     
    elif(Value1<0):
       print("Negative Number")

def main():
   print("enter number")
   no1=int(input())
   result=ChkNum(no1)

if __name__=="__main__":
    main()