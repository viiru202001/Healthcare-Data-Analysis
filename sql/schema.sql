CREATE TABLE IF NOT EXISTS healthcare_records (
    id INTEGER PRIMARY KEY,
    Age INTEGER NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    Blood_Type VARCHAR(5) NOT NULL,
    Medical_Condition VARCHAR(50) NOT NULL,
    Date_of_Admission DATE NOT NULL,
    Hospital VARCHAR(255) NOT NULL,
    Insurance_Provider VARCHAR(100) NOT NULL,
    Billing_Amount DECIMAL(12,2) NOT NULL,
    Room_Number INTEGER NOT NULL,
    Admission_Type VARCHAR(30) NOT NULL,
    Discharge_Date DATE NOT NULL,
    Medication VARCHAR(100) NOT NULL,
    Test_Results VARCHAR(30) NOT NULL,
    Length_of_Stay INTEGER
);

CREATE INDEX IF NOT EXISTS idx_admission_date ON healthcare_records(Date_of_Admission);
CREATE INDEX IF NOT EXISTS idx_condition ON healthcare_records(Medical_Condition);
CREATE INDEX IF NOT EXISTS idx_hospital ON healthcare_records(Hospital);
CREATE INDEX IF NOT EXISTS idx_admission_type ON healthcare_records(Admission_Type);
