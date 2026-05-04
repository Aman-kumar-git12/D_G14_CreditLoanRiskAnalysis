# NST DVA Capstone 2 - Project Repository
**Newton School of Technology | Data Visualization & Analytics**  
A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

---
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)


## Project Overview

| Field | Details |
| :--- | :--- |
| **Project Title** | Credit Loan Risk Analysis & Portfolio Optimization |
| **Sector** | Finance / Banking |
| **Team ID** | D_G-14 |
| **Section** | [To be filled by team] |
| **Faculty Mentor** | [To be filled by team] |
| **Institute** | Newton School of Technology |
| **Submission Date** | [29 Apr 2026] |

## Team Members

| Role | Name | GitHub Username |
| :--- | :--- | :--- |
| Project Lead | Aman Kumar | @Aman-kumar-git12 |
| Data Lead | Kartik Yadav | @NineT8 |
| ETL Lead | Prashant Pandey | [github-handle] |
| Analysis Lead | Anish Suman | [github-handle] |
| Visualization Lead | Kumar Sanu | [github-handle] |
| PPT & Quality Lead | Archit Gosain | [github-handle] |

*(Note: Replace placeholders with actual team member details)*

---

## Business Problem

The bank is currently managing a highly diverse $3.6B loan portfolio but struggles with a standardized method to quantify and mitigate credit risk. Without clear visibility into debt-to-income (DTI) thresholds, historical credit problems, and high-risk employment segments, the bank is exposed to significant potential defaults. This project provides a data-driven framework to categorize risk, optimize loan approval thresholds, and implement dynamic pricing strategies.

**Core Business Question**
What are the primary drivers of loan risk in the current portfolio, and how can we systematically segment borrowers to minimize defaults while maximizing interest revenue?

**Decision Supported**
This analysis enables credit risk managers to adjust lending criteria (e.g., DTI limits), apply dynamic interest rates based on Risk Categories, and flag high-risk demographic/geographic profiles for manual underwriter review.

---

## Dataset

| Attribute | Details |
| :--- | :--- |
| **Source Name** | Public Financial Dataset (e.g., Kaggle) |
| **Direct Access Link** | [Provide link to raw source if available] |
| **Row Count** | ~10,000+ (After cleaning) |
| **Column Count** | 10+ |
| **Time Period Covered** | Historical Loan Data |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
| :--- | :--- | :--- |
| `Annual Income` | Borrower's yearly income | Used to compute DTI and segment income groups |
| `Monthly Debt` | Borrower's monthly obligations | Used to compute DTI |
| `Credit Score` | Creditworthiness metric | Used for KPI & risk segmentation (adjusted >850 anomalies) |
| `Number of Credit Problems` | Past credit issues | Core driver for the composite Risk Score |
| `Years in current job` | Employment stability | Used for demographic risk segmentation |

For full column definitions, see `docs/data_dictionary.md`.

---

## KPI Framework

| KPI | Definition | Formula / Computation |
| :--- | :--- | :--- |
| **Debt-to-Income (DTI)** | Financial capacity to handle new debt | `Monthly Debt / (Annual Income / 12)` |
| **Composite Risk Score** | Aggregate score of historical financial issues | `Credit Problems + Bankruptcies + Tax Liens` |
| **Risk Category** | Categorical tiering of borrowers | `If Risk Score > 0 or DTI > 0.43 -> High, else Medium/Low` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
| :--- | :--- |
| **Dashboard URL** | [Live Tableau Dashboard](https://public.tableau.com/app/profile/aman.kumar7311/viz/bank_loan_risk/Dashboard1?publish=yes) |
| **Executive View** | High-level summary of the $3.6B portfolio, overall risk distribution (Low/Medium/High), and average DTI. |
| **Operational View** | Detailed drill-downs into risk by home ownership, employment length, and geographic location. |
| **Main Filters** | Risk Category, Loan Purpose, Home Ownership |

Store dashboard screenshots in `tableau/screenshots/` and document the public links in `tableau/dashboard_links.md`.

---

## Key Insights

1. **DTI is the primary driver of risk:** Borrowers with a DTI above 40% are disproportionately represented in the High-Risk category.
2. **Employment Tenure Impact:** Borrowers with less than 2 years of employment history exhibit significantly higher variance in credit scores.
3. **Credit Score Anomalies:** A systemic data entry issue caused over 10% of credit scores to exceed the maximum possible 850 (requiring a /10 adjustment).
4. **Home Ownership Correlation:** Renters show a 15% higher likelihood of falling into the Medium/High-Risk categories compared to mortgage holders.
5. **Debt Consolidation Dominates:** Over 70% of loan purposes are for debt consolidation, indicating a pre-existing high debt burden in the applicant pool.
6. **Zero-Tolerance for Tax Liens:** Applicants with even one historical tax lien almost universally fall into the High-Risk tier.
7. **Income Disparity:** The median annual income for Low-Risk borrowers is significantly higher than High-Risk borrowers, confirming the income-to-risk inverse relationship.
8. **Missing Data Patterns:** Applicants who refused to provide 'Years in current job' had a statistically higher correlation with missing credit scores.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
| :--- | :--- | :--- | :--- |
| 1 | DTI is the primary risk driver | Implement a hard stop or manual review trigger for any applicant with DTI > 43%. | 15% reduction in default exposure. |
| 2 | Renters show higher risk | Introduce a slight interest rate premium (Dynamic Pricing) for non-homeowners. | Increased revenue to offset renter default risks. |
| 3 | Debt Consolidation dominance | Require proof of closed accounts for debt consolidation loans post-funding. | Reduced likelihood of borrowers accumulating double-debt. |
| 4 | Manual Data Errors (Scores > 850) | Add input validation at the API/Application level to prevent scores > 850. | 100% reduction in this specific data quality issue. |

---

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- project_report.pdf
|   `-- presentation.pdf
|
|-- docs/
|   `-- data_dictionary.md
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:
1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
| :--- | :--- | :--- |
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Contribution Matrix
This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Aman Kumar | | | ✓ | | ✓ | | ✓ |
| Kartik Yadav | ✓ | | | | | ✓ | ✓ |
| Prashant Pandey | ✓ | ✓ | | | | | |
| Anish Suman | | | ✓ | ✓ | | | |
| Kumar Sanu | | | ✓ | | ✓ | | |
| Archit Gosain | | | | | | ✓ | ✓ |

**Declaration:** We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.

**Team Lead Name:** Aman Kumar

**Date:** 29 April 2026

---

## Academic Integrity
All analysis, code, and recommendations in this repository must be the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.
