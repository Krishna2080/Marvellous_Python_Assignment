#Q2. Vowel or Consonant Check Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print it's a consonant. 
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
