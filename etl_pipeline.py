import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Sample raw data
data = {
    'age': [25, 30, 35, 40, None],
    'gender': ['Male', 'Female', None, 'Male', None],
    'salary': [50000, 60000, 70000, None, 40000],
    'purchased': ['No', 'Yes', 'Yes', 'No', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)

# Encode categorical values
le_gender = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])  # Male=1, Female=0

le_purchased = LabelEncoder()
df['purchased'] = le_purchased.fit_transform(df['purchased'])  # Yes=1, No=0

# Scale numeric values
scaler = StandardScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

# Rename columns to indicate scaled values
df.rename(columns={'age': 'age_scaled', 'salary': 'salary_scaled'}, inplace=True)

# Save to CSV (current directory)
df.to_csv("complete_output.csv", index=False)

print("Saved: complete_output.csv")
