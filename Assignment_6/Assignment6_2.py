#Q2. Print Sum of Even Numbers Between 1 and 100.
# Use a loop to find and print the sum of all even numbers from 1 to 100. 
def main():
    sum=0
    for i in range(2,101,2):
        sum=sum+i
    print("Sum of even number 1 to 100 is : ",sum)    
    

if __name__=="__main__":
    main()