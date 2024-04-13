'''
While making a Data Frame from a csv file, many blank columns are imported as null value into the Data Frame which later creates problems while operating that data frame. Pandas isnull() and notnull() methods are used to check and manage NULL values in a data frame.
 

Dataframe.isnull()
Syntax: Pandas.isnull(“DataFrame Name”) or DataFrame.isnull()
Parameters: Object to check null values for
Return Type: Dataframe of Boolean values which are True for NaN values 
 

 

If we add the sum function after the isnull() it will give us the total number of data which are not present or null in our dataset.

Let us see with the help of an example.
'''

import pandas as pd
data = pd.read_csv("googleplaystore.csv")
print(data.isnull().sum())

'''
Output:

App                  0
Category             0
Rating            1474
Reviews              0
Size                 0
Installs             0
Type                 1
Price                0
Content Rating       1
Genres               0
Last Updated         0
Current Ver          8
Android Ver          3
dtype: int64
So we can see that our columns are App, Category, Rating etc. So the number which is being displayed after the column names is basically the total number of null values that particular column is containing.

 

So we can delete all the rows which are present in our dataframe with the help of dropna() function. Let us see the implementation of that now.
'''

df = data.dropna()
print(df.isnull().sum())

'''
Output:

App               0
Category          0
Rating            0
Reviews           0
Size              0
Installs          0
Type              0
Price             0
Content Rating    0
Genres            0
Last Updated      0
Current Ver       0
Android Ver       0
dtype: int64
So no more null values are present in any of the columns.
'''
