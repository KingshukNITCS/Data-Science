'''
Now we have already seen how we can handle null values for both Numeric and Categorical Data. Let use use those techniques and handle the null values for our GooglePlaystore Dataset.

So let us see our dataset again before getting started.
'''

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df=pd.read_csv("googleplaystore.csv")
print(df.head())

'''
Output:

Let us use the isnull().sum() function to check the number of null data in every column.
'''

print(df.isnull().sum())

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
 

So we have a huge number of data which is null in the Rating column. We can drop the rows which are null but that would not be optimal because the number of data. is very much. So we are going to use the SimpleImputer  and replace the null values with the mean of the Rating column.

Let's get started with the coding implementation now.
'''

impute = SimpleImputer(missing_values = np.nan , strategy = 'mean')
df.iloc[ : , 2:3 ] =impute.fit_transform(df.iloc[ : , 2:3 ].values)
 
'''
So we have replaced the null values with the mean value for the Rating column and there is no loss of data as well. Let us use the isnull().sum() function to again check our null values.
'''

print(df.isnull().sum())

'''
Output:

App               0
Category          0
Rating            0
Reviews           0
Size              0
Installs          0
Type              1
Price             0
Content Rating    1
Genres            0
Last Updated      0
Current Ver       8
Android Ver       3
dtype: int64     
 

So now we have some more null values present in the other columns. So we can see they are very less as compared to the size of the dataset( less than 1%) so we can just remove those null values.
'''

df=df.dropna()
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
So we have removed the rest of the null values and we have no null values present in our dataset anymore.
'''
