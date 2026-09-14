import pandas as pd
import sys

print("Empty data frame")
df = pd.DataFrame()
print(df)

print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

print("Dataframe with list")
data = [['Abc',4],['Bcd',3],['Pqr',3],['Rst',3]]
df = pd.DataFrame(data,columns=['Name','Duration'])
print(pd)

data = {'Name':['ABC','BCD','CDE','DEF'],'Duration':[4,3,3,3]}
df = pd.DataFrame(data)
print(df)

#data = [{'Name':'ABC','Duration':3,'Fees':10500},{'Name':'DEF', 'Duration':3, 'Fees':10500},{'Name':'BCD', 'Fees':10500},{'Name':'CDE', 'Fees':10500}]
data = [{'Name':'ABC','Duration':3,'Fees':10500},{'Name':'DEF', 'Duration':3, 'Fees':10500},{'Name':'BCD', 'Duration':3, 'Fees':10500},{'Name':'CDE', 'Duration':4, 'Fees':10500}]
df = pd.DataFrame(data)
print(df)

d = {'one' : pd.Series([1,2,3], index = ['a','b','c']),'two': pd.Series([1,2,3,4], index = ['x','y','z','w'])}

df = pd.DataFrame(d)
print(df['one'])

print("Pandas version: ")
print(pd.__version__)
print("\nPython version: ")
print(sys.version)
