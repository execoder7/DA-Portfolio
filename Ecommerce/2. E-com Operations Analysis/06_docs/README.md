# Order Fulfillment & Seller Operations Performance Analysis

**Olist Brazilian E-Commerce Public Dataset**

---

## Project Overview

This project analyzes **seller-controlled order fulfillment performance** using the **Brazilian E-Commerce Public Dataset by Olist**. The objective is to evaluate operational performance within the seller fulfillment lifecycle, identify SLA breaches, and highlight high-impact sellers contributing disproportionately to delays.

Delivery-related metrics are used for **diagnostic context**, while operational accountability and decision-making are intentionally focused on seller-controlled stages.

The analysis is designed as a **Business / Operations Analyst case study**, emphasizing operational KPIs, seller performance monitoring, and escalation-ready insights rather than revenue optimization or customer segmentation.

---

## Business Objective

Improve seller-controlled fulfillment efficiency by answering the following operational questions (as defined in the project blueprint):

- Which seller-controlled stages of fulfillment contribute most to SLA breaches?
- How does fulfillment performance vary across sellers when evaluated relative to peers?
- Which sellers disproportionately contribute to late shipments, and how concentrated is their impact?
- How should operations teams prioritize seller interventions to reduce late shipments with maximum impact?

---

## Dataset Context

- **Source**: Brazilian E-Commerce Public Dataset by Olist (Kaggle)
- **Domain**: Marketplace seller fulfillment operations
- **Scope**: Orders, sellers, customers, order items, and fulfillment-related timestamps
- **Timeframe**: Historical transactional data provided by Olist

The dataset represents a real-world multi-seller e-commerce marketplace and is suitable for simulating seller performance monitoring and SLA governance.

---

## Analytical Scope & Non-Goals

### In Scope

- Seller fulfillment lifecycle analysis (order approval → shipping handover)
- Seller operational performance (processing & shipping)
- Seller fulfillment SLA adherence
- Impact-based prioritization of operational issues

### Explicitly Out of Scope

- Revenue or pricing analysis
- Customer behavior or segmentation
- Logistics carrier or last-mile performance evaluation
- Predictive modeling or machine learning

---

## Analytical Approach (High-Level)

The project follows an operations-first analytical workflow:

1. **Data auditing & schema validation**  
   Verified table grains, relationships, and completeness across core datasets.

2. **Data cleaning & filtering**
   - Restricted analysis to **delivered orders** with complete fulfillment timestamps
   - Removed invalid or negative time intervals
   - Preserved raw, interim, and curated datasets for reproducibility

3. **Operational KPI engineering**
   - Processing time (order placed → approved)
   - Shipping time (order approved → handed to carrier)
   - Delivery time (handed to carrier → delivered to customer, diagnostic only)
   - Late shipping and late delivery flags

4. **Seller attribution & aggregation**
   - Orders attributed to a single seller to maintain one-row-per-order granularity
   - Seller-level KPIs calculated for volume, reliability, and delay contribution

5. **Impact vs reliability analysis**
   - Combined seller order volume and late shipment rates
   - Identified concentration of operational delays among high-impact sellers

All assumptions and transformations are documented separately.

---

## Key Operational Metrics

| Metric                 | Definition |
|------------------------|------------|
| Processing Time        | Order approved − order purchase timestamp |
| Shipping Time          | Order delivered to carrier − order approved |
| Late Shipping Rate     | % of orders with shipping time exceeding SLA proxy |
| Seller Order Volume    | Number of delivered orders per seller |
| Avg Shipping Time      | Mean shipping time per seller |
| Late Shipment Impact   | Late shipping rate × order volume |
| Underperformance Score | Peer-relative composite seller risk indicator |

---

## Key Findings

### 1. Late Shipments Are Highly Concentrated

- A **very small subset of sellers** drives a disproportionate share of late handovers to logistics.
- The **top ~0.4% of active sellers** account for approximately **25% of all late shipments**.
- These sellers are typically **high-volume**, meaning small inefficiencies scale into systemic delays.

**Operational takeaway**: Broad enforcement is inefficient; targeted intervention yields higher impact.

---

### 2. Low-Volume vs High-Volume Seller Dynamics

- Low-volume sellers exhibit **higher per-order late shipping rates**.
- However, their limited order volume results in **minimal aggregate operational impact**.
- High-volume sellers generate over **15× more late shipments per seller**, despite better average reliability.

**Operational takeaway**: Seller prioritization must consider **impact, not reliability alone**.

---

### 3. Shipping Delays Dominate Seller Underperformance

- Shipping time is the primary contributor to seller-driven delays.
- Slow order approvals are rare and operationally insignificant.
- Processing time and shipping time show **negligible correlation**, indicating independent failure modes.

**Operational takeaway**: Seller performance management should focus primarily on shipping SLAs.

---

### 4. Extreme Delays Are Rare but Critical

- Orders with extreme shipping delays are uncommon but heavily skewed toward a few sellers.
- These cases represent operational failures rather than normal variability.

**Operational takeaway**: Extreme delays should trigger immediate root-cause analysis and escalation.

---

## Operations Monitoring Framework

To translate analytical findings into operational use, the project defines a **monitoring and escalation framework** suitable for ongoing Ops review.

### Monitoring Objectives

- Track seller fulfillment performance over time
- Detect emerging SLA risks early
- Prioritize sellers based on operational impact
- Support structured escalation and intervention

### Core Monitoring Views

- Seller fulfillment KPI overview (processing & shipping)
- Seller impact vs reliability comparison
- High-risk seller watchlist

---

## Escalation & Action Logic (Conceptual)

| Trigger       | Condition                                | Action                         |
|---------------|------------------------------------------|--------------------------------|
| SLA Breach    | Late shipping rate above peer threshold  | Seller flagged for Ops review  |
| High Impact   | Top percentile sellers by late shipments | Prioritized intervention       |
| Extreme Delay | Shipping time exceeds extreme threshold  | Root-cause investigation       |
| Repeat Issues | Persistent SLA breaches                  | Escalation / governance action |

This structure mirrors real-world SLA governance and vendor performance management practices.

---

## Assumptions & Governance

Key assumptions include:

- Only **delivered orders** are included in SLA analysis
- Seller performance is evaluated using **shipping time**, not delivery time
- Delivery delays reflect logistics performance, not seller responsibility
- Multi-item orders are attributed to a single seller to preserve order-level granularity

Full details are documented in:

- `assumptions.md`
- `data_dictionary.md`

---

## Tools & Skills Demonstrated

- Python (Pandas, NumPy)
- SQL-style aggregations and KPI engineering
- Operational performance analysis
- SLA and vendor performance monitoring
- Business-oriented analytical documentation

---

## Project Structure

```
olist_ops_project_dap3
       ├── 01_data
       │   ├── 01_raw
       │   │   ├── olist_customers_dataset.csv
       │   │   ├── olist_geolocation_dataset.csv
       │   │   ├── olist_order_items_dataset.csv
       │   │   ├── olist_order_payments_dataset.csv
       │   │   ├── olist_order_reviews_dataset.csv
       │   │   ├── olist_orders_dataset.csv
       │   │   ├── olist_products_dataset.csv
       │   │   ├── olist_sellers_dataset.csv
       │   │   └── product_category_name_translation.csv
       │   ├── 02_interim
       │   │   ├── order_items.csv
       │   │   └── orders_kpi_clean.csv
       │   └── 03_curated
       │       ├── orders_enriched.csv
       │       └── seller_kpis.csv
       ├── 02_notebooks
       │   ├── 01_data_audit.ipynb
       │   ├── 02_cleaning.ipynb
       │   ├── 03_metric_calculation.ipynb
       │   ├── 04_seller_delay_diagnostics.ipynb
       │   ├── 04_visualization.ipynb
       │   └── 05_visualization.ipynb
       ├── 03_src
       │   ├── __pycache__
       │   │   └── utils.cpython-313.pyc
       │   └── utils.py
       ├── 04_visuals
       ├── 05_outputs
       │   └── Notebooks
       └── 06_docs
           ├── Database Schema.png
           ├── Findings and Recommendations.md
           ├── README.md
           ├── assumptions.md
           ├── data_dictionary.md
           └── project_blueprint.md


---

## Summary

This project demonstrates how operational data from a real e-commerce marketplace can be transformed into **actionable, operations-ready insights**. By isolating seller-controlled fulfillment stages and prioritizing impact over averages, the analysis mirrors how marketplace operations teams manage SLA risk and vendor performance at scale.
