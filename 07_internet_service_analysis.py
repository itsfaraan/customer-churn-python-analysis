import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("telco_customer_churn_cleaned.csv")
rates = df.groupby("InternetService")["Churn"].apply(lambda x: (x == "Yes").mean() * 100)
rates = rates.sort_values(ascending=False)

print("Churn Rate by Internet Service (%):")
print(rates.round(2))

rates.sort_values().plot(kind="barh", color="steelblue")
plt.title("Churn Rate by Internet Service")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Internet Service")
plt.tight_layout()
plt.savefig("internet_service_churn.png", dpi=300)
plt.close()
print("Chart saved successfully!")
