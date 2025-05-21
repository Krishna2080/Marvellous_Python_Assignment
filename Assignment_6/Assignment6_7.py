def Max(v1):
    for i in range(len(v1)):
        for j in range(0,len(v1)-i-1):
            if(v1[j]<v1[j+1]):
                v1[j],v1[j+1]=v1[j+1],v1[j]
    print("Maximum Nuber is : ",v1[0])
    
def main():
    print("enter 5 number : ")
    b=list()
    for i in range(5):
        n=int(input())
        b.append(n)
    Max(b)
if __name__=="__main__":
    main()