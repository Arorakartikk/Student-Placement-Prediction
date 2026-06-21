import streamlit as st
import pandas as pd 
import pickle

st.set_page_config(
    page_title="Student Placement Predictor", #Student Placement Prediction System title
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>

/* Main Page */
.main {
    padding-top: 1rem;
}

/* Predict Button */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    width: 300px !important;
}

</style>
""", unsafe_allow_html=True)

st.title(" Student Placement Prediction System")

st.markdown("""
### Predict Placement Chances Using Machine Learning

This application analyzes academic performance,
work experience, employability scores and MBA specialization
to predict whether a student is likely to be placed.

**Model:** Logistic Regression

**Accuracy:** 88%
""")

st.divider()
with st.sidebar:

    st.header("📊 Project Information")

    st.metric(
        "Model Accuracy",
        "88%"
    )

    st.metric(
        "Algorithm",
        "Logistic Regression"
    )

    st.info("""
Technologies Used

• Python

• Pandas

• Scikit-Learn

• Streamlit
""")
    st.success("Placement Prediction ML System")

def load_model(): # Load model
    return pickle.load(open("placement_model.pkl", "rb")) 

model = load_model()
importance_df = pd.DataFrame({
    "Feature": model.feature_names_in_,
    "Importance": model.coef_[0]
})

importance_df["Importance"] = importance_df["Importance"].abs()

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)
name = st.text_input("Student Name")


gender = st.selectbox( # Creates box where user can select gender 
    "Gender",
    ["Male", "Female"]
)
ssc_p = st.number_input( # Creates a box for numbers.
    "Secondary School Certificate (SSC) Percentage",
    min_value=0.0,
    max_value=100.0,
     key="ssc"
)

ssc_b = st.selectbox(
    "Secondary School Certificate (SSC) Percentage Board",
    ["Central", "Others"],
    key="ssc_b"
)

hsc_p = st.number_input(
    "Higher Secondary Certificate (HSC) Percentage",
    min_value=0.0,
    max_value=100.0,
    key="hsc"
)
hsc_b = st.selectbox(
    "Higher Secondary Certificate (HSC) Board",
    ["Central", "Others"],
    key="hsc_b"
)

hsc_s = st.selectbox(
    ""Higher Secondary Certificate (HSC) Stream",
    ["Commerce", "Science", "Arts"],
    key="hsc_s"
)

degree_p = st.number_input(
    "Degree Percentage",
    min_value=0.0,
    max_value=100.0,
    key="degree"
)
degree_t = st.selectbox(
    "Degree Type",
    ["Sci&Tech", "Comm&Mgmt", "Others"],
    key="degree_t"
)

workex = st.selectbox(     # user can select whether he has work experience or not 
    "Work Experience",     # Selected value gets stored in workex
    ["No", "Yes"]
)
etest_p = st.number_input(   #Score obtained in the employability/aptitude test.
    "Employability Test Percentage", # the model learned from this feature during training.
    min_value=0.0,                  # Generally, higher employability test scores may increase placement chances.
    max_value=100.0,
    key="etest"
)
mba_p = st.number_input( #represents the student's MBA academic performance.
    "MBA Percentage",
    min_value=0.0,
    max_value=100.0,
    key="mba"
)
specialisation = st.selectbox(
    "MBA Specialisation", #The model learned whether specialization has any relationship with placement.
    ["Mkt&Fin", "Mkt&HR"],
    key="specialisation"
)

# st.write("Gender:", gender)                # Used to check if all imput are working or not 
# st.write("SSC %:", ssc_p)                             
# st.write("HSC %:", hsc_p)
# st.write("Degree %:", degree_p)
# st.write("Work Experience:", workex)
# st.write("Employability Test %:", etest_p)
# st.write("MBA Percentage:", mba_p)
# st.write("MBA Specialisation:", specialisation)

predict_btn = st.button(
    "🚀 Predict Placement",
    use_container_width=True
)

if predict_btn:

    # Validation
    if (
        ssc_p == 0 and
        hsc_p == 0 and
        degree_p == 0 and
        etest_p == 0 and
        mba_p == 0
    ):
        st.warning("⚠️ Please enter student details before prediction.")
        st.stop()

    # Create DataFrame
    input_data = pd.DataFrame([{

        "gender": 1 if gender == "Male" else 0,
        "ssc_p": ssc_p,
        "hsc_p": hsc_p,
        "degree_p": degree_p,
        "workex": 1 if workex == "Yes" else 0,
        "etest_p": etest_p,
        "mba_p": mba_p,

        "hsc_s_Commerce": 1 if hsc_s == "Commerce" else 0,
        "hsc_s_Science": 1 if hsc_s == "Science" else 0,

        "degree_t_Others": 1 if degree_t == "Others" else 0,
        "degree_t_Sci&Tech": 1 if degree_t == "Sci&Tech" else 0,

        "specialisation_Mkt&HR": 1 if specialisation == "Mkt&HR" else 0,

        "ssc_b_Others": 1 if ssc_b == "Others" else 0,
        "hsc_b_Others": 1 if hsc_b == "Others" else 0

    }])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    st.divider()
    st.subheader("📈 Prediction Result")
    # st.write(input_data) #Display the table
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    # Output
    if prediction == 1:

        confidence = probability[1] * 100

        st.success(f"🎉 {name} is likely to be PLACED")


        st.progress(float(probability[1]))

        st.balloons()
    else:
        confidence = probability[0] * 100

        st.error(f"❌ {name} is likely to be NOT PLACED")


        st.progress(float(probability[0]))

    st.divider()
    st.subheader("📄 Student Profile Summary")

summary = pd.DataFrame({
    "Feature": [
        "Name",
        "SSC %",
        "HSC %",
        "Degree %",
        "MBA %",
        "Work Experience"
    ],
    "Value": [
        name,
        ssc_p,
        hsc_p,
        degree_p,
        mba_p,
        workex
    ]
})

st.table(summary)

st.divider()

st.caption(
    "Developed by Kartik Arora | Machine Learning Placement Prediction Project | Student Placement Prediction System"
)
       



