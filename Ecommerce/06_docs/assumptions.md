# Assumptions - Olist Operations Analysis

## Overview

This document records all assumptions, business rules, and transformations applied to the dataset. It ensures reproducibility, clarifies choices, and helps reviewers understand logic.

---

## `order_status` filterning

- Only orders with status = 'delivered' were included in SLA and delivery KPIs
- Orders in intermediate states (created, approved, invoiced, processing, shipped)
  were excluded due to incomplete lifecycle data
- Cancelled and unavailable orders were excluded from operational performance metrics
- *Notebook: 02_data_cleaning*

## Timestamps cleaning `orders`

- Orders missing `order_approved_at` (14 rows) or `order_delivered_customer_date` (8 rows) were dropped
- One order had a missing `order_delivered_carrier_date` after prior cleaning steps.
- Decision: drop this single row due to negligible impact on analysis (<0.001% of dataset).
- *Notebook: 02_data_cleaning*

## Processing & Delivery Time Assumptions

- Orders with negative shipping_time or delivery_time were removed as data errors
- Processing time greater than 7 days flagged as slow approval
- Shipping time greater than 30 days flagged as extreme shipping delay
- Delivery time greater than 30 days flagged as extreme delivery delay
- Extreme delays were retained to preserve operational failure insights

## Seller Attribution Assumption

- Orders may contain items from multiple sellers
- For operational analysis, each order was attributed to the seller of the first order item (order_item_id = 1)
- This preserves one-row-per-order grain and avoids duplication

## Seller Performance Assumptions

- Sellers are judged only by `shipping_time`. `Delivery_time` reflects logistics performance and is excluded from seller underperformance scoring
- Low-volume sellers (<1% mean order volume) are labeled inactive to reduce noise
- `underperformance_score` combines `late_shipping_flag` and `slow_processing_flag` for holistic operational risk
- `seller_status` thresholds:
  - Underperforming: high `late_shipping_rate` or `slow_processing_rate`
  - Watchlist: medium rates, requires monitoring
  - Healthy: low rates

## Late Shipments Concentration

- Cumulative analysis identifies high-impact sellers
- Finding: top 0.4% of active sellers account for ~25% of late handovers to logistics
- Columns `cum_late_shipments` and `cum_late_share` quantify concentration

## Interpretation

- Seller KPIs reflect seller operational responsibility only
- Observed late shipment concentration highlights a small fraction of sellers driving majority of operational delays

## Impact vs Reliability Framework

| Quadrant                           | Impact | Reliability | Interpretation                                 | Action                           |
| ---------------------------------- | ------ | ----------- | ---------------------------------------------- | -------------------------------- |
| **High Impact / Low Reliability**  | High   | Poor        | **Critical sellers** driving systemic failures | Immediate ops intervention       |
| **High Impact / High Reliability** | High   | Good        | Scale amplifies small inefficiencies           | Process optimization             |
| **Low Impact / Low Reliability**   | Low    | Poor        | Noisy / inconsistent sellers                   | Governance or activation control |
| **Low Impact / High Reliability**  | Low    | Good        | Healthy long-tail sellers                      | No action                        |

## Low vs high volume sellers impact

- Low-volume sellers (≤7 orders over the analysis period) exhibit higher late shipping rates on a per-order basis (8.6% vs 5.7% for higher-volume sellers), indicating lower operational reliability. However, their limited scale — averaging fewer than 3 orders per seller — results in an expected contribution of less than 0.3 late shipments per seller. In contrast, higher-volume sellers generate over 15× more late shipments per seller despite better reliability, capping the total operational impact of low-volume sellers.
  
## 1. Orders and Delivery

- Following `order_status` are **excluded** from delivery perfomance analysis: ('invoiced', 'shipped', 'processing', 'unavailable','canceled', 'created', 'approved')
- pass
- Orders with missing `order_delivered_customer_date` are treated as **undelivered**.
- Late delivery is defined as **actual delivery > estimated delivery**.
- Cancelled orders (`order_status = cancelled`) are **excluded** from delivery performance analysis.
- Negative or zero processing/shipping times are considered **data errors** and removed.

---

## 2. Multi-item Orders

- Metrics are calculated **per order**, not per item, unless specified.
- Shipping times are based on the earliest shipped item in multi-item orders.

---

## 3. Geolocation & Distance

- Distances between seller and customer are calculated using **lat/lng** from geolocation table.
- Missing geolocation data is ignored for distance-based analysis.

---

## 4. Reviews

- Only consider reviews for **delivered orders** when analyzing satisfaction vs delivery time.
- Review creation date is used to check **timeliness of feedback**.

---

## 5. Data Cleaning / Transformations

- Raw data is never overwritten; all cleaning occurs in **interim / curated datasets**.
- All date/time columns are converted to **datetime** objects for calculations.
- Categorical fields are standardized (lowercase, trimmed whitespace).

---

## 6. KPIs / Metrics

- **Order Cycle Time** = `order_delivered_customer_date - order_approved_at`
- **Processing Time** = `order_approved_at - order_purchase_timestamp`
- **Shipping Time** = `order_delivered_carrier_date - order_approved_at`
- **Delivery Delay Flag** = `True` if `order_delivered_customer_date > order_estimated_delivery_date`, else `False`
- Aggregation for SLA: by **seller**, **state**, **category**, and **month**.
