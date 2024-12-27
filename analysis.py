import pandas as pd
import numpy
import matplotlib.pyplot as plt

df = pd.read_csv('business data.csv')
print(df.describe())

#average revenue through all the products
mean_revenue = df['age'].mean()
count_category = df['category'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(count_category, labels=count_category.index, autopct='%1.1f%', startangle=140)
plt.title('category')
plt.show()

sales = list(df['sales'])
products = list(df['product'])
revenue = list(df['revenue'])

plt.bar(products, sales)
plt.title('product sales')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()


