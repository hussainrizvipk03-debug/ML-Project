import pandas as pd 
df = pd.read_csv('Salary Data.csv')
# this is for loading the first 10 of the dataset 
""" print(df.head(10))


# Exploratory data analysis 


# first we will check the shape -> this tells the number of rows and the number of columns present in the dataset 
# my dataset has 375 rows and 6 columns 

print(df.shape)"""


# now for checking the datatypes of each column i will use another function 


# print(df.dtypes)
"""
print(df.info())
"""
# this tells the total count for the missing valeues in the dataset 
"""
print(df.isnull().sum())
"""


# this is for the numerical stats of the dataset 
"""
print(df.describe())


print(df.info())
print(df.shape)
"""
"""
print(df.isnull().sum())
"""

"""
print(df.dropna(how='all', inplace=True))

inplace = True modifies the original dataset and then returns the rows and column left 
"""
print(df.shape)
"""
unique_ct = df['Education Level'].value_counts()
print(unique_ct)
"""


"""

cat_columns = df.select_dtypes(include=['object']).columns
unique_counts = df.stack().value_counts()

print(unique_counts)
"""
