import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("telco_customer_churn_cleaned.csv")
rates = df.groupby("PaymentMethod")["Churn"].apply(lambda x: (x == "Yes").mean() * 100)
rates = rates.sort_values(ascending=False)

print("Churn Rate by Payment Method (%):")
print(rates.round(2))

rates.sort_values().plot(kind="barh", color="steelblue")
plt.title("Churn Rate by Payment Method")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Payment Method")
plt.tight_layout()
plt.savefig("payment_method_churn.png", dpi=300)
plt.close()
print("Chart saved successfully!")
