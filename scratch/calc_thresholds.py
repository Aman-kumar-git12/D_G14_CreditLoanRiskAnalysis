import pandas as pd
df = pd.read_csv('data/processed/cleaned_loan_data.csv')

# Use 99th percentile for clipping high-end outliers to preserve as much data as possible for the dashboard
loan_cap = df[df['Current Loan Amount'] < 99999999]['Current Loan Amount'].quantile(0.99)
debt_cap = df['Monthly Debt'].quantile(0.99)

print(f"Loan Cap (99th percentile excl. sentinel): {loan_cap}")
print(f"Monthly Debt Cap (99th percentile): {debt_cap}")
print(f"Current Max Loan: {df['Current Loan Amount'].max()}")
print(f"Current Max Debt: {df['Monthly Debt'].max()}")
