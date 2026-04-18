# 📄 Data Dictionary

## 📌 Overview
This document describes all variables used in the project, including original dataset columns and engineered features created during preprocessing.

---

## 📊 Original Features

| Column Name                  | Type        | Description |
|-----------------------------|------------|------------|
| Current Loan Amount         | Numeric     | Total loan amount requested by the borrower |
| Annual Income               | Numeric     | Borrower's yearly income |
| Monthly Debt                | Numeric     | Monthly debt obligations |
| Credit Score                | Numeric     | Creditworthiness score (expected range: 300–850) |
| Years of Credit History     | Numeric     | Number of years the borrower has had credit |
| Number of Credit Problems   | Numeric     | Count of credit-related issues |
| Bankruptcies                | Numeric     | Number of bankruptcies recorded |
| Tax Liens                   | Numeric     | Number of tax liens on record |
| Home Ownership              | Categorical | Type of home ownership (Rent, Own, Mortgage, etc.) |
| Years in current job        | Categorical | Employment duration category |
| Purpose                     | Categorical | Purpose of the loan (debt consolidation, home improvement, etc.) |

---

## 🧠 Engineered Features

| Column Name        | Type        | Description |
|-------------------|------------|------------|
| DTI               | Numeric     | Debt-to-Income ratio = Monthly Debt / (Annual Income / 12) |
| Loan_to_Income    | Numeric     | Loan amount relative to income |
| Risk Score        | Numeric     | Composite risk score based on credit issues |
| Risk Category     | Categorical | Risk segmentation: Low, Medium, High |

---

## ⚙️ Data Cleaning Notes

- Placeholder values (e.g., `99999999`) treated as missing
- Credit Score values > 850 corrected by dividing by 10
- Missing values handled using:
  - Median (numerical columns)
  - Mode or logical replacement (categorical columns)
- Outliers capped at the 99th percentile
- Invalid or inconsistent entries removed where necessary

---

## 📦 Dataset Summary

- Rows: ~10,000+
- Columns: 10+ (including engineered features)
- Format: Tabular (CSV)
- Source: Public dataset (e.g., Kaggle / data.gov)

---

## ⚠️ Notes

- No ground-truth `loan_status` column is used
- Analysis is based on **risk segmentation**, not default prediction
- Engineered features are designed to support KPI analysis and dashboarding