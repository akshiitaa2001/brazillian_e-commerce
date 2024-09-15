
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the Orders dataset
orders = pd.read_csv('olist_orders_dataset.csv')  # Adjust the file path as needed

# Convert order_purchase_timestamp to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Extracting year and month
orders['year_month'] = orders['order_purchase_timestamp'].dt.to_period('M')

# Sales trends over time (number of orders per month)
sales_trends = orders.groupby('year_month').size()

# Plotting the sales trends
plt.figure(figsize=(12, 6))
sales_trends.plot(kind='line')
plt.title('Sales Trends Over Time (Monthly)')
plt.xlabel('Year and Month')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a file
plt.savefig('sales_trends_over_time.png')
