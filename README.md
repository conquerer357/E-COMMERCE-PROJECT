# Amazon Sales Analysis (March–June 2022)
**E-Commerce Performance Dashboard**

An end-to-end data analytics project analyzing Amazon fashion sales across Q2 2022, covering 126,241 orders and ₹77M in revenue across 34 Indian states. The project identifies key drivers of revenue decline, operational inefficiencies, and strategic opportunities to improve profitability.

&nbsp;

## Project Structure

    C:\Documents\Data analytics\projects\my-data-project\E-COMMERCE-PROJECT

    Analysis code\
        analysis.ipynb

    Data Cleaning code\
        data_cleaning.ipynb

    data\
        processed\
            amazon_sales_cleaned.csv
        Queried\
            cancellation_by_fulfilled_by.csv
            cancellation_by_fulfillment.csv
            monthly_revenue_trends.csv
            revenue_by_category.csv
            revenue_by_category_size.csv
            revenue_by_state.csv
            shipping_speed_completion.csv
        raw\
            Amazon Sale Report.csv

    Tableau\
        ecomms refined.twb
        fulfillment performance.png
        monthly trends.png
        Revenue by catagory.png
        Revenue by state.png
        shipping speed comparison.png

    README.md

&nbsp;

## Key Metrics

**Total Orders** 126,241

**Total Revenue** ₹77M

**Average Order Value** ₹644

**Cancellation Rate** 15%

&nbsp;

## Tools Used

**Python (Pandas)**
Python was chosen as the data processing layer due to its industry-standard status in analytics, efficient handling of large datasets (126K+ rows) with minimal overhead, and reproducible scripting workflows that can be re-run against updated data. Pandas groupby, aggregation, and pivot operations made it straightforward to compute all business metrics and export clean CSVs for visualization.

**Tableau Desktop**
Tableau was chosen over Python visualization libraries (matplotlib, seaborn) for its superior chart output quality, faster prototyping of different chart types, and professional presentation-ready results. The dashboard was intentionally kept simple and clean, prioritizing clarity and immediate insight comprehension over complex interactivity. Rather than overwhelming stakeholders with filters and drill-downs, the design focuses on the 6 most critical business metrics in a single, scannable view.


## Executive Summary

This analysis examines Amazon sales performance across Q2 2022 (March–June), identifying critical insights into revenue trends, operational efficiency, and market distribution. The project addresses three core business questions:

1. What is driving the 10.3% month-over-month revenue decline from April to June?
2. How much revenue is lost to cancellations, and which fulfillment method performs better?
3. Where should marketing and operations teams focus resources for maximum ROI?



### Revenue Trend Analysis

![Revenue Trends](Tableau/monthly%20trends.png)

After an initial spike to ₹28.2M in April, revenue declined consistently by 8.9% in May (₹25.7M) and 10.3% in June (₹23.1M). This 17.8% total decline from peak represents ₹5.1M in lost monthly revenue. April likely captured festival/wedding season demand in India, while subsequent months reflect market normalization or weakening customer acquisition.


### Fulfillment Performance Gap


![Fulfillment Performance](Tableau/fulfillment%20performance.png)

Merchant fulfillment demonstrates significantly worse performance than Amazon fulfillment. The cancellation rate for merchant orders stands at 16.9% versus Amazon's 12.4% — a 36% relative increase. More critically, merchant fulfillment loses 12.7% of potential revenue to cancellations, nearly double Amazon's 6.6% loss rate. With merchant fulfillment handling 30.6% of total orders, this represents ₹3.0M in preventable lost revenue. Migrating 50% of merchant orders to Amazon fulfillment would recover approximately ₹750K.


### Product Portfolio Concentration

![Revenue By catagory](Tableau/Revenue%20by%20catagory.png)

Three categories account for 91.2% of total revenue. Sets contribute 49.96% (₹38.5M), Kurtas contribute 27.16% (₹20.9M), and Western Dress contributes 14.08% (₹10.8M). The remaining six categories collectively generate only 8.8%, representing both a concentration risk and an untapped diversification opportunity.


### Geographic Revenue Distribution

![Revenue By State](Tableau/Revenue%20by%20state.png)

Top 10 states generate 73% of revenue while 24 states contribute the remaining 27%. Maharashtra alone accounts for 17% of total sales. The top 3 states — Maharashtra, Karnataka, and Uttar Pradesh — together generate 38.8% of revenue, indicating highly concentrated demand in urban and semi-urban markets.



### Shipping Speed and Completion Rates

![Shipping Speed](Tableau/shipping%20speed%20comparison.png)

Expedited shipping demonstrates an 87% successful delivery rate versus 72% for standard shipping. Expedited also shows a lower cancellation rate (12.5% vs 16.5%) and near-zero return rates compared to standard's 4.9% return rate. This 15-percentage-point completion gap suggests customers strongly value faster delivery and that expedited should be positioned as the default shipping option.



## Business Insights

**1. Revenue Trajectory Shows Concerning Decline**

After spiking from March (₹101K, only 170 orders — incomplete data) to April (₹28.2M), revenue fell 8.9% in May and 10.3% in June. If this trend continues into Q3, monthly revenue could drop below ₹20M. April's spike most likely reflects Indian wedding/festival season demand, suggesting that replicating those conditions — through targeted campaigns around Diwali and Raksha Bandhan — could stabilize performance.

**2. Fulfillment Choice Directly Impacts Profitability**

Amazon fulfillment: 12.4% cancellation rate, 6.6% lost revenue, ₹3.5M total lost revenue.
Merchant fulfillment: 16.9% cancellation rate, 12.7% lost revenue, ₹3.0M total lost revenue.

The gap is not marginal — merchant fulfillment loses nearly twice the revenue percentage. Shifting high-value categories (Sets, Kurtas) to FBA could recover ₹1.5M annually.

**3. Product Portfolio Concentration Risk**

Sets (₹782 AOV), Kurtas (₹428 AOV), and Western Dress (₹725 AOV) dominate the portfolio. A 10% decline in Sets alone would reduce total revenue by 5%. Bottom, Saree, and Dupatta categories are critically underperforming despite strong cultural relevance in the Indian market.

**4. Geographic Revenue Follows the 80/20 Principle**

States ranked 11–34 average ₹358K each (0.46% per state). Lakshadweep, Mizoram, and Dadra show less than ₹50K in revenue each. Marketing spend in these states should be paused until viability is assessed. The highest-performing states — particularly Telangana and Tamil Nadu — show high order volumes relative to their population, suggesting strong organic demand worth amplifying.

**5. Shipping Speed Correlates with Order Completion**

Expedited: 75,309 shipped out of 86,531 total (87% completion).
Standard: 28,478 delivered out of 39,710 total (72% completion).
Standard shipping also shows a 4.9% return rate, adding reverse logistics cost on top of lower completion. Customers on expedited shipping cancel less and return less.



## Strategic Recommendations

**Priority 1 — Migrate to Amazon Fulfillment**
Expected impact: Recover ₹1.5M annually.
Phase out merchant fulfillment for Sets and Kurtas first. Negotiate FBA fees on volume. Monitor cancellation rates weekly during transition. Target: reduce overall cancellation rate from 15% to 13% within 2 months.

**Priority 2 — Reverse the Revenue Decline**
Expected impact: Stabilize monthly revenue at ₹24M+.
Investigate April spike drivers. If festival-driven, build campaigns around upcoming Indian festivals. Test promotional pricing on Sets to boost order volume. Launch retargeting in Maharashtra and Karnataka, the two highest-revenue states.

**Priority 3 — Diversify Product Revenue Mix**
Expected impact: Reduce concentration risk, expand addressable market by 15%.
Grow Tops (currently 6.8%) and Ethnic Dress (1%) through targeted listings and promotions. Test bundle offers: Kurta + Bottom + Dupatta. Investigate why Sarees underperform despite cultural relevance. Target: grow non-top-3 category share from 9% to 15% within 6 months.

**Priority 4 — Optimize State-Level Marketing Spend**
Expected impact: Improve marketing ROI by 25%.
Increase ad spend in top 5 revenue states. Pause acquisition campaigns in states below ₹50K. Test localized creative in regional languages for tier-2 states. Conduct customer research in Telangana and Tamil Nadu to understand their above-average engagement.

**Priority 5 — Promote Expedited Shipping as Default**
Expected impact: Reduce cancellations by 4%, improve customer satisfaction.
Pre-select expedited at checkout. Offer free expedited for orders above ₹1,000 (above current AOV of ₹644). A/B test messaging: "Arrives in 2 days" versus "Standard 5–7 days." Track whether faster delivery reduces the 4.9% return rate on standard orders.


## Analysis Pipeline

The project was split into two notebook stages: a cleaning notebook that produced one modeling-ready fact table, and an analysis notebook that converted that table into Tableau-ready summary extracts.

**Notebook 1 - Data cleaning**

Source notebook: `Data Cleaning code/data_cleaning.ipynb`

1. Loaded the raw transaction export from `data/raw/Amazon Sale Report.csv` into Pandas.
2. Created a working copy and standardized column names by trimming whitespace, converting to lowercase, and replacing spaces and hyphens with underscores.
3. Removed columns not used in downstream analysis: `index`, `unnamed:_22`, `ship_country`, `currency`, `ship_postal_code`, `promotion_ids`, `courier_status`, `asin`, and later `order_id` and `ship_city`.
4. Normalized all text fields by trimming values, lowercasing them, converting separators to underscores, and converting empty strings back to nulls.
5. Enforced a consistent schema across dates, categoricals, numeric fields, and booleans so the analysis notebook could aggregate without ad hoc type fixes.
6. Replaced placeholder missing-value tokens such as `N/A`, `None`, `null`, and `?` with proper nulls.
7. Dropped duplicate rows from the working table.
8. Standardized dirty categorical labels:
   - `status` values were cleaned by collapsing malformed underscore patterns.
   - `ship_state` values were mapped to canonical names such as `odisha`, `rajasthan`, `uttar_pradesh`, and `jammu_&_kashmir`.
9. Exported the cleaned dataset to `data/processed/amazon_sales_cleaned.csv`.

The cleaned table contained 126,241 rows and 14 analysis columns:
`date`, `status`, `fulfilment`, `sales_channel`, `ship_service_level`, `style`, `sku`, `category`, `size`, `qty`, `amount`, `ship_state`, `b2b`, `fulfilled_by`.

**Notebook 2 - Business analysis**

Source notebook: `Analysis code/analysis.ipynb`

1. Loaded `data/processed/amazon_sales_cleaned.csv`.
2. Created an `is_cancelled` flag from `status == 'cancelled'` to simplify loss-rate calculations.
3. Built fulfillment performance tables:
   - `cancellation_by_fulfillment.csv`: compared Amazon vs merchant fulfillment using total orders, cancelled orders, revenue, lost revenue, cancellation rate, and lost revenue percent.
   - `cancellation_by_fulfilled_by.csv`: summarized cancellation rate by the `fulfilled_by` field.
4. Built geography and assortment tables:
   - `revenue_by_state.csv`: captured revenue, order count, and revenue share by state.
   - `revenue_by_category.csv`: captured revenue, order count, and revenue share by category.
   - `revenue_by_category_size.csv`: captured the category-size revenue mix for merchandise depth analysis.
5. Built delivery-operations tables:
   - `shipping_speed_completion.csv`: captured order status mix, revenue, group totals, and within-service-level percentages for each shipping service level.
6. Built time-series tables:
   - Converted `date` to datetime and derived a `month` field.
   - `monthly_revenue_trends.csv`: captured monthly revenue, total orders, average order value, and month-over-month revenue change.
7. Exported all summary tables to `data/Queried/` for Tableau consumption.

**Reporting layer**

The seven CSV extracts in `data/Queried/` were the direct inputs to the Tableau workbook in `Tableau/ecomms refined.twb`. Tableau was used only after the heavy lifting was finished in Pandas, so the dashboard layer stayed focused on presentation rather than data wrangling.

**Implementation note**

Both notebooks used absolute local file paths under the repository's `data/` directory, with raw inputs in `data/raw/`, the cleaned fact table in `data/processed/`, and Tableau-ready extracts in `data/Queried/`. 



## Metrics Definitions

**Cancellation Rate** = (Cancelled Orders / Total Orders) x 100

**Lost Revenue %** = (Lost Revenue / Total Potential Revenue) x 100

**Average Order Value** = Total Revenue / Total Orders

**Month-over-Month Growth** = ((Current Month Revenue - Previous Month Revenue) / Previous Month Revenue) x 100

**Category Concentration** = Top 3 Categories Revenue / Total Revenue x 100


## Dashboard Design

The Tableau dashboard was intentionally kept simple and clean. Rather than building an interactive tool with multiple filter panes and drill-down layers, the focus was on presenting the 6 most critical insights in a single, immediately scannable layout. This design decision reflects the audience: business stakeholders who need clear answers quickly, not an analytics playground. The visual hierarchy places KPI cards at the top, followed by trend and operational comparisons in the middle, and geographic and category breakdowns at the bottom.
