
import pandas as pd
from pandas import DataFrame as df  
import textdistance

def load_it():
    
    complist=pd.read_csv('.\\RawData\AddressCompare.csv')
    print(type(complist))
    return(complist)
    

def main():
    filer = load_it()
    for row in filer.itertuples():
        print(row.InsuredDriver)
        print(row.ULDDriver)
        print(row.Index)
        print(textdistance.levenshtein.normalized_similarity((row.InsuredDriver),(row.ULDDriver)))
    print(filer)
    # print(textdistance.levenshtein.normalized_similarity('test','text'))
    return
            
    

if __name__ =="__main__":
    main()
    
