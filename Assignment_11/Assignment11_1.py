def Display(no,no2=1):
    
    if(no2 >no):
      return
    print(no2,end=" ")

    Display(no,no2+1)

def main():
    a=int(input("Enter number : "))
    Display(a)

if __name__ == "__main__":
    main()