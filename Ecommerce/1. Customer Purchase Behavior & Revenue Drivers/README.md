# Customer Sales Analysis Dataset

Dataset: [Link](https://www.kaggle.com/datasets/carrie1/ecommerce-data?select=data.csv") 

## Key Points
- Customers are mostly wholesalers.
- Dataset period: 01/12/2010 - 09/12/2011.
- The company mainly sells unique all-occasion gifts.

### Problem Statement & Questions
How can the company optimize revenue, customer retention, and inventory efficiency by better understanding customer purchasing behavior, product performance, and sales patterns across markets?

- **Which customers generate the most revenue, and how can we increase their loyalty?**
- **What products are underperforming, and should we discontinue or promote them more heavily?**
- **How do sales trends vary by country, and what can we do to optimize performance in underperforming regions?**
- **What is the return rate by product, and how can we reduce returns to improve profitability?**
- **What are the seasonal buying patterns, and how can we optimize inventory and promotions around these periods?**

### Final Outputs Metrics
1. **Revenue by Customer & Product**
    - Top 10 Customers by Revenue
    - Top 10 Products by Revenue
    - Revenue per Product Category
2. **Customer Segmentation & Buying Patterns**
    - Customer Lifetime Value (CLV) – Estimated future revenue from each customer.
    - Frequency of Purchase – Average number of purchases per customer within a time period.
    - Average Order Value (AOV) – The average amount spent per order for each customer group.
3. **Sales Trends & Seasonality**
    - Monthly/Quarterly Sales Trend
    - Seasonal Demand Patterns
4. **Product Performance & Inventory Optimization**
    - Slow-Moving Products – Products with low sales or excess inventory.
    - Stockouts & Overstock Analysis – Frequency of stockouts for popular products or overstocked items.
5. **Sales by Country/Region**
    - Total Sales by Country
    - Country Growth Rate – Growth in revenue per country over time, identifying high-potential markets.
    - Regional Market Share – Comparing the company’s sales to overall market potential in different countries.
6. **Customer Acquisition and Retention Rates**
    - Customer Churn Rate – Percentage of customers who stopped buying after a certain period.
    - New vs. Returning Customer Sales – Revenue split between new customers and repeat buyers.
    - Customer Retention Rate – Percentage of customers who make repeat purchases.

#### The final outputs could include:
- A **Customer Insights Dashboard** that shows customer segmentation, purchasing patterns, and lifetime value.
- A **Product Performance Report** to help identify which products to focus on, promote, or discontinue.
- A **Geographic Sales Report** highlighting performance across different countries/regions.
- A **Revenue Forecasting Model** based on sales trends, seasonality, and customer purchasing behavior.
- A **Return & Satisfaction Analysis** to reduce returns and improve product offerings.

## Dataset Overview
The dataset consists of 8 columns and contains transactional data for a period from December 1, 2010, to December 9, 2011. Each transaction includes details about the product, quantity, price, and customer information.

### Data Columns:
| Column      | Description |
|-------------|-------------|
| **InvoiceNo** | Invoice number for the transaction. |
| **StockCode** | Unique code for each product. |
| **Description** | Product description. |
| **Quantity** | Number of units sold. |
| **InvoiceDate** | Date and time of the transaction. |
| **UnitPrice** | Price per unit of the product. |
| **CustomerID** | Unique identifier for each customer. |
| **Country** | Country where the customer is based. |

### Example Data:
```plaintext
InvoiceNo   | StockCode | Description                                  | Quantity | InvoiceDate          | UnitPrice | CustomerID | Country
------------|-----------|----------------------------------------------|----------|----------------------|-----------|------------|---------
536365      | 85123A    | WHITE HANGING HEART T-LIGHT HOLDER           | 6        | 12/1/2010 8:26       | 2.55      | 17850.0    | United Kingdom
536365      | 71053     | WHITE METAL LANTERN                         | 6        | 12/1/2010 8:26       | 3.39      | 17850.0    | United Kingdom
536365      | 84406B    | CREAM CUPID HEARTS COAT HANGER              | 8        | 12/1/2010 8:26       | 2.75      | 17850.0    | United Kingdom
536365      | 84029G    | KNITTED UNION FLAG HOT WATER BOTTLE         | 6        | 12/1/2010 8:26       | 3.39      | 17850.0    | United Kingdom
536365      | 84029E    | RED WOOLLY HOTTIE WHITE HEART               | 6        | 12/1/2010 8:26       | 3.39      | 17850.0    | United Kingdom
```

## Data Overview

- **Non-null Count**: 541,909 rows.

### Missing Data:
- 540,455 non-null values in the "Description" column.
- 406,829 non-null values in the "CustomerID" column.

### Data Types:
- **InvoiceNo**: object
- **StockCode**: object
- **Description**: object
- **Quantity**: int64
- **InvoiceDate**: object
- **UnitPrice**: float64
- **CustomerID**: float64
- **Country**: object

## Loading the Data:
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Inspect the data
print(df.head())
print(df.info())
```





