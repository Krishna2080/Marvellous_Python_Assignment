#Q3. Accept a number from the user and print its multiplication table up to 10
def table(v1):
        for i in range(1,11):
          print(v1,"x",i,"=",v1*i)
    
def main():
    a=int(input("Enter number : "))
    table(a)
    
    
if __name__=="__main__":
    main()