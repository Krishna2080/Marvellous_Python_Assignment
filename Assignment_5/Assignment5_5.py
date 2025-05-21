def EvenOdd(a1):
    if(a1%2==0):
        print(a1,"is an EVEN number")
    else:
        print(a1,"is an ODD number")


def main():
    a=int(input("enter 1st number : "))
    ret=EvenOdd(a)


if __name__=="__main__":
    main()