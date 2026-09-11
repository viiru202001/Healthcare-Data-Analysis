# Healthcare Analytics Dashboard

An end-to-end healthcare data analytics portfolio project using **SQL + Python + Power BI**.

## Dataset
The supplied dataset contains 10,000 healthcare records and 15 original columns. The public project version removes the direct personal fields `Name` and `Doctor` before sharing.

### Dashboard capabilities
- Executive KPIs: patients, average age, length of stay, total/average billing
- Medical condition analysis
- Test-result distribution
- Monthly admissions trend
- Admission-type billing
- Medication utilization
- Insurance-provider billing
- Hospital performance table
- Interactive filters for condition, gender, admission type, test result and date

## Tech stack
- **Python:** pandas, Plotly, Streamlit
- **SQL:** SQLite-compatible schema and analytical queries
- **Power BI:** data model, DAX measures and report layout specification
- **GitHub:** source control and portfolio delivery

## Project structure
```text
.
├── app.py
├── requirements.txt
├── data/
│   └── healthcare_clean.csv
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
└── powerbi/
    ├── README.md
    └── measures.dax
```

## Run the Python dashboard
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## SQL
The SQL folder contains the logical schema, indexes and 10 analytical queries for KPIs, conditions, outcomes, admissions, billing, insurance, medication and hospital performance.

## Power BI
Open `powerbi/README.md` and `powerbi/measures.dax` for the recommended model, measures, visuals and interactions.

## Important note
This project is for analytics/portfolio demonstration and is not a clinical decision-support system. The data should not be interpreted as real-world clinical guidance.

## Data privacy
Do not add the original raw CSV to a public repository. The supplied file contains names and doctor names, so the repository uses a cleaned version that excludes those fields.
