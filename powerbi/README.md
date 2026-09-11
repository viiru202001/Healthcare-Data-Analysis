# Power BI Report Build Guide

A `.pbix` binary report is created in Power BI Desktop. This folder contains the complete model, DAX measures, visuals and interaction plan.

## Load data
1. Open Power BI Desktop.
2. Get Data → Text/CSV.
3. Select `data/healthcare_clean.csv`.
4. Set date fields to Date and `Billing_Amount` to Decimal Number.

## Model
Create the `Date` table from `measures.dax` and relate `Date[Date]` to `healthcare_records[Date_of_Admission]`.

## Pages
### Executive Overview
Cards for Total Patients, Total Billing, Average Billing, Average Length of Stay and Abnormal Test Rate; charts for condition, test results, monthly admissions and admission-type billing.

### Patient & Outcomes
Slicers for Date, Gender, Medical Condition, Admission Type and Insurance Provider; charts for test results by condition, medication utilization, gender × test results and billing vs stay by condition.

### Hospital & Financials
Top hospital table plus insurance-provider billing and admission-type billing visuals.

## Interactivity
Use slicer sync across pages and enable drill-through from Medical Condition to a detail page.

## Data privacy
The public CSV excludes `Name` and `Doctor`. Do not publish the original raw patient/staff-identifying CSV.
