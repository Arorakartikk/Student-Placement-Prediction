import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv("placement.csv")
print(df.head())

print("\n Data understanding")
#Number of rows (students) and Number of columns (features)
print(df.shape) 
#Shows all column names
print(df.columns)
#Data types (int, float, object) Missing values
print(df.info())
#Mean Min / Max Distribution
print(df.describe())

print("\n Data cleaning")
#“Removing the useless column sl_no from the dataset permanently”
df.drop("sl_no", axis=1, inplace=True)
print(df.head())
print(df.columns)

print("\n Encoding")
df['gender'] = df['gender'].map({'M': 1, 'F': 0}) #Converting male to 1 value,female to 0 
df['workex'] = df['workex'].map({'Yes': 1, 'No': 0}) #Converting prior experience to 1 value, no experience to 0 
df['status'] = df['status'].map({'Placed': 1, 'Not Placed': 0}) #Converting placed to 1 value, not placed to 0 
print(df.head())

#multi category encoding 
df = pd.get_dummies(df, columns=['hsc_s', 'degree_t', 'specialisation'], drop_first=True)
print("\n")
print(df.head())

print("\n Exploratory Data Analysis")
sns.countplot(x='status', data=df)
plt.title("Placement Distribution")
plt.show()

sns.boxplot(x='status', y='degree_p', data=df) # CGPA VS PLACEMENT
plt.title("Degree Percentage vs Placement")
plt.show()

sns.countplot(x='workex', hue='status', data=df) # Work Experience vs Placement
plt.title("Work Experience vs Placement")
plt.show()

sns.boxplot(x='status', y='etest_p', data=df)
plt.title("Employability Test vs Placement") #Test Score vs Placement
plt.show()

print(df[['gender','workex','status']].head())

# Machine Learning Model (Prediction)
# Goal:
# Predict status (Placed / Not Placed)
print("\n Machine Learning ")
df = pd.get_dummies(df, drop_first=True)                #Pandas creates new column names based on the exact values present.
print(df.columns.tolist())

X = df.drop("status", axis=1) #X contains all the information about a student.
y = df["status"]#y contains the answer:

from sklearn.model_selection import train_test_split       #Dataset-215 students total.
X_train, X_test, y_train, y_test = train_test_split(       # Approximately:
    X,                                                     # 172 students → Training
    y,                                                     # 43 students → Testing
    test_size=0.2,                                         # Training Data-Used for learning patterns.
    random_state=42                                        # Testing Data- Used to check if the model learned correctly.
)           

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)                   #empty model.

model.fit(X_train, y_train)                                 #Train the model using historical student data
                                                            # Learn patterns

y_pred = model.predict(X_test)                              # 1 predition of Placed data 
                                                            #Predict placement

from sklearn.metrics import accuracy_score                  
accuracy = accuracy_score(y_test, y_pred)                   # used to check the actuall acurracy of our model 
print("Accuracy:", accuracy)                                #Measure performance

print("\n Model Evaulation ")
from sklearn.metrics import confusion_matrix                #Predicted
cm = confusion_matrix(y_test, y_pred)                       #               0                         1
print(cm)                                                   # Actual 0     TN(True Negatives)         FP(False Positives)
                                                            # Actual 1     FN(False Negative)         TP(True Positives)

                                                            #Correct Predictions:
                                                            #9 + 29 = 38(TN+TP)
                                                            #Wrong Predictions:
                                                            #3 + 2 = 5(FP+TP)

print("\nClassification Report")                          #Precision- Out of all students predicted as placed, how many were actually placed?
from sklearn.metrics import classification_report         #Recall- Out of all students who were actually placed, how many did the model find?
print(classification_report(y_test, y_pred))              #F1 Score- Precision + Recall
print("\n Out of the students your model predicted as Not Placed: 82% were actually Not Placed"
"\n Out of the 12 students who were actually Not Placed:The model correctly found 75% of them")              #support- How many examples existed in the test set

print("\n Saving the Trained Mode")
pickle.dump(model, open("placement_model.pkl", "wb")) # This creates a file: placement_model.pkl which stores everything the model learned.
print("Model saved successfully!")

print(X.columns)  # used to check what all columns are in our file and for prediction the student must enter all these values otherwise the model wont know what its looking at 
new_student = [[   #New Student Data
    1, 85, 80, 78, 1, 82, 75,
    0, 1, 0, 1, 0, 0, 0     
    #  1,      # gender
    # 85,     # ssc_p
    # 80,     # hsc_p
    # 78,     # degree_p
    # 1,      # workex
    # 82,     # etest_p
    # 75,     # mba_p
    # 0,      # hsc_s_Commerce
    # 1,      # hsc_s_Science
    # 0,      # degree_t_Others
    # 1,      # degree_t_Sci&Tech
    # 0,      # specialisation_Mkt&HR
    # 0,      # ssc_b_Others
    # 0       # hsc_b_Others
]]

import pandas as pd
new_student_df = pd.DataFrame(  #Convert to DataFrame
    new_student,
    columns=X.columns
)
prediction = model.predict(new_student_df) #Prediction

if prediction[0] == 1:
    print("Prediction: Placed")  #Make Output Human-Friendly
else:
    print("Prediction: Not Placed")