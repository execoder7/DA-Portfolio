# E-Commerce Order Fulfillment & Delivery Operations Analysis  
**Dataset:** Olist Brazilian E-Commerce Public Dataset  
**Prepared by:** Operations Analyst  
**Date:** January 22, 2026

---

## 1. Executive Summary
This analysis evaluates seller-controlled fulfillment operations across the Olist marketplace, pinpointing critical bottlenecks and SLA compliance issues. Shipping delays represent the primary seller-driven failure mode, while processing times remain negligible.

**Key Operational Insights:**

- Late shipment concentration: Top 5 sellers (~0.4% of total) drive 25% of all late shipments.
- Volume-impact disconnect: High-volume sellers create systemic delays despite reasonable per-order reliability.
- Regional delivery variance: Northeast states average 12–20 days vs. Southeast states averaging 8–12 days.
- Extreme delays (>30 days): Rare (~1% of orders) but concentrated among a few sellers.

**Primary Recommendation:**  
Prioritize interventions by **impact score** (order volume × late rate) rather than late rate alone. Implement seller dashboards, targeted account management, and regional logistics optimization.

![Figure 1: Boxplot – Order Lifecycle Times (Processing, Shipping, Delivery)](PLACEHOLDER_FOR_IMAGE)

---

## 2. Dataset & Methodology

- **Source:** Olist Brazilian E-Commerce Public Dataset (Kaggle)  
- **Scope:** 95K+ delivered orders with complete lifecycle timestamps  
- **Timeframe:** 2016–2018 historical data  
- **Focus:** Seller processing → shipping handoff  
- **Exclusions:** Canceled orders, incomplete timestamps  

**Analytical Rigor:**

- Verified referential integrity across 9 core tables  
- Engineered 7 operational KPIs with clear business definitions  
- Applied impact-weighting methodology for seller prioritization  

---

## 3. Core Operational Metrics

- **Processing Time:** order_approved − order_purchase → Median: 0.2 days, P75: 0.3 days (Seller)  
- **Shipping Time:** delivered_carrier − order_approved → Median: 1.7 days, P75: 3.1 days (Seller)  
- **Delivery Time:** order_delivered − delivered_carrier → Median: 7.5 days, P75: 10 days (Logistics)  
- **Late Shipping Rate:** Shipping time > 7 days → 7.2% (Seller)  
- **Extreme Shipping:** Shipping time > 30 days → 2.0% (Seller)  
- **Impact Score:** late_rate × order_volume → Top 5 = 25% total impact (Seller)  

![Figure 2: Histogram – Seller Late Shipping Rate Distribution](PLACEHOLDER_FOR_IMAGE)

---

## 4. Key Findings

### 4.1 Fulfillment Stage Breakdown

- Processing: 0.2 days median → negligible  
- Shipping: 1.7 days median → 85% of seller-attributable delays **← PRIMARY BOTTLENECK**  
- Delivery: 7.5 days median → logistics-controlled  

**Interpretation:** Boxplots reveal shipping time as the dominant seller-controlled failure mode.  

![Figure 3: Boxplot – Order Lifecycle Times Highlighting Shipping](PLACEHOLDER_FOR_IMAGE)

---

### 4.2 Late Shipment Pareto Analysis

- Top 5 sellers → 25% of late shipments  
- Top 20 sellers → 47% cumulative  
- Bottom 90% → 28% cumulative  

**Insight:** Shipping delays follow the 80/20 rule. Targeting the top 1% of sellers can reduce ~50% of late shipments.  

![Figure 4: Pareto Chart – Cumulative Late Shipments by Seller](PLACEHOLDER_FOR_IMAGE)

---

### 4.3 High-Volume Seller Risk Matrix

- **High Volume & High Late Rate:** HIGH IMPACT ← PRIORITY  
- **High Volume & Low Late Rate:** Moderate impact  
- **Low Volume & High Late Rate:** Moderate impact  
- **Low Volume & Low Late Rate:** Low impact  

**Insight:** Prioritize high-volume, high-late sellers as they drive systemic operational delays.  

![Figure 5: Bubble Plot – Seller Order Volume vs Late Shipping Rate](PLACEHOLDER_FOR_IMAGE)

---

### 4.4 Regional Delivery Heatmap Summary

- **SP (São Paulo):** Avg Delivery 6.1 days, Late Rate 14.2%  
- **RJ:** Avg Delivery 8.4 days, Late Rate 21.3%  
- **BA (Bahia):** Avg Delivery 13.7 days, Late Rate 31.4%  
- **CE:** Avg Delivery 15.2 days, Late Rate 36.8%  

**Insight:** Regional disparities suggest need for targeted logistics interventions.  

![Figure 6: Heatmap – Avg Delivery Time by State](PLACEHOLDER_FOR_IMAGE)  
![Figure 7: Bar Chart – Late Delivery Rate by State](PLACEHOLDER_FOR_IMAGE)

---

## 5. Operational Recommendations

**Priority 1: Seller Intervention Framework**  
**Immediate (Next 30 days):**

- Top 5 impact sellers → Dedicated account management  
- Extreme delay outliers → Root cause investigation  
- Shipping SLA < 20% → Performance improvement plan  

**Monitor (Ongoing):**

- Dashboard: Real-time impact scores  
- Weekly seller ranking reports  
- Monthly regional performance reviews  

**Priority 2: Regional Logistics**

- Target States: BA, CE, PE  
- Additional carrier capacity  
- Regional distribution center evaluation  
- Seller clustering by destination  

**Priority 3: Monitoring Infrastructure**

- Daily Dashboard Metrics:  
  - Seller impact ranking (top 20)  
  - Regional delivery SLA  
  - Extreme delay alerts (>30 days)  
  - 7-day performance trends  

---

## 6. Measured Operational Leverage

- **Top 5 sellers:** 2,020 orders impacted (23% of all
