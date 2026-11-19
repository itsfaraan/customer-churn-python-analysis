import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("telco_customer_churn_cleaned.csv")
tenure_avg = df.groupby("Churn")["tenure"].mean()

print("Average Tenure by Churn:")
print(tenure_avg.round(2))

tenure_avg.plot(kind="bar", color=["steelblue", "salmon"])
plt.title("Average Customer Tenure by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Tenure (Months)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("tenure_churn.png", dpi=300)
plt.close()
print("Chart saved successfully!")
