#4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List. 
def freq(n,li,f):
    cnt=0
    for i in range(n):
     if li[i]==f:
      cnt=+1
    return cnt


def main():
    a=int(input("enter how many elements you want to store : "))
    b=list()
    no=0
    for i in range(a):
        no=int(input())
        b.append(no)
    
    c=int(input("Enter element which you want to search : "))
    
    result=freq(a,b,c)

    print("frequency is : ",result)


if __name__=="__main__":
    main()
