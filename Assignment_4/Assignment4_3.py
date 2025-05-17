#3. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
#  Map function will increase each number by 10. Reduce will return product of all that numbers
from functools import reduce
def filterx(X):
    return X>=70 and X<=90

def inc(X):
    return X+10

def product(X, Y):
    return X * Y

def main():
    a=int(input("enter how many u want to store : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    print("Input list = ",b)
    ans1=list(filter(filterx,b))
    print("List After Filter = ",ans1)

    ans2=list(map(inc,ans1))
    print("List After map = ",ans2)

    ans3 = reduce(product, ans2)
    print("Output of Reduce = ", ans3)
    

if __name__=="__main__":
    main()
