# Findings & Recommendations – Olist E-Commerce Operations

## 1. Key Findings

### 1.1 Late Shipments Concentration

- Top 0.4% of active sellers account for ~25% of late handovers to logistics, confirming operational delays are concentrated among a very small subset of high-impact sellers.
- These sellers are typically high-volume, generating over 15× more late shipments per seller than low-volume sellers despite better reliability.
- **Operational takeaway**: systemic delivery delays are driven by a few critical sellers rather than widespread underperformance.

### 1.2 Low-Volume Seller Performance

- Sellers with ≤7 orders over the analysis period have a higher per-order late shipping rate: 8.6% vs 5.7% for higher-volume sellers.
- Average orders per low-volume seller: ~2.85 → expected <0.3 late shipments per seller, minimal total operational impact.
- **Operational takeaway**: low-volume sellers show lower reliability, but their small scale limits overall impact.

### 1.3 Shipping vs Processing

- Shipping time is the dominant contributor to seller underperformance; processing time delays are rare (slow_processing_rate ≈ 0.03%).
- Correlation between processing and shipping times is negligible (-0.01), indicating shipping delays are largely independent of order approval speed.

### 1.4 Extreme Delays

- Orders with shipping_time >7 days are uncommon (~5% of total orders) but heavily skewed toward a small set of sellers.
- High-volume sellers drive the majority of these extreme delays, reinforcing the need to focus on critical operational nodes.

## 2. Impact vs Reliability Insights

| Quadrant | Insight | Suggested Action |
| ---------- | --------- | ------------------ |
| **High Impact / Low Reliability** | Critical, high-volume sellers causing systemic delays | Immediate operational intervention; enforce SLAs; seller coaching |
| **High Impact / High Reliability** | High-volume, generally reliable sellers | Process optimization; monitor for small inefficiencies |
| **Low Impact / Low Reliability** | Low-volume, inconsistent sellers | Governance or activation control; optional monitoring |
| **Low Impact / High Reliability** | Long-tail sellers with good operational performance | No action required; maintain incentives for continued reliability |

## 3. Recommendations

### Targeted Seller Interventions

- Focus efforts on top 1–2% of high-volume, high-impact sellers responsible for the majority of late shipments.
- **Actions**: SLA enforcement, operational coaching, and workflow audits.

### Low-Volume Seller Governance

- Maintain monitoring of low-volume sellers for reliability trends but prioritize resources on high-impact sellers.
- Consider onboarding guidance or early warning alerts for sellers repeatedly late.

### Shipping Time SLAs

- Reinforce shipping time as primary operational KPI for seller performance.
- Ensure logistics partners' delivery times remain separate from seller performance scoring.

### Data-Driven Continuous Monitoring

- Establish a rolling Impact vs Reliability dashboard to track seller performance over time.
- Highlight emerging high-impact sellers before they contribute disproportionately to delays.

### Operational Escalation Policy

- Sellers in High Impact / Low Reliability quadrant trigger automated escalations for Ops team review.
- Align incentives and penalties to drive improvement in the most critical nodes.

## Summary

- Operational delays are highly concentrated among a very small set of high-volume sellers, confirming the original hypothesis.
- Low-volume sellers exhibit worse per-order reliability but contribute minimally to overall operational impact.
- Strategic focus should be on critical, high-volume sellers, leveraging the Impact vs Reliability framework to guide interventions and resource allocation.
