'''
We have already done some analysis on numerical data. Let us work with Categorical data now. 

Before doing analysis let us see our dataset again.
'''

import pandas as pd
df=pd.read_csv('googleplaystore.csv')
df.head()

'''
Output:

Total Number of Unique Categories
We can use the unique() function to get all the unique values of Category column
'''

df['Category'].unique()

'''
Output:

array(['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY',
       'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION',
       'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE',
       'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME',
       'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL',
       'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS', 'TRAVEL_AND_LOCAL',
       'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER',
       'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION'],
      dtype=object)
 

To get the total number of Unique values we can use the nunique() function.
'''

n=df['Category'].nunique()
print("There are a total of ",n," unique values in Category columns")

'''
Output:

There are a total of  33  unique values in Category columns
  
Total Number of apps in ART_AND_DESIGN
'''

c=0
for i in df['Category']:
    if(i=='ART_AND_DESIGN'):
        c+=1
print(f"There are a total of {c} applications in ART_AND_DESIGN")

'''
Output:

There are a total of 61 applications in ART_AND_DESIG

Total number of Free and Paid Apps
'''

f=0
p=0
for i in df['Type']:
    if(i=='Free'):
        f+=1
for i in df['Type']:
    if(i=='Paid'):
        p+=1
print(f"There are a total number of {f} free and {p} paid apps")

'''
Output:

There are a total number of 8715 free and 645 paid apps
 

Percentage of Free and Paid Apps
'''

ff=f/len(df['Type'])*100
ff=round(ff,2)
pp=100-ff
pp=round(pp,2)
print(f"A total of {ff}% of the apps are Free and {pp}% of the apps are paid")

'''
Output:

A total of 93.11% of the apps are Free and 6.89% of the apps are paid
'''
