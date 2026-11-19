import pandas as pd

df = pd.read_csv("telco_customer_churn_cleaned.csv")

print("Customer Churn Distribution:")
print(df["Churn"].value_counts())

churn_rate = (df["Churn"] == "Yes").mean() * 100

print(f"\nChurn Rate: {churn_rate:.2f}%")
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(data=df, x="Churn")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.savefig("churn_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
