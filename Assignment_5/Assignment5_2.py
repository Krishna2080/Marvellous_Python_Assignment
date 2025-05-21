def vowel(v1):
    if(v1=="a") or (v1=="e") or (v1=="i") or (v1=="o") or (v1=="u"):
        print(v1,"is a Vowel")
    else:
        print(v1,"is a consonant")
def main():
    a=input("enter character : ")
    ret=vowel(a)
if __name__=="__main__":
    main()