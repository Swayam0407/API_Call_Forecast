# 📊 **Time Series Prediction Project**  
*Predicting API Call Times with Machine Learning Models and an Interactive Interface!*  

---

## ⚠️ **Disclaimer**  
Due to size constraints, the **model files and related code** are not included in this repository. The current focus is on the interface. The complete project, including models and datasets, will be available soon.  

---

## 🧠 **Project Overview**  
This project tackles the problem of predicting API call times using **time series analysis** and machine learning techniques. The solution follows a structured approach:  

### 🔍 **Problem Statement**  
1. **Identify the top 3 most-called APIs** (e.g., A8, A1, A7).  
2. **Filter data** for each API and store it in separate files (e.g., A8.csv, A1.csv, A7.csv).  
3. **Build multiple models** for each API and determine the best-performing model for predictions.  
4. **Deploy an interface** for real-time predictions of the top 3 APIs.  

---

## 🧪 **Model Testing and Evaluation**  
The following steps were performed to identify the best model for each API:  

### Step 1: Data Preprocessing  
- Converted `Time of Call` to a datetime format for precision.  
- Resampled data at a minute level for accurate analysis.  
- Cleaned and filtered data to handle missing values.  

### Step 2: Models Tested  
Four models were tested for each API:  
1. **ARIMA**  
2. **Exponential Smoothing (ETS)**  
3. **Random Forest**  
4. **Linear Regression**  

Each model was evaluated based on two metrics:  
- **Root Mean Squared Error (RMSE)**  
- **Mean Absolute Error (MAE)**  

### Step 3: Results  
After extensive testing, **Exponential Smoothing (ETS)** emerged as the best model for all three APIs (A2, A7, and A9) based on its performance in terms of RMSE and MAE.  

---

## 🖥️ **The Matrix-Inspired Interface**  
The project includes a sleek **Matrix-themed interface** for making predictions:  

### **Features**:  
- A **dark, green-on-black theme**, replicating the iconic Matrix aesthetic.  
- Scrolling binary code animation with intuitive input fields 

### **User Flow**:  
1. **Input the API code** and desired number of predictions in the provided fields.  
2. Hit the **"Predict" button**, styled like a command terminal.  
3. View the prediction results in a clean, tabular format.

   
---

## 🛠️ **Technologies Used**  
- **Python**: Data processing, model training, and predictions.  
- **Pandas**: For data manipulation and preprocessing.  
- **Statsmodels & scikit-learn**: For building and evaluating models.  
- **Flask**: Backend framework for deployment.  
- **HTML/CSS/JavaScript**: Frontend for the user interface.

