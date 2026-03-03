import streamlit as st

# Page Config
st.set_page_config(page_title="HerHeart", page_icon="❤️", layout="wide")

# Sidebar Navigation
st.sidebar.title("❤️ HerHeart")
page = st.sidebar.radio("Go to", ["Home", "Risk Checker", "Features", "About"])

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.title("❤️ Welcome to HerHeart")
    st.subheader("Female-Focused Heart Risk Awareness Platform")

    st.write("""
    HerHeart is designed to highlight how heart symptoms in women 
    can be different from traditional indicators.
    """)

    st.image("https://images.unsplash.com/photo-1588776814546-ec7e90a3e9e3", use_container_width=True)

    st.success("Use the sidebar to explore the Risk Checker and Features.")

# ---------------- RISK CHECKER PAGE ----------------
elif page == "Risk Checker":
    st.title("🩺 Heart Risk Checker")

    st.header("Enter Your Details")

    age = st.slider("Age", 18, 80)
    family_history = st.selectbox("Family History of Heart Disease?", ["No", "Yes"])

    st.header("Select Your Symptoms")

    chest_pain = st.checkbox("Chest Pain")
    short_breath = st.checkbox("Shortness of Breath")
    fatigue = st.checkbox("Extreme Fatigue")
    nausea = st.checkbox("Nausea / Vomiting")
    jaw_pain = st.checkbox("Jaw Pain")
    back_pain = st.checkbox("Upper Back Pain")
    dizziness = st.checkbox("Dizziness")

    if st.button("Calculate Risk"):

        generic_score = 0
        female_score = 0

        if chest_pain:
            generic_score += 3
        if short_breath:
            generic_score += 2

        if fatigue:
            female_score += 2
        if nausea:
            female_score += 2
        if jaw_pain:
            female_score += 2
        if back_pain:
            female_score += 2
        if dizziness:
            female_score += 2

        if family_history == "Yes":
            generic_score += 2
            female_score += 2

        total_female = generic_score + female_score

        st.subheader("Results")

        st.write("Risk Score:", total_female)

        if total_female >= 7:
            st.error("High Risk! Please consult a doctor immediately.")
        elif total_female >= 4:
            st.warning("Moderate Risk. Consider medical evaluation.")
        else:
            st.success("Low Risk. Stay healthy!")

# ---------------- FEATURES PAGE ----------------
elif page == "Features":
    st.title("✨ Features")

    st.write("""
    ✔ Female-focused symptom analysis  
    ✔ Easy risk scoring  
    ✔ Awareness-driven platform  
    ✔ Simple and accessible interface  
    """)

# ---------------- ABOUT PAGE ----------------
elif page == "About":
    st.title("👩‍⚕️ About HerHeart")

    st.write("""
    HerHeart is a student-built awareness project 
    focusing on how heart disease symptoms in women 
    are often under-recognized.

    This platform demonstrates how female-adjusted 
    scoring can highlight different risk patterns.
    """)

    st.info("This is an educational demo and not a medical diagnosis tool.")