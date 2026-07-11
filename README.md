# 🎓 Student Performance Prediction

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic and academic attributes using various regression algorithms.

## 🚀 Live Demo

> Add your Render deployment link here

Example:
```
https://your-app-name.onrender.com
```

---

## 📌 Project Overview

This project predicts a student's **Math Score** using features such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The project covers the complete machine learning lifecycle:

- Data Ingestion
- Data Transformation
- Model Training
- Model Evaluation
- Model Serialization
- Flask Web Application
- Deployment

---

## 📊 Dataset

Dataset: Student Performance Dataset

Target Variable:
- **Math Score**

Input Features:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- CatBoost
- XGBoost
- Flask
- Pickle

### Tools

- Git
- GitHub
- Render

---

## 📂 Project Structure

```
PROJECT-1/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Pipeline

### 1. Data Ingestion

- Read dataset
- Split into train/test
- Save datasets

### 2. Data Transformation

- Handle categorical features
- Standard Scaling
- One-Hot Encoding
- Create preprocessing pipeline

### 3. Model Training

Models used:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model is automatically selected based on evaluation metrics.

---

## 🌐 Web Application

The Flask application allows users to:

- Enter student details
- Predict Math Score instantly

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Move inside the project

```bash
cd your-repository
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

## 📷 Screenshots

### Home Page

(Add Screenshot)

### Prediction Page

(Add Screenshot)

### Prediction Result

(Add Screenshot)

---

## 🎯 Future Improvements

- Improve UI/UX
- Add Model Explainability
- Dockerize the application
- CI/CD Pipeline
- AWS Deployment
- User Authentication
- Database Integration

---
## 📚 Key Learnings

- Built an end-to-end Machine Learning pipeline
- Implemented modular project structure
- Trained and evaluated multiple regression models
- Created a Flask web application
- Deployed the project
- Gained hands-on experience in debugging and project deployment

## 👨‍💻 Author

**Siddhant**

GitHub:
https://github.com/Sidcool0311-ml

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!