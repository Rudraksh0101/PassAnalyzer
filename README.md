# 🔐 AI-Based Password Security Analyzer

An AI-enabled web application that evaluates password strength using a machine learning model and generates a secure SHA-256 hash.

---

## 📌 Features

- 🔍 Password strength prediction (Weak / Medium / Strong)
- 🤖 Machine Learning model (Random Forest)
- 🔐 Secure hashing using SHA-256
- 📊 Feature-based analysis (length, characters, digits, symbols)
- ⚡ Interactive Streamlit UI with progress bar

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-learn
- hashlib

---

## 🚀 How It Works

1. User enters a password  
2. System extracts features:
   - Length  
   - Uppercase letters  
   - Lowercase letters  
   - Digits  
   - Special characters  
3. Features are passed to a trained ML model  
4. Model predicts password strength  
5. Password is converted into SHA-256 hash  
6. Results are displayed with suggestions  

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Rudra7439/password-analyzer.git
cd password-analyzer
