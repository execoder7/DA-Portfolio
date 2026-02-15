# 📊 Workforce SLA & Attrition Analytics Dashboard

[![PowerBI](https://img.shields.io/badge/Power-BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

> An interactive Power BI dashboard designed to monitor workforce performance, SLA compliance, and attrition risks for outsourced staffing operations. Built to support data-driven decision-making in alignment with Saudi Vision 2030 localization goals.

---

## Table of Contents

- [Overview](#overview)
- [Business Problem](#business-problem)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Data Source](#data-source)
- [Dashboard Preview](#dashboard-preview)
- [Key Insights](#key-insights)
- [File Structure](#file-structure)
- [Usage Guide](#usage-guide)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

This project is an operational intelligence dashboard that analyzes workforce data for outsourcing companies operating in Saudi Arabia. It tracks **1,000+ employees** across Cleaning, Construction, Hospitality, and Logistics sectors, providing actionable insights on:

- SLA Compliance & Performance Metrics
- Attrition Risk by Role & Contract Type
- Vendor/Subcontractor Performance
- Saudization Impact on Operational Quality

The dashboard is designed to help Operations Managers and Business Partners reduce SLA penalties, optimize vendor management, and improve workforce retention strategies.

---

## Business Problem

Outsourcing companies in KSA face critical operational challenges:

| Challenge | Impact |
|-----------|--------|
| High Attrition Rates | Constant re-recruiting costs & training overhead |
| SLA Breaches | Financial penalties & client churn risk |
| Vendor Inconsistency | Unreliable subcontractor performance |
| Saudization Pressure | Need to prove Saudi talent quality matches expats |

This dashboard addresses these challenges by transforming raw workforce data into **actionable operational intelligence**.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Real-Time KPI Tracking** | Monitor Total Employees, SLA Met %, Avg Performance, Attrition Rate |
| **Vendor Performance Analysis** | Compare SLA compliance across subcontractors/vendors |
| **Attrition Risk Modeling** | Identify high-risk roles (Construction, Waiter) using color-coded risk levels |
| **Saudization Analytics** | Compare Saudi vs. Expat performance scores to validate localization quality |
| **Contract Type Insights** | Analyze absenteeism and performance by Full-Time, Part-Time, Project-Based |
| **Tenure vs Performance** | Scatter plot analysis to understand if experience correlates with quality |
| **Interactive Filters** | Slice data by Contract Type, Sector, Vendor, and Location |

---

## Tech Stack

| Category | Tools |
|----------|-------|
| **Data Generation** | Python 3.10+, Pandas, Faker |
| **Data Processing** | Excel |
| **Visualization** |  Power BI  |

---

## Data Source

This project uses a **synthetic dataset** generated to simulate real-world outsourcing operations in Saudi Arabia.

| Attribute | Details |
|-----------|---------|
| **Records** | 1,000+ employee shift logs |
| **Sectors** | Cleaning, Construction, Hospitality, Logistics |
| **Locations** | Riyadh, Jeddah, Dammam, NEOM, Red Sea Project |
| **Timeframe** | 90 days of operational data |
| **Variables** | Attendance, Performance Score, SLA Compliance, Attrition Risk, Tenure, Contract Type, Saudization Status |

> *No real employee data was used. All data is artificially generated for demonstration and portfolio purposes.*

---

## Dashboard Preview

![Dashboard Preview](3.%20Outsourced%20Workforce%20SLA/05_outputs/Workforce%20Overview%20Dashbboard.jpeg)

*Figure 1: Workforce Overview Dashboard showing KPIs, Vendor SLA Compliance, Attrition Risk by Role, and Performance by Tenure.*

---

## Key Insights

| Insight | Business Impact |
|---------|-----------------|
| **19% SLA Breach Rate** | ~190 shifts daily at risk of penalty clauses; requires immediate vendor intervention |
| **Construction Has Highest Attrition** | Harsh site conditions (NEOM/Red Sea) driving turnover; needs retention bonuses |
| **Part-Time = Highest Absenteeism** | Unreliable for critical SLA sites; recommend reallocating to on-call roles |
| **Saudi Performance = Expat Performance** | Saudi employees scored 73 vs Expat 72; validates high-quality Saudization for client proposals |
| **No Tenure-Performance Correlation** | New hires perform as well as veterans; focus should be on retention, not just training |

---

## File Structure

```
3. Outsourced Workforce SLA/
│
├── 01_data
│   ├── 01_raw
│   │   ├── synthetic_data_gen.py
│   │   ├── workforce_data.xlsx
│   ├── 02_interim
│   ├── 03_curated
├── 02_notebooks
│   ├── dataset_analysis.ipynb
├── 03_src
├── 04_visuals
│   ├── Attrition Risk by Role.png
│   ├── Cost per Performance.png
│   ├── Performance Score by Saudization.png
│   ├── Performance vs Tenure (Colored by Attrition Risk).png
│   ├── SLA Compliance by Vendor.png
├── 05_outputs
│   ├── Outsourced_Workforce_Dashboard.pbix
│   ├── Workforce Overview Dashbboard.jpeg
├── 06_docs
│   ├── assumptions.txt
│   ├── data_dictionary.md
│   ├── project_blueprint.md
```

---

## Usage Guide

### For Operations Managers

1. **Monitor Daily KPIs:** Check the top banner for SLA Met % and Attrition Rate.
2. **Identify Problem Vendors:** Use the "SLA Compliance by Vendor" chart to flag underperformers.
3. **Target High-Risk Roles:** Review "Attrition Risk by Role" to prioritize retention efforts for Construction/Waiter staff.
4. **Validate Saudization:** Use the "Performance by Saudization Status" chart in client proposals to prove Saudi talent quality.

### For Data Analysts

1. **Refresh Data:** Update `generate_data.py` with new parameters and re-run.
2. **Modify DAX Measures:** Edit measures in Power BI's "Modeling" tab.
3. **Add New Visuals:** Drag fields from the "Data" pane to create custom charts.

---

## Future Enhancements

| Enhancement | Priority | Description |
|-------------|----------|-------------|
| Predictive Attrition Model | High | Use ML (Scikit-learn) to predict which employees will quit next month |
| Mobile-Optimized Layout | Medium | Create a phone-friendly Power BI layout for field supervisors |
| Automated Email Alerts | Medium | Use Power Automate to email managers when SLA drops below 80% |
| Geographic Heat Map | Low | Visualize performance by city/region on a Saudi Arabia map |
| Live API Integration | Low | Connect to real HRIS systems (SAP, Oracle) instead of synthetic data |

---

## License

This project is open-source and available under the [MIT License](LICENSE).

```
Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

</div>
