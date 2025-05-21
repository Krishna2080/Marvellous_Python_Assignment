#Q7. Area and Perimeter of Rectangle Accept the length and width of a rectangle. Calculate and display the area and perimeter. 
def Rectangle(L1,W1):
    area=L1*W1
    perimeter=2*(L1+W1)
    print("Area: ",area)
    print("Perimeter: ",perimeter)
    
def main():
    a=int(input("Enter length : "))
    b=int(input("Enter width: "))
    ret=Rectangle(a,b)

if __name__=="__main__":
    main()
