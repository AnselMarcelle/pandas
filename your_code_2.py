import pandas as pd
df = pd.read_csv('GoogleApps.csv')
print(df.info())
print('end')
print(df[df['Type'] == 'Paid']['Price'].min())
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())
print(df[df['Type'] == 'Free']['Reviews'].max() - df[df['Type'] == 'Paid']['Reviews'].max())
print(df[df['Content Rating'] == 'Teen']['Size'].min())
print(df['Reviews'].max)