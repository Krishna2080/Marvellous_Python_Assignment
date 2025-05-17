#5. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user.
#  Filter should filter out all prime numbers. Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers.
#  (You can also use normal functions instead of lambda functions). 

from functools import reduce
def filt(X):
    if X<2:
     return False
    for i in range(2,X):
       if X%i==0:
           return False
    return True
        
def Multiply(X):
    return X*2

def Max(X, Y):
   if X>Y:
    return X
   else:
      return Y
    

def main():
    a=int(input("enter how many u want to store : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    print("Input list = ",b)
    ans1=list(filter(filt,b))
    print("List After Filter = ",ans1)

    ans2=list(map(Multiply,ans1))
    print("List After map = ",ans2)

    ans3 =reduce(Max, ans2)
    print("Output of Reduce = ", ans3)
    

if __name__=="__main__":
    main()

