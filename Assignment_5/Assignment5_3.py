#Q3. Voting Eligibility Checker Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.) 
def vote(v1):
    if(v1>=18):
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")
def main():
    a=int(input("enter your age : "))
    ret=vote(a)

if __name__=="__main__":
    main()
