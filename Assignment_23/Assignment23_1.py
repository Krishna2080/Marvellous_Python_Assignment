import pandas as pd

def main():
      data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
      df=pd.DataFrame(data)
      print("Shape :",df.shape)
      print("columns of data :",df.columns)
      print("Data types of data :",df.dtypes)

if __name__=="__main__":
    main()