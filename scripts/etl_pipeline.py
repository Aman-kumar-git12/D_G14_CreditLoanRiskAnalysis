# ==============================
# 1. IMPORTS
# ==============================
import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)


# ==============================
# 2. LOAD DATA
# ==============================
def load_data(path):
    return pd.read_csv(path)


# ==============================
# 3. CLEAN DATA
# ==============================
def clean_data(df):
    # Drop rows without Loan ID
    df = df.dropna(subset=['Loan ID'])

    # Drop redundant column
    if 'Months since last delinquent' in df.columns:
        df = df.drop('Months since last delinquent', axis=1)

    # Convert to numeric
    df['Current Loan Amount'] = pd.to_numeric(df['Current Loan Amount'], errors='coerce')

    # Handle sentinel values safely
    valid_loans = df['Current Loan Amount'].replace(99999999, pd.NA)
    loan_upper_limit = valid_loans.quantile(0.99)
    df['Current Loan Amount'] = valid_loans.fillna(loan_upper_limit)

    # Missing value imputation
    df['Credit Score'] = df['Credit Score'].fillna(df['Credit Score'].median())
    df['Annual Income'] = df['Annual Income'].fillna(df['Annual Income'].median())
    df['Years in current job'] = df['Years in current job'].fillna(df['Years in current job'].mode()[0])
    df['Bankruptcies'] = df['Bankruptcies'].fillna(df['Bankruptcies'].mode()[0])
    df['Tax Liens'] = df['Tax Liens'].fillna(df['Tax Liens'].mode()[0])

    # Outlier clipping
    debt_upper_limit = df['Monthly Debt'].quantile(0.99)
    df['Monthly Debt'] = df['Monthly Debt'].clip(upper=debt_upper_limit)

    # Fix credit score anomalies
    df.loc[df['Credit Score'] > 850, 'Credit Score'] /= 10

    return df


# ==============================
# 4. FEATURE ENGINEERING
# ==============================
def feature_engineering(df):

    # DTI Ratio
    df['DTI'] = df['Monthly Debt'] / (df['Annual Income'] / 12)
    df['DTI'] = df['DTI'].replace([np.inf, -np.inf], np.nan)
    df['DTI'] = df['DTI'].fillna(df['DTI'].median())

    # Risk Score
    df['Risk Score'] = (
        (df['Number of Credit Problems'] > 0).astype(int) +
        (df['Bankruptcies'] > 0).astype(int) +
        (df['Tax Liens'] > 0).astype(int)
    )

    # Risk Category
    def risk_category(score):
        if score == 0:
            return 'Low Risk'
        elif score == 1:
            return 'Medium Risk'
        else:
            return 'High Risk'

    df['Risk Category'] = df['Risk Score'].apply(risk_category)

    return df


# ==============================
# 5. SAVE DATA
# ==============================
def save_data(df, path):

    # Save main dataset
    df.to_csv(path, index=False)

    # Risk Summary Table
    risk_summary = df.groupby('Risk Category').agg({
        'Current Loan Amount': 'mean',
        'Annual Income': 'mean',
        'DTI': 'mean',
        'Risk Score': 'count'
    }).rename(columns={'Risk Score': 'Applicant Count'}).reset_index()

    risk_summary.to_csv('data/processed/risk_summary.csv', index=False)

    # Risk by Home Ownership
    risk_by_home = df.groupby('Home Ownership')['Risk Score'].mean().reset_index(name='avg_risk')

    risk_by_home.to_csv('data/processed/risk_by_home.csv', index=False)


# ==============================
# 6. MAIN PIPELINE
# ==============================
def run_pipeline():

    df = load_data('data/raw/loan_data.csv')
    df = clean_data(df)
    df = feature_engineering(df)
    save_data(df, 'data/processed/final_loan_risk_processed.csv')

    print("ETL Pipeline executed successfully!")


# ==============================
# 7. EXECUTE
# ==============================
if __name__ == "__main__":
    run_pipeline()