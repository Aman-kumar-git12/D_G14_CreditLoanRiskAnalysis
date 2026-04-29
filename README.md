# 🏦 Credit Loan Risk Analysis & Portfolio Optimization (D_G-14)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

## 📌 Project Overview
This project presents an end-to-end data pipeline designed to analyze credit loan risk for a $3.6B banking portfolio. The goal of this analysis is to categorize portfolio risk, identify key drivers of financial instability (like Debt-to-Income ratios and credit issues), and provide actionable, data-driven business insights through comprehensive reporting and interactive dashboards.

From raw data extraction to a final presentation, this repository captures every phase of the analytical lifecycle.

---

## 🛠️ End-to-End Workflow

This project follows a structured methodology split into distinct phases:

### 1️⃣ Data Extraction & Cleaning (`notebooks/01` & `02`)
- **Extraction:** Loaded raw loan data to establish our baseline dataset.
- **Cleaning:** Handled systemic anomalies, such as converting `99999999` placeholder values into missing data, fixing credit scores exceeding the 850 maximum, and imputing missing categorical/numerical values using statistical logic.
- **Outliers:** Applied 99th-percentile clipping to ensure robust statistical analysis.

### 2️⃣ EDA & Statistical Analysis (`notebooks/03` & `04`)
- **Exploratory Data Analysis (EDA):** Uncovered patterns across income levels, home ownership, and loan purposes.
- **Feature Engineering:** Developed critical business metrics including:
  - **DTI (Debt-to-Income):** Monthly Debt / (Annual Income / 12)
  - **Risk Score:** A composite score based on bankruptcies, tax liens, and credit problems.
  - **Risk Category:** Segmented borrowers into `Low`, `Medium`, and `High` risk tiers.
- **Statistical Testing:** Validated findings and correlations to ensure statistically significant results.

### 3️⃣ Final Data Prep & Dashboarding (`notebooks/05` & `tableau/`)
- Exported the finalized, cleaned dataset for business intelligence integration.
- Developed an interactive **Tableau Dashboard** to visualize risk distributions, high-risk geographic/employment segments, and portfolio health.
- 🔗 **[View the Live Tableau Dashboard Here](https://public.tableau.com/app/profile/aman.kumar7311/viz/bank_loan_risk/Dashboard1?publish=yes)**
- *Note: Screenshots of the dashboard are available in the `tableau/screenshots/` directory.*

### 4️⃣ Reporting & Presentation (`reports/`)
Synthesized the technical findings into executive-ready reports:
- `BankLoanRisk_Rethemed.pdf` / `presentation.pdf`: The final slide deck highlighting the problem statement, ETL process, key findings, and strategic recommendations (e.g., dynamic pricing, ML models).
- `project_report.pdf`: A comprehensive text-based report detailing the methodology and conclusions.

---

## 📂 Repository Structure

```text
D_G-14_Loan/
├── data/
│   └── processed/          # Final cleaned datasets ready for BI consumption
├── docs/
│   └── data_dictionary.md  # Detailed description of all original and engineered features
├── notebooks/
│   ├── 01_extraction.ipynb # Raw data ingestion
│   ├── 02_cleaning.ipynb   # Data cleaning and anomaly resolution
│   ├── 03_eda.ipynb        # Exploratory Data Analysis
│   ├── 04_statistical_analysis.ipynb # Advanced statistical tests
│   └── 05_final_load_prep.ipynb      # Final export formatting for Tableau
├── reports/
│   ├── presentation.pdf    # Executive slide deck (Canva export)
│   ├── project_report.pdf  # Comprehensive written analysis
│   └── BankLoanRisk_Rethemed.pdf
├── scripts/
│   └── etl_pipeline.py     # Core python scripts containing ETL and engineering logic
├── tableau/
│   ├── dashboard_links.md  # Links to public Tableau dashboards
│   └── screenshots/        # Visual exports from the dashboard
└── README.md               # You are here!
```

---

## 🚀 How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aman-kumar-git12/D_G14_CreditLoanRiskAnalysis.git
   cd D_G14_CreditLoanRiskAnalysis
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Notebooks:**
   Launch Jupyter Notebook and execute the notebooks in sequential order (01 to 05) to recreate the cleaned dataset from scratch.
   ```bash
   jupyter notebook
   ```

4. **View the Dashboard:**
   Click the [Tableau Public Link](https://public.tableau.com/app/profile/aman.kumar7311/viz/bank_loan_risk/Dashboard1?publish=yes) to interact with the visual analysis.

---

## 🤝 Team Contributions (Team D_G-14)
This project was successfully delivered by a team of 6 members, collectively driving the data extraction, pipeline architecture, statistical validation, and final business presentation.

**Next Steps & Future Roadmap:**
- Implementation of a Supervised Machine Learning Model (XGBoost) for real-time risk prediction.
- Integration of live API connectivity to replace static CSV extracts.
- Introduction of Dynamic Pricing logic to automatically correlate interest rates with borrower risk categories.
