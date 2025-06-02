fact=1
def Display(no):
    global fact
    if(no >= 1):
        fact=fact*no
        no = no - 1
        Display(no)
    return fact
    

def main():
    a=int(input("Enter number : "))
    ret=Display(a)
    print("Factorial is = ",ret)

if __name__ == "__main__":
    main()