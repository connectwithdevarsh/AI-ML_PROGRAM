import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('vgsalesGlobale.xlsx')

print("--- SECTION 1: DataFrame Basics ---")

print("1. First 10 rows")
print(df.head(10))

print("\n2. Total rows and columns")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n3. Column names and Data types")
print(df.columns)
print(df.dtypes)

print("\n4. Describe dataframe")
print(df.describe())

print("\n5. Number of unique Platform values")
print(df['Platform'].nunique())

print("\n6. Games released by each Publisher")
print(df['Publisher'].value_counts())

print("\n--- SECTION 2: Data Exploration ---")

print("1. First five Name and Platform values")
print(df[['Name', 'Platform']].head())

print("\n2. Last five rows where Genre is Sports")
sports_data = df[df['Genre'] == 'Sports']
print(sports_data.tail())

print("\n3. Average Global_Sales and NA_Sales")
print("Average Global_Sales:", df['Global_Sales'].mean())
print("Average NA_Sales:", df['NA_Sales'].mean())

print("\n4. Maximum Global_Sales and corresponding Name")
max_sales = df['Global_Sales'].max()
print("Maximum Global_Sales:", max_sales)
game_record = df[df['Global_Sales'] == max_sales]
print("Name:", game_record['Name'].iloc[0])

print("\n5. Missing values of every column")
print(df.isnull().sum())

print("\n6. Only Name, Genre, Global_Sales")
print(df[['Name', 'Genre', 'Global_Sales']])

print("\n7. 100th game record")
print(df.iloc[99])

print("\n8. Games released after 2010")
print(df[df['Year'] > 2010])

print("\n9. Games where Global_Sales > 10")
print(df[df['Global_Sales'] > 10])

print("\n10. Games published by Nintendo")
print(df[df['Publisher'] == 'Nintendo'])

print("\n11. Top five games based on EU_Sales")
top_eu = df.sort_values('EU_Sales', ascending=False)
print(top_eu.head())

print("\n12. Games where Genre == Action AND Platform == PS2")
action_ps2 = df[(df['Genre'] == 'Action') & (df['Platform'] == 'PS2')]
print(action_ps2)

print("\n--- SECTION 3: Grouping & Aggregation ---")

print("1. Average Global_Sales by Genre")
avg_genre = df.groupby('Genre')['Global_Sales'].mean()
print(avg_genre)

print("\n2. Game count by Platform")
plat_count = df.groupby('Platform')['Name'].count()
print(plat_count)

print("\n3. Total Global_Sales by Publisher")
pub_sales = df.groupby('Publisher')['Global_Sales'].sum()
print(pub_sales)

print("\n4. Maximum JP_Sales by Genre")
jp_max = df.groupby('Genre')['JP_Sales'].max()
print(jp_max)

print("\n5. Total NA_Sales by Year")
na_year = df.groupby('Year')['NA_Sales'].sum()
print(na_year)

print("\n6. Average EU_Sales by Platform")
eu_plat = df.groupby('Platform')['EU_Sales'].mean()
print(eu_plat)

print("\n--- SECTION 4: Visualization ---")

print("1. Bar Chart: Games per Genre")
genre_counts = df['Genre'].value_counts()
genre_counts.plot(kind='bar')
plt.title('Games per Genre')
plt.xlabel('Genre')
plt.ylabel('Game Count')
plt.show()

print("2. Histogram: Global_Sales")
df['Global_Sales'].plot(kind='hist')
plt.title('Global_Sales Histogram')
plt.xlabel('Global_Sales')
plt.ylabel('Frequency')
plt.show()

print("3. Pie Chart: Platform Distribution")
plat_dist = df['Platform'].value_counts().head(10)
plat_dist.plot(kind='pie')
plt.title('Platform Distribution')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.show()

print("4. Scatter Plot: NA_Sales vs Global_Sales")
df.plot(kind='scatter', x='NA_Sales', y='Global_Sales')
plt.title('NA_Sales vs Global_Sales')
plt.xlabel('NA_Sales')
plt.ylabel('Global_Sales')
plt.show()

print("5. Line Chart: Total Global_Sales by Year")
year_sales = df.groupby('Year')['Global_Sales'].sum()
year_sales.plot(kind='line')
plt.title('Total Global_Sales by Year')
plt.xlabel('Year')
plt.ylabel('Global_Sales')
plt.show()

print("6. Bar Chart: Top 10 Publishers based on Global_Sales")
top_pubs = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
top_pubs.plot(kind='bar')
plt.title('Top 10 Publishers by Global_Sales')
plt.xlabel('Publisher')
plt.ylabel('Global_Sales')
plt.show()
