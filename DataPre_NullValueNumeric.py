'''
Earlier we have discussed an approach to remove nulll values from a dataset. But removing the null values is always not the most optical approach to work on a dataset. Let us see here how we can handle the null values instead of dropping them.

Let us import pandas and read the csv file initially.
'''

import pandas as pd
df=pd.read_csv('Data.csv')
print(df)

'''
Output 

   Country   Age   Salary Purchased
0   France  44.0  72000.0       Yes
1    Spain  27.0  48000.0       Yes
2      NaN  30.0  54000.0       NaN
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
So we can see we don't have a big dataset and there are NaN or null values present in almost every column. So now how would we handle them?

SimpleImputer is a scikit-learn class which is helpful in handling the missing data in the predictive model dataset. It replaces the NaN values with a specified placeholder. 
It is implemented by the use of the SimpleImputer() method which takes the following arguments :
 

missing_values : The missing_values placeholder which has to be imputed. By default is NaN 
strategy : The data which will replace the NaN values from the dataset. The strategy argument can take the values – ‘mean'(default), ‘median’, ‘most_frequent’ and ‘constant’. 
fill_value : The constant value to be given to the NaN data using the constant strategy.  
'''

import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
df.iloc[:,1:3]=imputer.fit_transform(df.iloc[:,1:3].values)

'''
Now if we print the DataFrame(df) we will notice that the null values of the numeric column has been removed
'''
print(df)

'''
Output 

   Country   Age   Salary Purchased
0   France  44.0  72000.0       Yes
1    Spain  27.0  48000.0       Yes
2      NaN  30.0  54000.0       NaN
3    Spain  38.0  61000.0        No
4  Germany  40.0  48000.0       Yes
5   France  35.0  58000.0       Yes
6    Spain  27.0  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
 
To confirm it we can use the isnull().sum() function.
'''

print(df.isnull().sum())

'''
Output 

Country      1
Age          0
Salary       0
Purchased    1
dtype: int64
So the null values from the numeric data columns has been removed.
'''
