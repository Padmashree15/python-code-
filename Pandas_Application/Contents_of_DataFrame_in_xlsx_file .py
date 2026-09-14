import pandas as pd

data = [{'Name':'ABC','Duration': 3, 'Fees':10500},{'Name':'BCD','Duration':3},{'Name':'Python','Fees':10500}]
df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('PadmashreePandas.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.close()