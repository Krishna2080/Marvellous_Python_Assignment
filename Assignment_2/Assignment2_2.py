#2. Write a program which accept one number and display below pattern. 
#       *    *    *    *    *
#       *    *    *    *    *
#       *    *    *    *    *
#       *    *    *    *    *
#       *    *    *    *    *
def main():
    no1=int(input("enter number"))
    for i in range(no1):
     print("* \t"*no1)
        
if __name__=="__main__":
    main()
