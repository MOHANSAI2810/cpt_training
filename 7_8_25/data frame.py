import pandas as pd
data = {
    'name': ['john Doe', None, 'alice Brown', 'bob Lee', 'mary White', 'Tom Green', 'Sara Black'],
    'id': ['1', '2', '3', '4', '5', '6', '7'],
        'age': [45, 30, 25, 60, None, 38, 28],
        'cause': ['Fever', 'Fracture', 'Flu', 'Heart Attack', 'Migraine', None, 'Allergy'],
    'date': ['2025-08-01', '2025-08-02', '2025-08-03', '2025-08-01', '2025-08-04', '2025-08-03', '2025-08-02'],
    'bill': [2500.0, 5000.0, 1500.0, 12000.0, 2000.0, 4000.0, 1800.0]
}
df = pd.DataFrame(data)

df.to_csv('hospital_data.csv', index=False)

print("✅ Static hospital data for 7 patients saved to 'hospital_data.csv'")