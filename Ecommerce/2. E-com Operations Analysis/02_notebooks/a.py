# %%
"""
04_visualization.ipynb
Polished and evidence-backed visualizations for Olist E-Commerce Ops Analysis
Author: [Your Name]
"""

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# %%
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)
pd.set_option('display.max_columns', None)

# %%
# Load curated enriched orders
orders_enriched = pd.read_csv(Path("..") / "03_curated" / "orders_enriched.csv")

# %%
# Aggregate seller-level KPIs
seller_kpis = (
    orders_enriched.groupby("seller_id").agg(
        order_volume=('order_id','count'),
        avg_processing_time=('processing_time','mean'),
        avg_shipping_time=('shipping_time','mean'),
        avg_delivery_time=('delivery_time','mean'),
        late_shipping_count=('late_shipping_flag','sum'),
        extreme_shipping_count=('extreme_delivery_flag','sum')
    ).reset_index()
)

seller_kpis['late_shipping_rate'] = seller_kpis['late_shipping_count'] / seller_kpis['order_volume']
seller_kpis['extreme_shipping_rate'] = seller_kpis['extreme_shipping_count'] / seller_kpis['order_volume']

# %%
# Aggregate regional KPIs
regional_kpis = (
    orders_enriched.groupby('customer_state')
    .agg(order_volume=('order_id','count'),
         avg_delivery_time=('delivery_time','mean'),
         late_delivery_count=('late_delivery_flag','sum'))
    .reset_index()
)
regional_kpis['late_delivery_rate'] = regional_kpis['late_delivery_count'] / regional_kpis['order_volume']

# %%
# -------------------------------
# SECTION 1: Order Lifecycle Distributions
# -------------------------------

plt.figure(figsize=(10,6))
sns.boxplot(data=orders_enriched[['processing_time','shipping_time','delivery_time']], palette='Set2')
plt.title("Order Lifecycle Times: Processing, Shipping, Delivery")
plt.ylabel("Days")
plt.show()

# Focus on relevant range (0-30 days) to highlight operational delays
plt.figure(figsize=(10,5))
sns.boxplot(x='variable', y='value',
            data=pd.melt(orders_enriched[['processing_time','shipping_time','delivery_time']]),
            palette='Set2')
plt.ylim(0,30)
plt.title("Order Lifecycle Times (0–30 Days Focus)")
plt.ylabel("Days")
plt.show()

# %%
# -------------------------------
# SECTION 2: Delivery Delay Distribution
# -------------------------------

delayed_orders = orders_enriched[orders_enriched['delivery_delay'] > 0]

plt.figure(figsize=(10,5))
sns.histplot(delayed_orders['delivery_delay'], bins=50, color='tomato')
plt.title("Distribution of Delivery Delays (days)")
plt.xlabel("Delivery Delay (days)")
plt.ylabel("Number of Orders")
plt.show()

# %%
# -------------------------------
# SECTION 3: Top Sellers Driving Delays (Impact Analysis)
# -------------------------------

# Compute impact score: late_shipping_rate * order_volume
seller_kpis['impact_score'] = seller_kpis['late_shipping_rate'] * seller_kpis['order_volume']

# Top 10 sellers by impact
top_sellers = seller_kpis.sort_values('impact_score', ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x='seller_id', y='impact_score', data=top_sellers, palette='Reds_r')
plt.xticks(rotation=45)
plt.title("Top 10 Sellers by Late Shipment Impact (Volume × Rate)")
plt.ylabel("Late Shipments Impact")
plt.xlabel("Seller ID")
plt.show()

# Scatter plot: Volume vs Late Rate
plt.figure(figsize=(10,6))
sns.scatterplot(x='order_volume', y='late_shipping_rate', data=seller_kpis, alpha=0.5)
plt.scatter(top_sellers['order_volume'], top_sellers['late_shipping_rate'], color='red', s=100, label='Top 10 Impact')
plt.title("Seller Volume vs Late Shipping Rate")
plt.xlabel("Order Volume")
plt.ylabel("Late Shipping Rate")
plt.legend()
plt.show()

# %%
# -------------------------------
# SECTION 4: Volume Bucket Analysis
# -------------------------------

# Define volume buckets
seller_kpis['volume_bucket'] = pd.cut(seller_kpis['order_volume'],
                                     bins=[0,50,200,500,1000,10000],
                                     labels=['Very Low','Low','Medium','High','Very High'])

volume_summary = seller_kpis.groupby('volume_bucket').agg(
    avg_late_rate=('late_shipping_rate','mean'),
    avg_order_volume=('order_volume','mean'),
    avg_late_shipments=('impact_score','mean')
).reset_index()

plt.figure(figsize=(10,5))
sns.barplot(x='volume_bucket', y='avg_late_shipments', data=volume_summary, palette='Blues_r')
plt.title("Average Late Shipments by Seller Volume Bucket")
plt.ylabel("Avg Late Shipments (Impact Score)")
plt.xlabel("Seller Volume Bucket")
plt.show()

# %%
# -------------------------------
# SECTION 5: Regional Performance
# -------------------------------

# Average delivery time by state
regional_sorted = regional_kpis.sort_values('avg_delivery_time', ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x='customer_state', y='avg_delivery_time', data=regional_sorted, palette='Blues_r')
plt.xticks(rotation=45)
plt.title("Average Delivery Time by Customer State")
plt.ylabel("Avg Delivery Time (days)")
plt.xlabel("Customer State")
plt.show()

# Late delivery rate by state
plt.figure(figsize=(12,6))
sns.barplot(x='customer_state', y='late_delivery_rate', data=regional_sorted, palette='Oranges_r')
plt.xticks(rotation=45)
plt.title("Late Delivery Rate by Customer State")
plt.ylabel("Late Delivery Rate")
plt.xlabel("Customer State")
plt.show()

# %%
# -------------------------------
# SECTION 6: Extreme Delays
# -------------------------------

extreme_orders = orders_enriched[orders_enriched['extreme_delivery_flag']]

plt.figure(figsize=(10,5))
sns.histplot(extreme_orders['delivery_time'], bins=30, color='tomato')
plt.title("Extreme Delivery Times (>30 days)")
plt.xlabel("Delivery Time (days)")
plt.ylabel("Number of Orders")
plt.show()

# Highlight top sellers causing extreme delays
extreme_seller_counts = extreme_orders['seller_id'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=extreme_seller_counts.index, y=extreme_seller_counts.values, palette='Reds_r')
plt.xticks(rotation=45)
plt.title("Top Sellers with Extreme Delivery Delays")
plt.ylabel("Number of Extreme Delays")
plt.xlabel("Seller ID")
plt.show()

# %%
# -------------------------------
# END OF NOTEBOOK
# -------------------------------
