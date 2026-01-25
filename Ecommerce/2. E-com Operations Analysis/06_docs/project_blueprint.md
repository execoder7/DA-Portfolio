# Project Blueprint: Seller Fulfillment Operations Performance Analysis

## Project Title

Seller Fulfillment Performance & SLA Impact Analysis
*(Brazilian E-Commerce Public Dataset by Olist)*

---

## Objective

Analyze **seller-controlled fulfillment performance** within a multi-seller e-commerce marketplace to identify operational bottlenecks, SLA breaches, and high-impact sellers, using multi-table order lifecycle data.

The goal is to support **actionable operational decision-making**, not exploratory analytics.

---

## Audience / Use Case

* **Portfolio project**: Demonstrate Operations & Business Analytics skills
* **Stakeholder simulation**: Marketplace Operations / Vendor Performance Manager

---

## Explicit Scope Definition

### In Scope

* Seller-controlled fulfillment stages
* Order processing and shipping performance
* SLA breach identification
* Seller-level KPI benchmarking
* Impact-based prioritization and escalation logic

### Out of Scope

* Revenue or pricing optimization
* Customer behavior or segmentation
* Product category performance
* Distance-based or logistics carrier analysis
* Predictive or ML-based modeling

---

## Non-Goals

* End-to-end commercial optimization
* Logistics carrier performance evaluation
* Last-mile delivery route efficiency

---

## Step 1: Define Key Operational Questions

### High-Level Goal

Improve fulfillment SLA performance by focusing on **seller-controlled operational levers**.

### Final, Scoped Operational Questions

1. **Which seller-controlled stages of the order fulfillment process contribute most to SLA breaches?**

2. **How does fulfillment performance vary across sellers when evaluated relative to operational peers?**

3. **Which sellers disproportionately contribute to late shipments, and how concentrated is their operational impact?**

4. **How can sellers be operationally segmented (healthy, watchlist, underperforming) to support targeted intervention?**

5. **What monitoring and escalation framework would allow operations teams to reduce late shipments with minimal effort and maximum impact?**

> *Note: Logistics-driven factors (e.g., distance, carrier performance, last-mile delivery) are intentionally excluded to preserve clear ownership and actionability.*

---

## Step 2: Corresponding KPIs & Metrics

> Metrics are intentionally limited to those directly computed and used in the analysis.

| KPI                           | Definition                                                      |
| ----------------------------- | --------------------------------------------------------------- |
| Processing Time               | Order approved − order purchase timestamp (days)                |
| Shipping Time                 | Order delivered to carrier − order approved (days)              |
| Delivery Time                 | Order delivered to customer − order delivered to carrier (days) |
| Late Shipping Rate            | % of orders with shipping time exceeding SLA proxy              |
| Late Delivery Flag            | Delivery occurred after estimated delivery date                 |
| Seller Order Volume           | Number of delivered orders per seller                           |
| Avg Shipping Time (Seller)    | Mean shipping time per seller                                   |
| Seller Underperformance Score | Composite peer-relative performance indicator                   |
| Late Shipment Impact          | Late shipping rate × order volume                               |

### Explicitly Excluded Metrics

* Order cycle time (end-to-end)
* Distance-adjusted delivery time
* Product category KPIs
* Revenue-weighted SLA metrics

These exclusions are intentional and aligned with the project’s operational focus.

---

## Step 3: Analytical Logic (Summary)

* Filter to delivered orders with complete lifecycle timestamps
* Engineer fulfillment KPIs at the order level
* Attribute each order to a single seller
* Aggregate KPIs at the seller level
* Benchmark sellers relative to peers
* Quantify impact concentration using cumulative contribution analysis
* Translate insights into monitoring and escalation logic

---

## Step 4: Intended Outcome

Produce an **operations-ready performance framework** that enables:

* Identification of high-risk sellers
* Prioritization based on operational impact, not averages
* Scalable monitoring of fulfillment SLAs
* Clear escalation paths for underperforming sellers

---

## Summary

This project intentionally prioritizes **depth, actionability, and ownership clarity** over exhaustive exploration. By isolating seller-controlled fulfillment stages, the analysis supports realistic operational decision-making and mirrors how marketplace Ops teams manage SLA performance in practice.
