'''
We have already seen how we could remove the null values from our dataset. Let's analyse the numeric data present with us and try to find out the inferences which we can get.

So let us see our dataset again before getting started.
'''

import pandas as pd
df=pd.read_csv('googleplaystore.csv')
df.head()

'''
Output:

Let's do some analysis on the Rating column
'''

print(df['Rating'])

'''
Output:

0        4.1
1        3.9
2        4.7
3        4.5
4        4.3
        ... 
10834    4.0
10836    4.5
10837    5.0
10839    4.5
10840    4.5
Name: Rating, Length: 9360, dtype: float64
So the data type of the Rating is float64
'''
 

# Finding out the Average Rating


s=0
for i in df['Rating']:
    s+=i
s=int(s)
a=s/len(df['Rating'])
print("The average Rating of the datas in our data set is : ",round(a,3))

'''
Output:

The average Rating of the datas in our data set is :  4.192
 

How many Apps are there with Rating 5
'''

c=0
for i in df['Rating']:
    if (i==5.0):
        c+=1
print(f"There are {c} applications with rating 5")

'''
Output:

There are 274 applications with rating 5
 

Apps with Rating between the range of 4 and 4.5
'''

c=0
for i in df['Rating']:
    if (i>=4.0 and i<=4.5):
        c+=1
print(f"There are {c} applications with rating between the range of 4 and 4.5")

'''
Output:

There are 5446 applications with rating between the range of 4 and 4.5
'''
