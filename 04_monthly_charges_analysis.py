import pandas as pd

df = pd.read_csv("telco_customer_churn_cleaned.csv")

monthly_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("Average Monthly Charges by Churn:")
print(monthly_charges.round(2))

import matplotlib.pyplot as plt

monthly_charges.plot(kind="bar", color=["steelblue", "salmon"])
plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("monthly_charges_churn.png", dpi=300)
plt.close()
print("Chart saved successfully!")
