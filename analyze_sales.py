import pandas as pd
from pathlib import Path

df = pd.read_csv(Path('retail_sales_dataset.csv'), parse_dates=['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)
df['Weekday'] = df['Date'].dt.day_name()
df['Weekend'] = df['Weekday'].isin(['Saturday','Sunday'])

def price_class(price):
    if price <= 50:
        return 'Budget'
    elif price == 300:
        return 'Mid-Range'
    elif price == 500:
        return 'Premium'
    return 'Other'

df['Price Class'] = df['Price per Unit'].apply(price_class)
df['Age Group'] = pd.cut(df['Age'], bins=[0,25,35,45,55,65], labels=['Young','Millennial','Gen X','Boomer','Senior'], include_lowest=True)

summary = []
summary.append(f"Total revenue: {df['Total Amount'].sum()}")
summary.append(f"Total transactions: {len(df)}")
summary.append(f"Unique customers: {df['Customer ID'].nunique()}")
summary.append(f"Overall AOV: {df['Total Amount'].mean():.2f}")
summary.append('')
cat = df.groupby('Product Category')['Total Amount'].agg(['sum','count','mean']).sort_values('sum', ascending=False)
summary.append('Revenue by category:')
for idx,row in cat.iterrows():
    summary.append(f"{idx}: revenue={row['sum']}, transactions={row['count']}, avg order={row['mean']:.2f}")
summary.append('')
price_class_stats = df.groupby('Price Class')['Quantity'].agg(['sum','count','mean'])
summary.append('Quantity by price class:')
for idx,row in price_class_stats.iterrows():
    summary.append(f"{idx}: total qty={row['sum']}, transactions={row['count']}, avg qty={row['mean']:.2f}")
summary.append('')
quart = df.groupby('Quarter')['Total Amount'].agg(['sum','count']).sort_values('sum', ascending=False)
summary.append('Revenue by quarter:')
for idx,row in quart.iterrows():
    summary.append(f"{idx}: revenue={row['sum']}, transactions={row['count']}")
summary.append('')
week = df.groupby(df['Weekend'])['Total Amount'].agg(['sum','count','mean'])
summary.append('Weekend vs Weekday revenue:')
for idx,row in week.iterrows():
    label = 'Weekend' if idx else 'Weekday'
    summary.append(f"{label}: revenue={row['sum']}, transactions={row['count']}, avg={row['mean']:.2f}")
summary.append('')
seg = df.groupby(['Age Group','Gender'])['Total Amount'].agg(['sum','count','mean']).sort_values('sum', ascending=False)
summary.append('Top age-gender segments by revenue:')
for (age,gender),row in seg.head(5).iterrows():
    summary.append(f"{age} {gender}: revenue={row['sum']}, tx={row['count']}, avg={row['mean']:.2f}")
print('\n'.join(summary))
