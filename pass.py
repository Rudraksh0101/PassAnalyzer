import streamlit as st
import hashlib
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# -----------------------------
# Feature Extraction Function
# -----------------------------
def extract_features(password):
    length = len(password)
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if not c.isalnum())

    return [length, upper, lower, digits, special]

# -----------------------------
# Dataset
# -----------------------------
data = [
    ("12345", 0), ("password", 0), ("admin123", 0),
    ("Cyber123", 1), ("Cyber@123", 2), ("Str0ng@Pass!", 2),
    ("helloWorld1", 1), ("P@ss", 1), ("weakpass", 0),
    ("Very$trongP@ssw0rd", 2), ("Test@1234", 2),
    ("qwerty", 0), ("Hello123", 1)
]

X = [extract_features(pwd) for pwd, _ in data]
y = [label for _, label in data]

X = np.array(X)
y = np.array(y)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier()
model.fit(X_train, y_train)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Password Analyzer", page_icon="🔐")

st.title("🔐 AI Password Security Analyzer")
st.subheader("Evaluate your password strength and get a secure hash")
st.write("**Created by Rudra Kumar Sharma**")
with st.expander("ℹ️ Project Details"):
    st.write("This project uses a simple machine learning model to analyze password strength based on features like length, uppercase letters, lowercase letters, digits, and special characters. It also generates a secure SHA-256 hash of the password for demonstration purpose only.")
st.markdown("### Check password strength and generate secure hash")

st.markdown("---")

password = st.text_input("🔑 Enter your password", type="password")

if st.button("🚀 Analyze Password"):

    if password:
        # -----------------------------
        #     Progress Bar Animation
        # -----------------------------
        progress = st.progress(0)
        status_text = st.empty()

        for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
            status_text.text(f"Analyzing your password... {i}%")

        status_text.text("Analysis Complete ✅")

        # -----------------------------
        # Prediction
        # -----------------------------
        features = np.array([extract_features(password)])
        prediction = model.predict(features)[0]

        if prediction == 0:
            strength = "🔴 Weak"
            suggestion = "Use longer passwords with symbols and numbers."
        elif prediction == 1:
            strength = "🟡 Medium"
            suggestion = "Increase complexity using special characters."
        else:
            strength = "🟢 Strong"
            suggestion = "Good password. Maintain this level of security."

        # -----------------------------
        #           Hashing
        # -----------------------------
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # -----------------------------
        #         Results UI
        # -----------------------------
        st.subheader("🔎 Analysis Result")

        st.metric("Password Strength", strength)

        st.markdown("### 🔐 SHA-256 Hash")
        with st.expander("🔍 View Hash"):
            st.code(hashed_password, language="text")

        st.markdown("### 💡 Suggestion")
        st.info(suggestion)

    else:
        st.warning("⚠️ Please enter a password.")

st.markdown("---")
st.caption("⚠️ This is a demonstration tool. Do not use for real-world password security.")