#Q2. Accept a list of integers from the user and use the map () function to double each value. 
double=lambda X:X*2


def main():
    a=int(input("Enter number : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    
    ans1=list(map(double,b))
    print("Double list : ",ans1)
      
if __name__=="__main__":
    main()