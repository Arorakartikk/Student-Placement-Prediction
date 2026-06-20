Student Placement Prediction System
📌 Project Overview

The Student Placement Prediction System is a Machine Learning web application developed using Python, Scikit-Learn, Pandas, and Streamlit.

The project predicts whether a student is likely to be placed based on academic performance, work experience, employability test scores, educational background, and MBA specialization.

The trained model is deployed using Streamlit, allowing users to enter student details and receive real-time placement predictions along with confidence scores.

🎯 Project Objective

The objective of this project is to predict student placement outcomes using machine learning techniques.

The system helps analyze how academic performance, work experience, employability skills, and specialization affect placement opportunities.

📁 Dataset Information
Dataset Name

Placement.csv

Dataset Description

The dataset contains information about students including:

Academic Performance
Educational Background
Work Experience
Employability Test Scores
MBA Specialisation
Placement Status
Total Records

215 Students

Target Variable
Status	Meaning
1	Placed
0	Not Placed
Original Dataset Features
sl_no
gender
ssc_p
ssc_b
hsc_p
hsc_b
hsc_s
degree_p
degree_t
workex
etest_p
specialisation
mba_p
salary
status
🔍 Data Understanding

Before building the model, the dataset was analyzed using:

df.shape
df.columns
df.info()
df.describe()

The following were examined:

Dataset dimensions
Feature names
Data types
Statistical summaries
Overall data structure
🧹 Data Cleaning
Removed Unnecessary Column
df.drop("sl_no", axis=1, inplace=True)

The sl_no column was removed because it is only a serial number and has no predictive value.

🔄 Data Encoding
Label Encoding

Binary categorical variables were converted into numerical format.

Gender
Original	Encoded
Male	1
Female	0
Work Experience
Original	Encoded
Yes	1
No	0
Placement Status
Original	Encoded
Placed	1
Not Placed	0
One-Hot Encoding

The following categorical variables were encoded using:

pd.get_dummies()
Encoded Features
hsc_s
degree_t
specialisation

Generated Features:

hsc_s_Commerce
hsc_s_Science
degree_t_Others
degree_t_Sci&Tech
specialisation_Mkt&HR
📊 Exploratory Data Analysis (EDA)

The following visual analyses were performed.

1. Placement Distribution
sns.countplot(x='status')

Purpose:

Compare placed and not placed students.
2. Degree Percentage vs Placement
sns.boxplot(x='status', y='degree_p')

Purpose:

Analyze the relationship between degree performance and placement.
3. Work Experience vs Placement
sns.countplot(x='workex', hue='status')

Purpose:

Study the impact of work experience on placement.
4. Employability Test Score vs Placement
sns.boxplot(x='status', y='etest_p')

Purpose:

Analyze whether employability scores influence placement.
🧠 Feature Engineering

After encoding, the final features used for model training were:

gender
ssc_p
hsc_p
degree_p
workex
etest_p
mba_p
hsc_s_Commerce
hsc_s_Science
degree_t_Others
degree_t_Sci&Tech
specialisation_Mkt&HR
ssc_b_Others
hsc_b_Others
🤖 Machine Learning Model
Algorithm Used
Logistic Regression
model = LogisticRegression(max_iter=1000)
Why Logistic Regression?
Suitable for binary classification
Fast and efficient
Easy to interpret
Provides prediction probabilities
Works well on structured datasets
📚 Model Training
Train-Test Split
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
Data Split
Training Data = 80%
Testing Data = 20%
📈 Model Evaluation

The following evaluation techniques were used:

Accuracy Score
accuracy_score()

Measures overall prediction accuracy.

Confusion Matrix
confusion_matrix()

Provides:

True Positives
True Negatives
False Positives
False Negatives
Classification Report
classification_report()

Provides:

Precision
Recall
F1-Score
Support
💾 Model Saving

The trained model was saved using Pickle.

pickle.dump(model, open("placement_model.pkl", "wb"))

This allows the model to be reused without retraining.

🌐 Streamlit Web Application

A professional web interface was developed using Streamlit.

User Inputs
Student Name
Gender
SSC Percentage
SSC Board
HSC Percentage
HSC Board
HSC Stream
Degree Percentage
Degree Type
Work Experience
Employability Test Score
MBA Percentage
MBA Specialisation
Prediction Features

The application provides:

✅ Real-Time Placement Prediction

✅ Confidence Score

✅ Progress Indicator

✅ Student Summary

✅ Input Validation

✅ Professional Dashboard Layout

Prediction Output
If Placed
🎉 Kartik Arora is likely to be PLACED

Displays:

Placement Confidence
Progress Bar
Success Message
Balloons Animation
If Not Placed
❌ Kartik Arora is likely to be NOT PLACED

Displays:

Prediction Confidence
Progress Bar
Error Message
🎯 Project Workflow
CSV Dataset
↓
Data Understanding
↓
Data Cleaning
↓
Label Encoding
↓
One-Hot Encoding
↓
Exploratory Data Analysis
↓
Train-Test Split
↓
Logistic Regression Model
↓
Accuracy Evaluation
↓
Confusion Matrix
↓
Classification Report
↓
Model Saving (Pickle)
↓
Streamlit Web Application
↓
Real-Time Placement Prediction
🛠 Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Pickle
Streamlit
Development Tools
Visual Studio Code
GitHub
Streamlit
📂 Project Structure
Student-Placement-Prediction/

├── app.py
├── placement_analysis.py
├── placement_model.pkl
├── placement.csv
├── requirements.txt
└── README.md
⚙️ Installation Guide
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py
Open Browser
http://localhost:8501
🎓 Learning Outcomes

This project demonstrates:

Data Understanding
Data Cleaning
Data Preprocessing
Data Encoding
Exploratory Data Analysis
Feature Engineering
Logistic Regression
Model Evaluation
Pickle Serialization
Streamlit Deployment
Machine Learning Application Development
👨‍💻 Developer

Kartik Arora

Bachelor of Computer Applications (BCA)

Machine Learning Project

📄 License

This project is developed for educational and learning purposes.

Conclusion

The Student Placement Prediction System successfully demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, evaluation, deployment, and real-time prediction through a web application.

The project provides practical experience in applying machine learning techniques to solve real-world placement prediction problems.