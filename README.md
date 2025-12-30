# End-to-End Machine Learning Project: Student Performance Prediction

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/22677ccc-f0a5-45d2-ae25-685ddc4c72f5" />

## Project Overview
This project focuses on predicting students’ exam scores using machine learning regression techniques based on their study habits, lifestyle choices, and well-being indicators. The goal is to demonstrate how data-driven insights can support academic decision-making and early intervention strategies in educational institutions.

The project follows an end-to-end data science workflow from data exploration and model development to deploying a predictive web application using Streamlit.

---

## Real-World Problem Statement
Academic performance is influenced by more than classroom instruction alone. Factors such as study time, attendance, sleep quality, mental health, and digital media usage significantly impact student outcomes.

Educational stakeholders (teachers, counselors, school administrators) need data-driven tools to:
- Identify students at risk of underperforming
- Understand which factors most affect academic success
- Provide targeted academic or wellness interventions

This project simulates a real-life scenario by building a regression model that predicts exam scores based on students’ behavioral and lifestyle attributes.

---

## Dataset Description
- Records: 1,000 students
- Target Variable: `exam_score`
- Features include:
  - Study hours per day
  - Social media hours
  - Netflix hours
  - Attendance percentage
  - Sleep hours
  - Exercise frequency
  - Mental health rating
  - Demographic and lifestyle indicators

---

## Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- StatsModels
- Jupyter Notebook
- Streamlit

---

## Exploratory Data Analysis (EDA)
EDA was performed to understand data distribution, detect anomalies, and identify relationships between features and exam performance.

Key insights:
- Study hours per day show a strong positive correlation with exam scores
- Social media and Netflix usage negatively impact performance
- Mental health, sleep duration, and physical activity significantly improve outcomes

---

## Data Preprocessing
- Handled missing values in `parental_education_level` using mode imputation
- Verified absence of duplicate records
- Selected relevant numerical features for modeling
- Standardized feature variables to improve model stability

---

## Model Development
- Model Used: Linear Regression
- Train–Test Split: 80% training, 20% testing
- Feature Scaling: StandardScaler

The linear regression model was chosen for its interpretability and suitability for continuous target prediction in educational analytics.

---

## Model Evaluation
Performance metrics on the test dataset:
- R² Score: ~0.90
- RMSE: ~5.07

This indicates that the model explains approximately 90% of the variance in students’ exam scores, with predictions typically within ±5 marks of actual values.

---

## Model Interpretation
Regression coefficients revealed:
- Study hours per day as the strongest positive predictor
- Mental health rating, sleep hours, and exercise frequency positively influence performance
- Excessive social media and Netflix usage negatively affect exam scores

Statistical validation using OLS regression confirmed that all selected predictors were statistically significant.

---

## Deployment: Streamlit Predictive App
To demonstrate real-world usability, the trained model was deployed as an interactive Streamlit web application.

### App Capabilities:
- Accepts student lifestyle inputs via a user-friendly interface
- Predicts exam scores in real time
- Demonstrates how machine learning models can be converted into decision-support tools

---

## Project Structure
├── data

│ └── student_habits_performance.csv

├── notebook

│ └── student_performance_regression.ipynb

├── app

│ └── exam_score_app.py

├── requirements.txt

├── README.md


---

## Future Improvements
- Experiment with advanced models (Ridge, Lasso, Random Forest)
- Add cross-validation and hyperparameter tuning
- Deploy the Streamlit app to Streamlit Cloud
- Introduce classification for risk-level prediction

## Live Demo
The model has been deployed as an interactive Streamlit application.

**Live App:** https://student-performance-predictor.streamlit.app

Users can input student lifestyle details and receive real-time exam score predictions.

---

## Author

**Idris Oladejo**  
Data Analyst | Machine Learning Enthusiast  

Skilled in **Python, SQL, Excel, Power BI**, **SPSS for Statistical Analysis**, and **predictive analytics**, with a strong focus on transforming data into actionable insights and building end-to-end analytical and machine learning solutions.

### Collaboration & Opportunities
I am open to **teamwork, technical collaborations, freelance gigs, and internship opportunities** and **job opportunities** in data analytics and machine learning.  
If you’re interested in working together or discussing potential opportunities, feel free to reach out.

### Contact
- 📞 Phone: +234 702 506 2857  
- 📧 Email: oladejoidris55@gmail.com

