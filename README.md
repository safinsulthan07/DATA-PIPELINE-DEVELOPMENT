# DATA-PIPELINE-DEVELOPMENT

"COMPANY":CODETECH IT SOLUTIONS

"NAME":G NAVEEN

"INTERN ID":CT04DF448

"DOMAIN":DATA SCIENCE

"DURATION": 4 WEEKS

"MENTOR":NEELA SANTOSH


This Python script demonstrates a typical data preprocessing workflow using the pandas and scikit-learn libraries. It performs key steps such as handling missing values, encoding categorical variables, scaling numerical features, and exporting the cleaned dataset to a CSV file. These operations are fundamental in preparing data for machine learning models and analytics.

1. Data Initialization
The code starts by creating a dictionary containing sample data for four columns: age, gender, salary, and purchased. This dictionary simulates a dataset with missing values (represented by None). The data is then converted into a pandas DataFrame for easier manipulation.

2. Handling Missing Values
Missing data is a common issue in real-world datasets. The script addresses this using the fillna() method:

For the age column, missing values are filled with the mean age of the existing entries.

For the gender column, the mode (most frequently occurring value) is used to fill in the blanks. This is appropriate for categorical data.

For the salary column, the mean salary is used to replace missing values.

This ensures that no missing data remains, which is essential for training most machine learning models, as they typically cannot handle NaN or None values directly.

3. Encoding Categorical Variables
Machine learning models generally require numeric input. Hence, the code converts the categorical columns gender and purchased into numeric values using LabelEncoder from scikit-learn:

gender: 'Male' is encoded as 1, and 'Female' as 0.

purchased: 'Yes' is encoded as 1, and 'No' as 0.

LabelEncoder is simple and effective for binary or ordinal categorical data, although other methods like one-hot encoding are used for multi-class scenarios.

4. Feature Scaling
Feature scaling is a critical step when working with machine learning models, especially those based on distance (like KNN or SVM). The script uses StandardScaler to normalize the age and salary columns:

StandardScaler transforms features such that they have a mean of 0 and a standard deviation of 1 (Z-score normalization).

This ensures that one feature does not dominate another due to differences in units or scale.

The transformed columns overwrite the originals, and are then renamed to age_scaled and salary_scaled for clarity.

5. Saving the Cleaned Data
Finally, the processed DataFrame is saved to a CSV file named complete_output.csv using the to_csv() method. The index=False argument ensures that the DataFrame index is not written to the file.

Conclusion
This code is a compact and practical example of a real-world data preprocessing pipeline. It covers all critical aspects—cleaning missing values, encoding categorical variables, scaling numerical features, and saving results. These steps form the backbone of preparing data for analysis and model building, and the code can easily be adapted to larger or more complex datasets.
