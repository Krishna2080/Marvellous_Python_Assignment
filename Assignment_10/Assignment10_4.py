#4. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even.
#  Map function will calculate its square. 
# Reduce will return addition of all that numbers. 
from functools import reduce
def filt(X):
    return X%2==0

def square(X):
    return X**2

def sum(X, Y):
    return X + Y

def main():
    a=int(input("enter how many u want to store : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    print("Input list = ",b)
    ans1=list(filter(filt,b))
    print("List After Filter = ",ans1)

    ans2=list(map(square,ans1))
    print("List After map = ",ans2)

    ans3 = reduce(sum, ans2)
    print("Output of Reduce = ", ans3)
    

if __name__=="__main__":
    main()

