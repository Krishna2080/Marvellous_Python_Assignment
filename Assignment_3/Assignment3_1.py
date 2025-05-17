from functools import reduce
def Sum (A,B):
    return A+B

def main():
    a=int(input("how many number you want to store : "))
    b=list()
    for i in range(a):
        no=int(input())
        b.append(no)

    result=reduce(Sum,b)
    print("your list addition is : ",result)
       
if __name__=="__main__":
    main()


#result=0
    #for i in b:
       #result=result+i
    