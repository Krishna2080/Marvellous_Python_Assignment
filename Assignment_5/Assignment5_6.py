def Fahrenheit(v1):
    F=(v1*9/5)+32
    print("Temprature in Fahrenheit : ",F)
    
def main():
    a=int(input("enter temprature in Celsius : "))
    ret=Fahrenheit(a)

if __name__=="__main__":
    main()