# Workforce Analytics Data Dictionary

## Dataset Overview

This dataset represents outsourced workforce records used for workforce analytics, vendor performance management, Saudization tracking, SLA compliance, and attrition risk monitoring.  
Each row represents a **single worker record** sourced from an external vendor.

**Grain:** One record per worker  
**Primary Use Cases:**  

- Vendor performance benchmarking  
- SLA compliance analysis  
- Attrition risk modeling  
- Saudization reporting  
- Workforce cost optimization  

---

## Field Definitions

### Employee_ID

- **Type:** Integer  
- **Nullable:** No  
- **Description:** Unique identifier for each worker record.  
- **Notes:** Generated per worker; not reusable across records.

---

### Vendor

- **Type:** String  
- **Nullable:** No  
- **Description:** Outsourcing vendor responsible for supplying the worker.  
- **Allowed Values:**  
  - Al-Rajhi Cleaning  
  - Saudi Hospitality Staffing  
  - Jazan Construction Labor  
  - Riyadh Logistics Crew  
  - Tabuk Facility Services  
- **Analytics Use:** Vendor performance, SLA compliance, cost comparison.

---

### Role

- **Type:** String  
- **Nullable:** No  
- **Description:** Functional role assigned to the worker.  
- **Allowed Values:**  
  - Cleaner  
  - Security Guard  
  - Construction Worker  
  - Driver  
  - Housekeeper  
  - Warehouse Staff  
- **Analytics Use:** Role-based productivity, staffing mix optimization.

---

### Contract_Type

- **Type:** String  
- **Nullable:** No  
- **Description:** Employment engagement model between vendor and worker.  
- **Allowed Values:**  
  - Full-Time  
  - Part-Time  
  - Project-Based  
- **Analytics Use:** Attrition modeling, cost structure analysis.

---

### Saudization_Status

- **Type:** String  
- **Nullable:** No  
- **Description:** Indicates whether the worker is a Saudi national or expatriate.  
- **Allowed Values:**  
  - Saudi  
  - Expat  
- **Analytics Use:** Regulatory reporting, Saudization ratio tracking.

---

### Performance_Score

- **Type:** Integer  
- **Nullable:** No  
- **Range:** 0–100  
- **Description:** Composite performance score derived from operational and supervisory assessments.  
- **Analytics Use:** Performance benchmarking, vendor scorecards.

---

### SLA_Met

- **Type:** Boolean  
- **Nullable:** No  
- **Description:** Indicates whether the worker met the defined Service Level Agreement for the evaluation period.  
- **Values:**  
  - TRUE – SLA met  
  - FALSE – SLA not met  
- **Analytics Use:** SLA compliance tracking, vendor governance.

---

### Attrition_Risk

- **Type:** String  
- **Nullable:** No  
- **Description:** Predicted likelihood of worker attrition within the near term.  
- **Allowed Values:**  
  - Low  
  - Medium  
  - High  
- **Analytics Use:** Workforce stability forecasting, retention planning.

---

### Tenure_Months

- **Type:** Integer  
- **Nullable:** No  
- **Range:** 1–36  
- **Description:** Length of time the worker has been engaged, measured in months.  
- **Analytics Use:** Attrition correlation, experience analysis.

---

### Absenteeism_Days

- **Type:** Integer  
- **Nullable:** No  
- **Range:** 0–15  
- **Description:** Number of recorded absenteeism days within the reporting period.  
- **Analytics Use:** Productivity analysis, risk indicators.

---

### Hourly_Rate_SAR

- **Type:** Integer  
- **Nullable:** No  
- **Unit:** Saudi Riyal (SAR)  
- **Description:** Hourly billing rate charged by the vendor for the worker.  
- **Analytics Use:** Cost optimization, vendor rate benchmarking.
