#Program 1 : This takes default index
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

#Program 2: to pass user defined index
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100,101,102,103])
print(s)

#Program 3 : Indexing and slicing operations
import pandas as pd
s=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s['a'])

#Dataframe from list
import pandas as pd
lst = ['Python','is','not','difficult','at','all.']
df = pd.DataFrame(lst)
print(df)

#DataFrame using Dictionary
import pandas as pd
data = {'Name': ['Lisa','Tanni','Rohan','Mike'],
        'Age': [20,21,19,18]}
df = pd.DataFrame(data)
print(df)

#Program using excel file to create Dataframe
# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("myexcel.csv", index_col="Name")

# retrieving columns by indexing operator
first = data["Age"]
print(first)

#Program to delete rows
import pandas as pd

# making data frame from csv file
data = pd.read_csv("myexcel.csv", index_col="Name")

data.drop(["Avery Bradley","John Holland","R.J. Hunter","R.J. Hunter"], inplace = True)
print(data)

#Program to reshape the dataframe
import pandas as pd
df = pd.read_csv("myexcel.csv")
df_stacked = df.stack()
print(df_stacked.head(26))

#Program to handle missing data in dataframe
import pandas as pd
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)
# using isnull() function
print(df.isnull())

#Program for grouping data frame based on 1 column
import pandas as pd
# Creating the dataframe
df = pd.read_csv("myexcel.csv")
# Print the dataframe
print(df)
gk = df.groupby('Team')
gk.first()

#Program for grouping on 2 columns

import pandas as pd
# Creating the dataframe
df = pd.read_csv("myexcel.csv")
# First grouping based on "Team"
# Within each team we are grouping based on "Position"
gkk = df.groupby(['Team', 'Position'])
# Print the first value in each group
print(gkk.first())

#Program to sort data frame
import pandas as pd
data = {'Brand': ['HH', 'TT', 'FF', 'AA'],
        'Price': [22000, 25000, 27000, 35000],
        'Year': [2015, 2013, 2018, 2018]
        }
df = pd.DataFrame(data, columns=['Brand', 'Price', 'Year'])
# sort Brand in an ascending order
df.sort_values(by=['Year'], inplace=True)
print(df)
# sort Brand in an descending order
df.sort_values(by=['Year'], inplace=True, ascending=False)
print(df)

#Program to stack and then unstack

import pandas as pd
df = pd.read_csv("myexcel.csv")
# reshape the dataframe using stack() method
df_stacked = df.stack()
print(df_stacked.head(26))
# unstack() method
df_unstacked = df_stacked.unstack()
print(df_unstacked.head(10))


#Program for concatenating the dictionaries
# importing pandas module
import pandas as pd
# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

# Define a dictionary containing employee data
data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])
# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])
print(df, "\n\n", df1)
# using a .concat() method
frames = [df, df1]
res1 = pd.concat(frames)
print(res1)

#Program for time series
import pandas as pd
from datetime import datetime
import numpy as np
range_date = pd.date_range(start='1/1/2019', end='1/08/2019', freq='Min')
print(range_date)

##Program to export DataFrame to a csv
import pandas as pd
data = pd.read_csv("BankWages.csv")
data.to_csv("CopyOfBankWages.csv")

#Program to export DataFrame to a csv
# importing pandas as pd
import pandas as pd

# list of name, degree, score
nme = ["Priyanka", "Rohan", "Sudheer", "Shelen"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('file1.csv')

