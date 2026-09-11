import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Healthcare Analytics Dashboard", page_icon="🏥", layout="wide")
DATA = Path(__file__).parent / "data" / "healthcare_clean.csv"

@st.cache_data
def load_data():
    d = pd.read_csv(DATA, parse_dates=["Date_of_Admission", "Discharge_Date"])
    if "Length_of_Stay" not in d.columns:
        d["Length_of_Stay"] = (d["Discharge_Date"] - d["Date_of_Admission"]).dt.days
    return d

df = load_data()
st.title("🏥 Healthcare Analytics Dashboard")
st.caption("Interactive analysis of admissions, conditions, outcomes, utilization and billing.")

st.sidebar.header("Filters")
conditions = st.sidebar.multiselect("Medical condition", sorted(df["Medical_Condition"].unique()), default=sorted(df["Medical_Condition"].unique()))
genders = st.sidebar.multiselect("Gender", sorted(df["Gender"].unique()), default=sorted(df["Gender"].unique()))
admission_types = st.sidebar.multiselect("Admission type", sorted(df["Admission_Type"].unique()), default=sorted(df["Admission_Type"].unique()))
results = st.sidebar.multiselect("Test result", sorted(df["Test_Results"].unique()), default=sorted(df["Test_Results"].unique()))
date_min, date_max = df["Date_of_Admission"].min().date(), df["Date_of_Admission"].max().date()
date_range = st.sidebar.date_input("Admission date", (date_min, date_max), min_value=date_min, max_value=date_max)
start, end = (pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])) if isinstance(date_range, tuple) and len(date_range) == 2 else (pd.Timestamp(date_min), pd.Timestamp(date_max))

f = df[df["Medical_Condition"].isin(conditions) & df["Gender"].isin(genders) & df["Admission_Type"].isin(admission_types) & df["Test_Results"].isin(results) & df["Date_of_Admission"].between(start, end)].copy()

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Patients", f"{len(f):,}")
c2.metric("Avg age", f"{f['Age'].mean():.1f}" if len(f) else "—")
c3.metric("Avg stay", f"{f['Length_of_Stay'].mean():.1f} days" if len(f) else "—")
c4.metric("Total billing", f"${f['Billing_Amount'].sum():,.0f}" if len(f) else "$0")
c5.metric("Avg billing", f"${f['Billing_Amount'].mean():,.0f}" if len(f) else "$0")
st.divider()

col1,col2 = st.columns(2)
with col1:
    by_condition = f.groupby("Medical_Condition").size().reset_index(name="Patients").sort_values("Patients", ascending=False)
    st.plotly_chart(px.bar(by_condition, x="Medical_Condition", y="Patients", title="Patients by Medical Condition"), use_container_width=True)
with col2:
    by_result = f.groupby("Test_Results").size().reset_index(name="Patients")
    st.plotly_chart(px.pie(by_result, names="Test_Results", values="Patients", hole=0.45, title="Test Result Distribution"), use_container_width=True)

col1,col2 = st.columns(2)
with col1:
    monthly = f.set_index("Date_of_Admission").resample("MS").size().reset_index(name="Admissions")
    st.plotly_chart(px.line(monthly, x="Date_of_Admission", y="Admissions", markers=True, title="Monthly Admissions"), use_container_width=True)
with col2:
    billing = f.groupby("Admission_Type")["Billing_Amount"].agg(["count","mean"]).reset_index()
    billing.columns=["Admission_Type","Admissions","Avg Billing"]
    st.plotly_chart(px.bar(billing, x="Admission_Type", y="Avg Billing", text_auto=".2s", title="Average Billing by Admission Type"), use_container_width=True)

col1,col2 = st.columns(2)
with col1:
    med = f.groupby("Medication").size().reset_index(name="Patients").sort_values("Patients", ascending=False)
    st.plotly_chart(px.bar(med, x="Patients", y="Medication", orientation="h", title="Medication Utilization"), use_container_width=True)
with col2:
    ins = f.groupby("Insurance_Provider")["Billing_Amount"].agg(["count","sum","mean"]).reset_index()
    ins.columns=["Insurance_Provider","Patients","Total Billing","Avg Billing"]
    st.plotly_chart(px.bar(ins, x="Insurance_Provider", y="Total Billing", title="Total Billing by Insurance Provider"), use_container_width=True)

st.subheader("Hospital performance")
hosp = f.groupby("Hospital").agg(Patients=("Hospital","size"), Avg_Stay=("Length_of_Stay","mean"), Total_Billing=("Billing_Amount","sum"), Avg_Billing=("Billing_Amount","mean")).reset_index().sort_values("Patients", ascending=False).head(15)
st.dataframe(hosp.style.format({"Avg_Stay":"{:.1f}", "Total_Billing":"${:,.0f}", "Avg_Billing":"${:,.0f}"}), use_container_width=True, hide_index=True)
with st.expander("Filtered data"):
    st.dataframe(f, use_container_width=True, hide_index=True)
