class Demo:
    classvariable="Value"

    def __init__(self,A,B):
     self.no1=A
     self.no2=B
    

    def Fun(self):
       print(self.no1)
       print(self.no2)
       
    def Gun(self):
       print(self.no1)
       print(self.no2)
       
def main():
   obj1=Demo(11,21)
   obj2=Demo(51,101)

   obj1.Fun()
   obj2.Fun()
   obj1.Gun()
   obj2.Gun()
   
if __name__=="__main__":
   main()