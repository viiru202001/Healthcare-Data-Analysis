-- Healthcare Analytics SQL Analysis Queries

-- 1. Executive KPIs
SELECT COUNT(*) AS total_patients, ROUND(AVG(Age), 1) AS avg_age,
       ROUND(AVG(Length_of_Stay), 1) AS avg_length_of_stay,
       ROUND(SUM(Billing_Amount), 2) AS total_billing,
       ROUND(AVG(Billing_Amount), 2) AS avg_billing
FROM healthcare_records;

-- 2. Patients by medical condition
SELECT Medical_Condition, COUNT(*) AS patients
FROM healthcare_records GROUP BY Medical_Condition ORDER BY patients DESC;

-- 3. Test outcome distribution
SELECT Test_Results, COUNT(*) AS patients,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM healthcare_records GROUP BY Test_Results ORDER BY patients DESC;

-- 4. Monthly admissions
SELECT strftime('%Y-%m', Date_of_Admission) AS admission_month, COUNT(*) AS admissions
FROM healthcare_records GROUP BY admission_month ORDER BY admission_month;

-- 5. Billing by admission type
SELECT Admission_Type, COUNT(*) AS admissions,
       ROUND(AVG(Billing_Amount), 2) AS avg_billing,
       ROUND(SUM(Billing_Amount), 2) AS total_billing
FROM healthcare_records GROUP BY Admission_Type ORDER BY total_billing DESC;

-- 6. Condition-level billing and stay
SELECT Medical_Condition, COUNT(*) AS patients,
       ROUND(AVG(Length_of_Stay), 1) AS avg_stay,
       ROUND(AVG(Billing_Amount), 2) AS avg_billing,
       ROUND(SUM(Billing_Amount), 2) AS total_billing
FROM healthcare_records GROUP BY Medical_Condition ORDER BY total_billing DESC;

-- 7. Insurance provider performance
SELECT Insurance_Provider, COUNT(*) AS patients,
       ROUND(SUM(Billing_Amount), 2) AS total_billing,
       ROUND(AVG(Billing_Amount), 2) AS avg_billing
FROM healthcare_records GROUP BY Insurance_Provider ORDER BY total_billing DESC;

-- 8. Medication utilization
SELECT Medication, COUNT(*) AS patients
FROM healthcare_records GROUP BY Medication ORDER BY patients DESC;

-- 9. Hospital performance
SELECT Hospital, COUNT(*) AS patients,
       ROUND(AVG(Length_of_Stay), 1) AS avg_stay,
       ROUND(SUM(Billing_Amount), 2) AS total_billing,
       ROUND(AVG(Billing_Amount), 2) AS avg_billing
FROM healthcare_records GROUP BY Hospital HAVING COUNT(*) >= 5
ORDER BY patients DESC, total_billing DESC LIMIT 20;

-- 10. Gender and outcome cross-tab
SELECT Gender, Test_Results, COUNT(*) AS patients
FROM healthcare_records GROUP BY Gender, Test_Results ORDER BY Gender, patients DESC;
