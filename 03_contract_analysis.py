import pandas as pd

df = pd.read_csv("telco_customer_churn_cleaned.csv")

contract_churn = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("Churn Rate by Contract Type:")
print(contract_churn.round(2))
import matplotlib.pyplot as plt
contract_churn.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("contract_churn.png", dpi=300)
