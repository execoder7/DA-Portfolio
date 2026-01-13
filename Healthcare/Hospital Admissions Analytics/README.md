# Healthcare Cost & Utilization Analysis (EDA Project)

## Project Overview
This project performs an Exploratory Data Analysis (EDA) on a healthcare dataset to understand the key drivers of hospital billing amounts, length of stay, and admission patterns. The analysis bridges data insights → modeling implications → business actions, making it suitable for both technical and executive audiences.

## Objectives
- Identify key cost drivers in hospital billing
- Analyze length of stay (LOS) patterns and their impact on cost
- Segment patients by admission type, age group, department, and insurance
- Detect outliers, skewness, and imbalance relevant for modeling
- Translate EDA findings into actionable business and modeling recommendations

## Repository Structure
```powershell
📁 Healthcare/Hospital Admissions Analytics
│
├── 📓 Data cleaning.ipynb            # Main cleaning notebook
├── 📓 Healthcare Dataset EDA.ipynb   # Main EDA notebook
├── 📄 README.md                      # Project documentation
└── 📁 data/                          # Raw / cleaned datasets
```

## Key Analyses Performed
1. **Data Understanding & Cleaning**
   - Missing value analysis
   - Data type validation
   - Outlier inspection (billing & LOS)

2. **Univariate Analysis**
   - Distribution of Billing Amount, Length of Stay, Age
   - Skewness and heavy-tail behavior

3. **Bivariate Analysis**
   - Billing vs Length of Stay
   - Billing by Admission Type
   - Billing across Departments & Insurance Types

4. **Multivariate Analysis**
   - Combined impact of LOS, Age, Admission Type
   - Department-wise cost variance

5. **Temporal Analysis**
   - Monthly and weekday admission trends
   - Seasonal effects on hospital load

## Key Insights
- Length of Stay (LOS) is the strongest driver of billing amount
- Emergency admissions consistently incur higher costs
- Certain departments exhibit structurally higher billing
- Elderly patients (60+) have longer stays and higher costs
- Billing data is highly right-skewed with significant outliers
- Seasonality impacts admission volume and capacity needs

## Insight → Modeling → Business Translation

| Insight | Modeling Implication | Business Action |
|---------|---------------------|-----------------|
| LOS drives cost | LOS buckets, log features | Early discharge planning |
| Emergency admissions cost more | Admission type encoding | ER triage optimization |
| Skewed billing | Log-transform target | Focus on high-cost cases |
| Department variance | Target / one-hot encoding | Department KPIs |
| Class imbalance | SMOTE / weighting | Capacity forecasting |

## Recommended Models (Next Steps)
- **Regression**: Gradient Boosting, Random Forest, XGBoost
- **Classification**: High-cost patient flagging with imbalance handling
- **Forecasting**: Admission volume using time features

## Tools & Libraries
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook

## Business Value
- Enables data-driven hospital cost control
- Supports operational efficiency & staffing optimization
- Lays groundwork for predictive healthcare analytics
- Bridges technical analysis with executive decision-making

## How to Run
1. Clone the repository
2. Install required libraries: `pip install pandas numpy matplotlib seaborn`
3. Open `Healthcare Dataset EDA.ipynb`
4. Run cells sequentially

## License
This project is for educational and analytical purposes.



