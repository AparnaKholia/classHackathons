import sys
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

df=pd.read_csv('CropsDataFile.csv')
while(1):
    
    print("Enter 1 to retrive data year wise,")
    print("Enter 2 to retrive cropwise details")
    print("Enter 3 to exit system")
    ch=int(input())
    if ch==1:
       print("Enter year")
       yr=input()
       gk=df.groupby('Year')
       s=gk.get_group(yr)
       print(s) 
    elif ch==2:
       crop=input("Enter crop:",)
       gk=df.groupby('Crop_Name')
       s=gk.get_group(crop)
       print(s)
       print("\nEnter 1 if you want a graph\nEnter 2 if you don't want a graph")
       ch2=int(input("\nEnter your choice:"))
       if ch2==1:
           ss=s.groupby('Year')['Production'].apply(lambda x: x.tolist()).to_dict()
           #print(ss)
           pro=list()
           sum=0
           for i in ss.values():
                for j in i:
                    sum+=float(j)
                pro.append(sum)
                sum=0
           #print(pro)
           year=list()
           for x in ss.keys():
               year.append(x)
           #print(year)
       
           plt.bar(year,pro)
           plt.xlabel('year')
           plt.ylabel('production')
           plt.title('Year wise production of crop')
           plt.show()
       elif ch2==2:
            sys.exit(1)
       else:
            print("\nWrong choice")

    elif ch==3:
       print("\nThank you for using our system!\nHave a good day!\n")
       sys.exit(1)
    else:
        print("Wrong Choice!! Try again!")



                          
        