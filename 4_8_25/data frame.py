import pandas as pd
data = {
    'name': ['John Doe', None, 'Alice Brown', 'Bob Lee', 'Mary White', 'Tom Green', 'Sara Black'],
    'id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007'],
    'age': [45, 30, 25, 60, None, 38, 28],
    'cause': ['Fever', 'Fracture', 'Flu', 'Heart Attack', 'Migraine', None, 'Allergy'],
    'date': ['2025-08-01', '2025-08-02', '2025-08-03', '2025-08-01', '2025-08-04', '2025-08-03', '2025-08-02'],
    'bill': [2500.0, 5000.0, 1500.0, 12000.0, 2000.0, 4000.0, 1800.0]
}
df = pd.DataFrame(data)

df.to_csv('hospital_data.csv', index=False)

print("✅ Static hospital data for 7 patients saved to 'hospital_data.csv'")
