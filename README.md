E-commerce Sales and Cancellations analysis (March-June 2022).

a. Project Overview
____________________


This project focuses on analysiing Amazon sales and cancellation trends from March to April, in the year 2022.
It was designed to showcase a complete data analysis/science workflow, from raw data cleaning with Python and Pandas to Sql quering in Postgressql(PgAdmin), and then summarizing and visualising in Excel and Tableau.

This analysis focuses on uncovering:
1) Revenue by month.
2) Top 15 Skus by Sales.
3) Cancellation statistics by states.
4) Cancellation statistics by billing timing, pre vs post.
5) Fulfillment performance, Amazon vs Merchant.


b. Tools Used
_______________

1) PostgresSql with PgAdmin.
2) Python with Numpy and Pandas.
3) Excel.
4) Tableau Public.

c. Workflow
_____________

1) Data Cleaning: Removed nulls, standardized fulfillment logic, and formatted dates in Python.

2) SQL Analysis: Wrote queries to analyze monthly revenue, SKU performance, cancellation rates, and fulfillment splits.

3) Excel Visualization: Built pivot charts to explore early patterns and validate metrics.

4) Tableau Dashboard: Combined key insights into an interactive dashboard summarizing sales trends and cancellations.

d. Insights
____________

Peak sales occurred in April 2022 (₹25.6M), followed by a steady seasonal decline post-billing.

Revenue concentration is high across a few SKUs and regions — top 5 SKUs and top 3 states (Maharashtra, Karnataka, Tamil Nadu) drive most sales.

Cancellation behavior: ~59% of cancellations occur after billing, pointing toward refund-stage drop-offs or fulfillment delays.

Fulfillment performance: Merchant-handled orders show higher post-billing cancellations (~75%), indicating seller-side dispatch or QC bottlenecks.

Regional imbalance: North-East and Island states show disproportionately high cancellation rates — likely due to logistic limitations or limited serviceability.

e. Recommendations
____________________

Optimize logistics in North-East and Island regions — improve delivery SLAs and communication during checkout.

Review seller performance for Merchant-fulfilled orders; consider shifting high-volume SKUs to Amazon-fulfillment.

Encourage SKU diversification — promote lower-performing SKUs in high-revenue regions to balance sales.

Introduce predictive cancellation scoring using historical order behavior to flag risky orders pre-billing.

Maintain April-level engagement strategies (ads, offers) into later months to stabilize revenue.

f. Project Structure
_____________________


Project Structure

E-COMMERCE-PROJECT/
│
├── data/
│ └── raw/
│ ├── Amazon Sale Report.csv
│ ├── Cloud Warehouse.csv
│ ├── Expense IIGF.csv
│ ├── International Sale Report.csv
│ ├── May-2022.csv
│ └── P L March 2021.csv
│
├── export/
│ ├── cancellations_story.csv
│ ├── monthly_revenue.csv
│ ├── TOP_SKUS_BY_REVENUE.csv
│ ├── cancellations_by_state.csv
│ ├── cancellation_pre_post_billing.csv
│ └── cancellations_by_fulfillment.csv
│
├── docs/
│ ├── schema_audit.txt
│ ├── EXCEL_DASHBOARD_SUMMARY.png
│ └── Tableau_Dashboard_Summary.png
│
├── EXCEL/
│ └── Project.xlsx
│
├── python/
│ ├── data_cleaning.py
│ └── intro.py
│
├── sql/
│ ├── monthly_revenue.sql
│ ├── cancellations_by_state.sql
│ ├── cancellations_story.sql
│ ├── cancellation_pre_post_billing.sql
│ └── TOP_SKUS_BY_REVENUE.sql
│
├── tableau/
│ └── Project_amazon_sales_analysis.twbx
│
└── README.md

Dashboard Previews

Excel Dashboard Summary
Exploratory dashboard built with pivot charts and calculated KPIs.
![Excel Dashboard_Summary](docs/EXCEL_DASHBOARD_SUMMARY.png)

Tableau Dashboard Summary
![Tableau Dashboard Summary](docs/Tableau_Dashboard_summary.png)


Link: https://public.tableau.com/app/profile/akshat.verma12/viz/Project_amazon_sales_analysis/Analysis_summary

Author:

Akshat Verma
Data Analytics | SQL | Python | Excel | Tableau
Email: theconquerer357@gmail.com

LinkedIn: https://www.linkedin.com/in/akshat-verma-b5284a38a/
GitHub: https://github.com/conquerer357/E-COMMERCE-PROJECT
