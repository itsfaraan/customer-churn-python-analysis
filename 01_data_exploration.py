import pandas as pd

df = pd.read_csv("telco_customer_churn.csv")

print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumn information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())
print("\nBlank TotalCharges values:")
print((df["TotalCharges"].str.strip() == "").sum())
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

print("\nMissing TotalCharges after conversion:")
print(df["TotalCharges"].isna().sum())
print("\nCustomers with missing TotalCharges:")
print(
    df.loc[
        df["TotalCharges"].isna(),
        ["customerID", "tenure", "MonthlyCharges", "Churn"]
    ]
)
df = df.dropna(subset=["TotalCharges"]).copy()

print("\nDataset shape after cleaning:")
print(df.shape)
df.to_csv("telco_customer_churn_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")