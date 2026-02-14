import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Define realistic parameters
vendors = ["Al-Rajhi Cleaning", "Saudi Hospitality Staffing", "Jazan Construction Labor", "Riyadh Logistics Crew", "Tabuk Facility Services"]
roles = ["Cleaner", "Security Guard", "Construction Worker", "Driver", "Housekeeper", "Warehouse Staff"]
contract_types = ["Full-Time", "Part-Time", "Project-Based"]
saudization_status = ["Saudi", "Expat"]
attrition_risk_levels = ["Low", "Medium", "High"]

# Generate 1,000 records
data = []
for _ in range(1000):
    vendor = random.choice(vendors)
    role = random.choice(roles)
    contract = random.choice(contract_types)
    saudization = random.choice(saudization_status)

    # Performance and SLA logic
    if vendor in ["Al-Rajhi Cleaning", "Tabuk Facility Services"]:  # Assume these vendors are better
        performance_score = random.randint(70, 100)
        sla_met = random.choices([True, False], weights=[0.9, 0.1])[0]  # 90% SLA compliance
    else:
        performance_score = random.randint(40, 90)
        sla_met = random.choices([True, False], weights=[0.75, 0.25])[0]  # 75% SLA compliance

    # Attrition risk logic (higher for part-time and expats)
    if contract == "Part-Time" or saudization == "Expat":
        attrition_risk = random.choices(attrition_risk_levels, weights=[0.3, 0.5, 0.2])[0]  # Higher risk
    else:
        attrition_risk = random.choices(attrition_risk_levels, weights=[0.6, 0.3, 0.1])[0]  # Lower risk

    data.append({
        "Employee_ID": fake.unique.random_number(),
        "Vendor": vendor,
        "Role": role,
        "Contract_Type": contract,
        "Saudization_Status": saudization,
        "Performance_Score": performance_score,
        "SLA_Met": sla_met,
        "Attrition_Risk": attrition_risk,
        "Tenure_Months": random.randint(1, 36),
        "Absenteeism_Days": random.randint(0, 15),
        "Hourly_Rate_SAR": random.randint(15, 40),  # Typical rates for outsourced roles in KSA
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_excel("workforce_data.xlsx", index=False)
print("Dataset generated successfully!")