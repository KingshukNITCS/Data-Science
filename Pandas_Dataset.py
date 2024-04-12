'''
To access data from the CSV file, we require a function read_csv() that retrieves data in the form of the Dataframe.

Syntax of read_csv() 
Syntax: pd.read_csv(filepath_or_buffer, sep=’ ,’ , header=’infer’,  index_col=None, usecols=None, engine=None, skiprows=None, nrows=None) 

 
Parameters: 

filepath_or_buffer: It is the location of the file which is to be retrieved using this function. It accepts any string path or URL of the file.
sep: It stands for separator, default is ‘, ‘ as in CSV(comma separated values).
header: It accepts int, a list of int, row numbers to use as the column names, and the start of the data. If no names are passed, i.e., header=None, then,  it will display the first column as 0, the second as 1, and so on.
usecols: It is used to retrieve only selected columns from the CSV file.
nrows: It means a number of rows to be displayed from the dataset.
index_col: If None, there are no index numbers displayed along with records.  
skiprows: Skips passed rows in the new data frame.
Read CSV using Pandas read_csv
Before using this function, we must import the Pandas library, we will load the CSV file.
'''

# Import pandas
import pandas as pd
 
# reading csv file
pd.read_csv("example1.csv")


'''
Output

             Date  Latitude  Longitude  Magnitude
0      01/02/1965   19.2460   145.6160        6.0
1      01/04/1965    1.8630   127.3520        5.8
2      01/05/1965  -20.5790  -173.9720        6.2
3      01/08/1965  -59.0760   -23.5570        5.8
4      01/09/1965   11.9380   126.4270        5.8
...           ...       ...        ...        ...
23407  12/28/2016   38.3917  -118.8941        5.6
23408  12/28/2016   38.3777  -118.8957        5.5
23409  12/28/2016   36.9179   140.4262        5.9
23410  12/29/2016   -9.0283   118.6639        6.3
23411  12/30/2016   37.3973   141.4103        5.5

[23412 rows x 4 columns]
It basically shows us our data set where we have 23412 rows and 4 Columns

 

 

If we want to see the data of a specific column we can store the dataset in a variable and print it enclosing the column name inside the square brackets.
'''


df=pd.read_csv('example1.csv')
print(df['Magnitude'])


'''
Output

0        6.0
1        5.8
2        6.2
3        5.8
4        5.8
        ... 
23407    5.6
23408    5.5
23409    5.9
23410    6.3
23411    5.5
Name: Magnitude, Length: 23412, dtype: float64
If we want to select multiple columns we need to give double square brackets
'''

print(df[['Magnitude','Latitude']])

'''
Output

       Magnitude  Latitude
0            6.0   19.2460
1            5.8    1.8630
2            6.2  -20.5790
3            5.8  -59.0760
4            5.8   11.9380
...          ...       ...
23407        5.6   38.3917
23408        5.5   38.3777
23409        5.9   36.9179
23410        6.3   -9.0283
23411        5.5   37.3973

[23412 rows x 2 columns]
 

 

Pandas DataFrame.columns attribute return the column labels of the given Dataframe.

Syntax: DataFrame.columns

Parameter : None

Returns : column names
'''

print(df.columns)


# Index(['Date', 'Latitude', 'Longitude', 'Magnitude'], dtype='object')
