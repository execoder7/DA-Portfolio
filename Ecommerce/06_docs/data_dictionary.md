# Data Dictionary - Olist Brazilian E-Commerce

## Overview

This document describes all tables, fields, data types, primary keys, foreign keys, and notes for the Olist dataset. It is intended to help with understanding, joining, and transforming data safely.

---

## Datasets Info

### 1. orders

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| order_id | string | Unique identifier for each order | O1001 | Primary key |
| customer_id | string | Customer(!unique) placing the order | C2001 | FK to customers table |
| order_status | string | Status of order (delivered, shipped, cancelled, etc.) | delivered | Useful for filtering completed orders |
| order_purchase_timestamp | datetime | Timestamp when order was placed | 2018-01-01 10:05 | |
| order_approved_at | datetime | Timestamp when order was approved | 2018-01-02 08:30 | Can be used to calculate processing time |
| order_delivered_carrier_date | datetime | When order was handed to the carrier | 2018-01-03 15:00 | Useful for shipping duration |
| order_delivered_customer_date | datetime | When order was delivered to customer | 2018-01-06 12:00 | Used to calculate delivery time |
| order_estimated_delivery_date | datetime | Estimated delivery promised | 2018-01-05 12:00 | Compare with actual for SLA |

**Grain**: order_id (1 row per 1 order)

---

### 2. order_items

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| order_id | string | Order reference | O1001 | FK to orders |
| order_item_id | int | Item sequence in order | 1 | Primary key within order_id |
| product_id | string | Unique product | P3001 | FK to products table |
| seller_id | string | Seller fulfilling the order | S4001 | FK to sellers table |
| shipping_limit_date | datetime | Shipping deadline promised by seller | 2018-01-04 17:00 | Compare to actual shipping date |
| price | float | Product price | 100.50 | |
| freight_value | float | Shipping cost | 10.00 | |

**Grain**:  1 row per  item per order (composite key: order_id, order_item_id)

---

### 3. customers

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| customer_id | string | Unique customer ID | C2001 | PK |
| customer_unique_id | string | Unique customer identifier across multiple orders | CU12345 | Can be used to identify repeat customers |
| customer_zip_code_prefix | int | Customer postal code | 01001 | Can join with geolocation |
| customer_city | string | City | Sao Paulo | |
| customer_state | string | State abbreviation | SP | |

**Grain**: customer_id (1 row per 1 customer order)(!unique)

---

### 4. sellers

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| seller_id | string | Unique seller ID | S4001 | PK |
| seller_zip_code_prefix | int | Seller postal code | 01002 | Can join with geolocation |
| seller_city | string | City | Sao Paulo | |
| seller_state | string | State abbreviation | SP | |

**Grain**: seller_id ( 1 row per 1 seller)

---

### 5. payments

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| order_id | string | Order reference | O1001 | FK to orders |
| payment_type | string | Payment method | credit_card | |
| payment_installments | int | Number of installments | 1 | |
| payment_value | float | Amount paid | 110.50 | |

---

### 6. order_reviews

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| review_id | string | Unique review | R5001 | PK |
| order_id | string | Order being reviewed | O1001 | FK to orders |
| review_score | int | 1-5 rating | 5 | Use as customer satisfaction proxy |
| review_comment_title | string | Short title | Great! | Optional |
| review_comment_message | string | Full comment | Excellent service | Optional |
| review_creation_date | datetime | When review created | 2018-01-07 | Useful to track feedback timing |
| review_answer_timestamp | datetime | When seller responded | 2018-01-08 | Optional |

---

### 7. geolocation

| Column | Type | Description | Example | Notes |
| -------- | ------ | ------------- | -------- | ------ |
| zip_code_prefix | int | Postal code | 01001 | Can join with seller/customer |
| lat | float | Latitude | -23.5505 | |
| lng | float | Longitude | -46.6333 | |

## Primary Datasets

### order_items

- shipping_limit_date per order | For calculating order delays

### customer

- customer_city, customer_state | Delay analysis by customer & seller distance

### sellers

- seller_city, seller_state | Delay analysis by customer & seller distance
  
### orders

- order_status | for excluding `cancelled`
- Delay Analysis
  - order_purchase_timestamp
  - order_approved_at
  - order_delivered_carrier_date
  - order_delivered_customer_date
  - order_estimated_delivery_date

## Feature Engineering

### `orders`

- Processing time: `order_approved_at` - `order_purchase_timestamp`
- Shipping time: `order_delivered_carrier_date` - `order_approved_at` → used to evaluate seller operational performance
- Delivery time: `order_delivered_customer_date` - `order_delivered_carrier_date` → used to evaluate logistics performance
- IsSlowApproval: `processing_time` > 7
- late_shipping_flag: True if `shipping_time` exceeds SLA threshold → identifies orders where seller was late handing to logistics
- late_delivery_flag: True if `delivery_time` > promised delivery → identifies logistics delay, not seller responsibility
- extreme_shipping_flag: True if `shipping_time` > 30 days
- extreme_delivery_flag: True if `delivery_time` > 30 days

### Seller kpis (aggregation)

- order_volume = number of orders per seller
- avg_processing_time = mean `processing_time` per seller
- avg_shipping_time = mean `shipping_time` per seller (core seller performance metric)
- slow_processing_rate = fraction of orders with `processing_time` > 7 days
- late_shipping_rate = fraction of orders with `late_shipping_flag` = True
- underperformance_score = sum of slow processing and late shipping flags
- seller_status = classified as Healthy, Watchlist, Underperforming based on thresholds of shipping metrics
- late_shipments = total number of late shipments per seller
- cum_late_shipments = cumulative late shipments in descending order
- cum_late_share = % of total late shipments accounted for by cumulative sellers
- seller_share = % of total sellers represented cumulatively

## Notes

- Only active sellers (order_volume ≥1% of mean seller order volume) are included in operational analysis
- Metrics are seller-centric, i.e., shipping times reflect seller responsibility; delivery times reflect logistics, not seller performance
- Analysis shows top 0.4% of active sellers account for ~25% of late handovers to logistics

