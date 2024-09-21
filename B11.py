#pandas
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales.csv')
print(df)
df['amt']=df['qty']*df['price']
total_sales=df['amt'].sum()
print(f"total sales of al transactions={total_sales}")

df_total_amt_product=df.groupby('product')['amt'].sum().reset_index()
df_total_amt_product.columns=['product','total_amt']
print(df_total_amt_product)

df_avg_sales_product=df.groupby('product')['amt'].mean().reset_index()
df_avg_sales_product.columns=['product','avg_sales']
print(df_avg_sales_product)

df_total_amt_product.plot(kind='bar',x='product',y='total_amt',title='bar chart showing total amt of each product', color=['red','blue','green'])

df_total_amt_product.plot(kind='pie', y='total_amt', labels=['redmi','realme','samsung','vivo','iphone'], autopct='%1.1f%%',title='pie chart showing percentage wise total amt of each product')
plt.show()