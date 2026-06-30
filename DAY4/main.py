import pandas as pd

df = pd.read_excel('University_Admissions_Data.xlsx')

print("1. First five rows")
print(df.head())

print("\n2. Total number of rows and columns")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n3. Column Names and Data Types")
print(df.dtypes)

print("\n4. Department and Admitted columns")
print(df[['Department', 'Admitted']])

print("\n5. Unique Department names")
print(df['Department'].unique())

print("\n6. Total Applicants")
print(df['Applicants'].sum())

print("\n7. Total Admitted students")
print(df['Admitted'].sum())

print("\n8. Average Applicants")
print(df['Applicants'].mean())

print("\n9. Maximum Applicants")
print(df['Applicants'].max())

print("\n10. Minimum Admitted students")
print(df['Admitted'].min())

print("\n11. Records where Year == 2024")
print(df[df['Year'] == 2024])

print("\n12. Records where Department == Civil")
print(df[df['Department'] == 'Civil'])

print("\n13. Records where Gender == Female")
print(df[df['Gender'] == 'Female'])

print("\n14. Records where Applicants > 450")
print(df[df['Applicants'] > 450])

print("\n15. Records where Gender == Male AND Department == Mechanical")
print(df[(df['Gender'] == 'Male') & (df['Department'] == 'Mechanical')])

print("\n16. Records where Year == 2023 AND Admitted > 200")
print(df[(df['Year'] == 2023) & (df['Admitted'] > 200)])

print("\n17. Sort Applicants in ascending order")
print(df.sort_values('Applicants'))

print("\n18. Sort Admitted in descending order")
print(df.sort_values('Admitted', ascending=False))

print("\n19. Count Female applicants without using groupby")
print(len(df[df['Gender'] == 'Female']))

print("\n20. Create new column Rejected")
df['Rejected'] = df['Applicants'] - df['Admitted']
print(df)
